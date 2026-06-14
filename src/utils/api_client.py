import requests
from typing import Optional


class APIClient:
    def __init__(self, base_url: str = 'https://jsonplaceholder.typicode.com'):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def get(self, path: str, params: Optional[dict] = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url, params=params)

    def post(self, path: str, json: Optional[dict] = None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.post(url, json=json)

    def delete(self, path: str):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.delete(url)
