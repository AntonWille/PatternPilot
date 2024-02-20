from stack_overflow_api import StackOverflowAPI
from data_loader import DataLoader
import pandas as pd
from sqlalchemy import create_engine

def process_response(response):
    if not response:
        raise Exception('No data found')
    else:
        return pd.DataFrame(response)

def fetch_questions(so_client, category, params):
    questions = so_client.fetch_questions(params)
    questions_df = process_response(questions['items'])
    questions_df['category'] = category
    return questions_df

def fetch_answers(so_client, question_ids, params):
    answers = so_client.fetch_answers(question_ids, params)
    return process_response(answers)

def main(category, additional_tags, page=1):
    engine = create_engine('postgresql://postgres@localhost:5432/pattern_pilot_development')
    so_client = StackOverflowAPI()
    params = {'tagged': [category] + additional_tags,
              'sort': 'votes',
              'order': 'desc',
              'pagesize': 100,
              'page': page}

    questions_df = fetch_questions(so_client, category, params)
    questionsLoader = DataLoader(questions_df)
    questionsLoader.to_db(engine, 'questions')

    question_ids = questions_df['question_id'].tolist()

    questions_comments = so_client.fetch_comments(question_ids, 'questions', params)
    questions_comments_df = process_response(questions_comments)
    if not questions_comments_df.empty:
        questionsCommentsLoader = DataLoader(questions_comments_df)
        questionsCommentsLoader.to_db(engine, 'questions_comments')

    answers_df = fetch_answers(so_client, question_ids, params)
    answersLoader = DataLoader(answers_df)
    answersLoader.to_db(engine, 'answers')

    answer_ids = answers_df['answer_id'].tolist()

    answers_comments = so_client.fetch_comments(answer_ids, 'answers', params)
    answers_comments_df = process_response(answers_comments)
    if not answers_comments_df.empty:
        answersCommentsLoader = DataLoader(answers_comments_df)
        answersCommentsLoader.to_db(engine, 'answers_comments')

if __name__ == "__main__":
    main('python', [], page=4)
