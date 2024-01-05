import sys
from stack_overflow_api import StackOverflowAPI
from data_loader import DataLoader
import pandas as pd
from sqlalchemy import create_engine

def process_response(response):
    if not response:
        raise Exception('No data found')
    else:
        return pd.DataFrame(response)

def main(category, additional_tags, page=1):
    engine = create_engine('postgresql://postgres@localhost:5432/pattern_pilot_development')
    so_client = StackOverflowAPI()
    tags = [category] + additional_tags
    questions = so_client.fetch_questions(tags=tags, page=page)
    questions_df = process_response(questions['items'])
    questions_df['category'] = category
    questionsLoader = DataLoader(questions_df)
    questionsLoader.to_db(engine, 'questions')

    answers = so_client.fetch_answers(questions_df)
    answers_df = process_response(answers)
    answersLoader = DataLoader(answers_df)
    answersLoader.to_db(engine, 'answers')

    questions_comments = so_client.fetch_questions_comments(questions_df)
    questions_comments_df = process_response(questions_comments)
    questionsCommentsLoader = DataLoader(questions_comments_df)
    questionsCommentsLoader.to_db(engine, 'questions_comments')

    answers_comments = so_client.fetch_answers_comments(answers_df)
    answers_comments_df = process_response(answers_comments)
    answersCommentsLoader = DataLoader(answers_comments_df)
    answersCommentsLoader.to_db(engine, 'answers_comments')

if __name__ == "__main__":
    main('python', [], page=1)
