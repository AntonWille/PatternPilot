
import os
import requests
import logging
from urllib.parse import urljoin

class SORequest:
  def __init__(self, api_key=None):
    self.site = 'stackoverflow'
    self.api_key = api_key or os.getenv('STACK_OVERFLOW_KEY')
    self.base_url = 'https://api.stackexchange.com/2.3/'
    logging.basicConfig(level=logging.INFO)


  def fetch_data(self, data_type, params):
    if not isinstance(params, dict):
      logging.error("Params must be a dictionary.")
      return None

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
