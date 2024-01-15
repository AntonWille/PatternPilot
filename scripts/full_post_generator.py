import pandas as pd
from sqlalchemy import create_engine, text

def fetch_question(engine, question_id):
    query = f"SELECT * FROM questions WHERE question_id = {question_id}"
    df = pd.DataFrame(engine.execute(text(query)))
    return df.iloc[0].to_dict()

def fetch_answers(engine, question_id):
    query = f"SELECT * FROM answers WHERE question_id = {question_id}"
    return pd.DataFrame(engine.execute(text(query)))

def fetch_comments(engine, post_ids):
    query = f"SELECT * FROM comments WHERE commentable_id IN ({','.join(map(str, post_ids))})"
    df = pd.DataFrame(engine.execute(text(query)))
    if df.empty:
        return pd.DataFrame(columns=['comment_id', 'commentable_type', 'commentable_id', 'owner_id',
                                            'owner_display_name', 'body', 'score'])
    return df

def fetch_all_question_ids(engine):
    query = "SELECT question_id FROM questions"
    df = pd.DataFrame(engine.execute(text(query)))
    return df['question_id'].tolist()

def create_post_file(engine, question_id):
    question = fetch_question(engine, question_id)
    filename = f"data/html/{question['score']}{question['category']}_{question_id}.html"
    answers_df = fetch_answers(engine, question_id)

    post_ids = [question_id]
    if not answers_df.empty:
         post_ids += answers_df['answer_id'].tolist()

    comments_df = fetch_comments(engine, post_ids)

    text = f" <h2> Title: {question['title']} </h2>"
    text += f" <h4> {question['owner_display_name']}, question_id: {question_id} </h4>"
    text += f"Score: {question['score']}, Tags: {question['tags']} <br>"
    text += question['body']

    question_comments = comments_df[comments_df['commentable_id'] == question_id]
    for _, comment in question_comments.iterrows():
        text += f"<h4> {comment['owner_display_name']}, Id: {comment['comment_id']} Score: {comment['score']}: </h4>"
        text += comment['body']
        text += "<br>"

    for _, answer in answers_df.iterrows():
        text += "------------------------------------------------------------------ <br>"
        text += f"<h3> {answer['owner_display_name']}, Id: {answer['answer_id']}, Score: {answer['score']}: </h3>"
        text += answer['body']

        answer_comments = comments_df[comments_df['commentable_id'] == answer['answer_id']]
        for _, comment in answer_comments.iterrows():
            text += f"<h4> {comment['owner_display_name']}, Comment {comment['comment_id']} Score: {comment['score']}: </h4>"
            text += comment['body']
            text += "<br>"

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
