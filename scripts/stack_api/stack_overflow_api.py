
import os
import requests
import logging
from urllib.parse import urljoin
class StackOverflowAPI:
  """Fetch data from the Stack Overflow API"""

  def __init__(self):
    self.site = 'stackoverflow'
    self.api_key = ''
    self.base_url = 'https://api.stackexchange.com/2.3/'
    logging.basicConfig(level=logging.INFO)

  def fetch_questions(self, params):
    params['filter'] = '!6WPIomnm)E*eI' # include body and comment count for questions, filter differs by query
    return self.__fetch_data('questions', params)

  def fetch_answers(self, question_ids, params):
    a_params = params.copy()
    a_params['filter'] = '!6WPIomqomPQfa'
    del a_params['tagged']
    return self.__split_and_fetch(question_ids, 'questions', 'answers', a_params)

  def fetch_comments(self, post_ids, post_type, params):
    c_params = params.copy()
    c_params['filter'] = '!nNPvSN_ZTx'
    del c_params['tagged']
    return self.__split_and_fetch(post_ids, post_type, 'comments', c_params)

  def __split_and_fetch(self, ids, data_type, endpoint, params):
    chunked_ids = [ids[i:i + 20] for i in range(0, len(ids), 20)]
    all_responses = []
    for chunk in chunked_ids:
        has_more = True
        params['page'] = 1
        formatted_ids = ';'.join(map(str, chunk))
        while has_more:
            response = self.__fetch_data(f'{data_type}/{formatted_ids}/{endpoint}', params)
            if response:
                all_responses.extend(response.get('items', []))
                has_more = response.get('has_more', False)
                params['page'] += 1
    return all_responses

  def __fetch_data(self, data_type, params):
    params['site'] = self.site

    if self.api_key:
      params['key'] = self.api_key

    url = urljoin(self.base_url, data_type)

    response = requests.get(url, params=params)

    if response.status_code == 200:
      data = response.json()
      logging.info(f"Quota remaining: {data.get('quota_remaining', 'N/A')}")
      return data
    else:
      logging.error(f'Failed to fetch data: {response.status_code}, {response.text}')
      return None
