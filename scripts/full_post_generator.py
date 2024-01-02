import pandas as pd
from sqlalchemy import create_engine, text

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

def create_post_file(engine, question_id, filename):
    question_df = fetch_question(engine, question_id)
    answers_df = fetch_answers(engine, question_id)

    post_ids = [question_id] + answers_df['answer_id'].tolist()
    comments_df = fetch_comments(engine, post_ids)

    with open(filename, 'w') as file:
        file.write(f"TAGS: {question_df['tags'].iloc[0]}\n")
        file.write(f"Title: {question_df['title'].iloc[0]}, Question ID: {question_id} \n\n")
        file.write(question_df['body'].iloc[0])
        file.write("\n\n")

        for _, answer in answers_df.iterrows():
            file.write(f"Answer {answer['answer_id']}:\n")
            file.write(answer['body'])
            file.write("\n\n")

            answer_comments = comments_df[comments_df['commentable_id'] == answer['answer_id']]
            for _, comment in answer_comments.iterrows():
                file.write(f"Comment {comment['comment_id']}:\n")
                file.write(comment['body'])
                file.write("\n\n")

        question_comments = comments_df[comments_df['commentable_id'] == question_id]
        for _, comment in question_comments.iterrows():
            file.write(f"Comment {comment['comment_id']}:\n")
            file.write(comment['body'])
            file.write("\n\n")

def main():
    engine = create_engine('postgresql://postgres@localhost:5432/pattern_pilot_development')
    with engine.connect() as conn:
        question_ids = fetch_all_question_ids(conn)
        for question_id in question_ids:
            create_post_file(conn, question_id, f"data/{question_id}.html")

if __name__ == "__main__":
    main()
