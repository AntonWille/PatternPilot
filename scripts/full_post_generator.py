import pandas as pd
from sqlalchemy import create_engine, text
import html2text

def html_to_text(html):
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text_maker.bypass_tables = False
    return text_maker.handle(html)

def fetch_question(engine, question_id):
    query = f"SELECT * FROM questions WHERE question_id = {question_id}"
    return pd.DataFrame(engine.execute(text(query)))

def fetch_answers(engine, question_id):
    query = f"SELECT * FROM answers WHERE question_id = {question_id}"
    return pd.DataFrame(engine.execute(text(query)))

def fetch_comments(engine, post_ids):
    query = f"SELECT * FROM comments WHERE commentable_id IN ({','.join(map(str, post_ids))})"
    return pd.DataFrame(engine.execute(text(query)))

def fetch_all_question_ids(engine):
    query = "SELECT question_id FROM questions"
    df = pd.DataFrame(engine.execute(text(query)))
    return df['question_id'].tolist()

def create_post_file(engine, question_id):
    question_df = fetch_question(engine, question_id)
    filename = f"data/{question_df['score'][0]}{question_df['category'][0]}_{question_id}.txt"
    answers_df = fetch_answers(engine, question_id)

    h = html2text.HTML2Text()
    h.ignore_links = True

    post_ids = [question_id]
    if not answers_df.empty:
         post_ids += answers_df['answer_id'].tolist()
    comments_df = fetch_comments(engine, post_ids)
    if comments_df.empty:
        comments_df = pd.DataFrame(columns=['comment_id', 'commentable_type', 'commentable_id', 'owner_id', 'owner_display_name',
                                     'body', 'score'])
    text = f"Title: {question_df['title'].iloc[0]}, \n Question ID: {question_id} \n Score: {question_df['score'].iloc[0]} \n"
    text += f"Tags: {question_df['tags'].iloc[0]}\n"
    text += h.handle(question_df['body'].iloc[0])
    text += "\n"
    question_comments = comments_df[comments_df['commentable_id'] == question_id]
    for _, comment in question_comments.iterrows():
        text += f"Comment {comment['comment_id']}:\n"
        text += h.handle(comment['body'])
        text += "\n"

    for _, answer in answers_df.iterrows():
        text += f"Answer {answer['answer_id']}:\n"
        text += h.handle(answer['body'])
        text += "\n"

        answer_comments = comments_df[comments_df['commentable_id'] == answer['answer_id']]
        for _, comment in answer_comments.iterrows():
            text += f"Comment {comment['comment_id']}:\n"
            text += h.handle(comment['body'])
            text += "\n"

    with open(filename, 'w') as f:
        f.write(text)

def main():
    engine = create_engine('postgresql://postgres@localhost:5432/pattern_pilot_development')
    with engine.connect() as conn:
        question_ids = fetch_all_question_ids(conn)
        for question_id in question_ids:
            create_post_file(conn, question_id)

if __name__ == "__main__":
    main()
