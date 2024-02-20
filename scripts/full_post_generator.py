import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime, timezone

def fetch_question_ids(conn):
    query = "SELECT question_id FROM questions"
    df = pd.DataFrame(conn.execute(text(query)))
    return df['question_id'].tolist()

def fetch_question(conn, question_id):
    query = f"SELECT * FROM questions WHERE question_id = {question_id}"
    df = pd.DataFrame(conn.execute(text(query)))
    return df.iloc[0].to_dict()

def fetch_answers(conn, question_id):
    query = f"SELECT * FROM answers WHERE question_id = {question_id}"
    return pd.DataFrame(conn.execute(text(query)))

def fetch_questions_comments(conn, question_id):
    query = f"SELECT * FROM questions_comments WHERE parent_id = {question_id}"
    df = pd.DataFrame(conn.execute(text(query)))
    if df.empty:
        return pd.DataFrame(columns=['comment_id', 'parent_id', 'owner_id',
                                            'owner_display_name', 'body', 'score'])
    return df

def fetch_answers_comments(conn, post_ids):
    query = f"SELECT * FROM answers_comments WHERE parent_id IN ({','.join(map(str, post_ids))})"
    df = pd.DataFrame(conn.execute(text(query)))
    if df.empty:
        return pd.DataFrame(columns=['comment_id', 'parent_id', 'owner_id',
                                            'owner_display_name', 'body', 'score'])
    return df

def format_question(question):
    created_at = datetime.fromtimestamp(question['creation_date'], timezone.utc)
    text = f" <h2> Title: {question['title']} </h2>"
    text += f" <h4> {question['owner_display_name']}, question_id: {question['question_id']}, created_at: {created_at} </h4>"
    text += f"Score: {question['score']}, Tags: {question['tags']} <br>"
    text += question['body']
    return text

def format_comments(comments):
    text = ""
    for _, comment in comments.iterrows():
        created_at = datetime.fromtimestamp(comment['creation_date'], timezone.utc)
        text += f"<h4> Comment by {comment['owner_display_name']}, Score: {comment['score']}, Id: {comment['comment_id']}, created_at: {created_at} </h4>"
        text += comment['body']
    return text

def format_answers(answers, answers_comments):
    text = ""
    for _, answer in answers.iterrows():
        created_at = datetime.fromtimestamp(answer['creation_date'], timezone.utc)
        is_accepted = "✔️" if answer['is_accepted'] else ""
        text += '<hr>'
        text += f"<h3> {is_accepted} Answer by {answer['owner_display_name']}, Id: {answer['answer_id']}, Score: {answer['score']}, created_at: {created_at} </h3>"
        text += answer['body']

        comments = answers_comments[answers_comments['parent_id'] == answer['answer_id']]
        if not comments.empty:
            text += format_comments(comments)
    return text

def create_post_file(conn, question_id):
    question = fetch_question(conn, question_id)
    filename = f"data/html/{question['score']}{question['category']}_{question_id}.html"

    with open(filename, 'w') as f:
        question_text = format_question(question)
        question_comments = fetch_questions_comments(conn, question_id)
        question_comments.sort_values(by='score', ascending=False)

        f.write(question_text)

        if not question_comments.empty:
            question_comments_text = format_comments(question_comments)
            f.write(question_comments_text)

        answers_df = fetch_answers(conn, question_id)
        if not answers_df.empty:
            answers_df.sort_values(by='score', ascending=False)
            answer_ids = answers_df['answer_id'].tolist()
            answer_comments = fetch_answers_comments(conn, answer_ids)
            answer_comments.sort_values(by='score', ascending=False)
            answers_text = format_answers(answers_df, answer_comments)
            f.write(answers_text)

def main():
    engine = create_engine('postgresql://postgres@localhost:5432/pattern_pilot_development')
    with engine.connect() as conn:
        ids = fetch_question_ids(conn)
        for question_id in ids:
            create_post_file(conn, question_id)

if __name__ == "__main__":
    main()
