import sys, os
from stack_overflow_api import SORequest
import pandas as pd

def get_questions(tags=[], sort='votes', order='desc', pagesize=100, page=1):
    params = {
        'filter': '!6WPIomnm)E*eI', # include body and comment count for questions
        'pagesize': pagesize,
        'tagged': tags,
        'sort': sort,
        'order': order,
        'page': page
    }
    data = SORequest().fetch_data('questions', params)
    return data

def get_answers(question_ids, sort='votes', order='desc', pagesize=100, page=1):
    params = {
        'filter': '!6WPIomqomPQfa', # include body and comment count for answers
        'pagesize': pagesize,
        'sort': sort,
        'order': order,
        'page': page
    }

    chunked_ids = [question_ids[i:i + 100] for i in range(0, len(question_ids), 100)]
    all_responses = []
    for chunk in chunked_ids:
        formatted_ids = ';'.join(map(str, chunk))
        response = SORequest().fetch_data(f'questions/{formatted_ids}/answers', params)
        if response:
            all_responses.extend(response.get('items', []))
    return all_responses

def data_to_json(path, data):
    if not data or 'items' not in data:
        return None
    df = pd.DataFrame(data['items'])
    df.to_json(path, orient='records')
    return df

def data_to_csv(path, data):
    if not data or 'items' not in data:
        return None
    df = pd.DataFrame(data['items'])
    if not os.path.exists(path):
       df.to_csv(path, index=False)
    else:
       df.to_csv(path, mode='a', header=False, index=False)
    return df

def main(page=1, tags=[], mode='csv'):
    questions = get_questions([tag], page=page)
    df = data_to_json(f'data/json/questions_{tag}_{page}.json', questions)

    ids = df['question_id'].tolist()
    answers = get_answers(ids, page=page)
    df = data_to_json(f'data/json/answers_{tag}_{page}.json', {'items': answers})

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
