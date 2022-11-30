import time

from envparse import env
import requests

import config


class APIClient:
    """
    No need to do anything too robust
    """

    def __init__(self, email=None, organization=None):
        self.email = email
        if self.email is None:
            self.email = env("PEERLOGIC_USER_EMAIL")

        if env("IS_LOCAL_TEST", None) == "true":
            self._url = "http://localhost:8001"
        else:
            self._url = "http://api:8000"
        self._session = requests.session()
        self._is_logged_in = False

    @property
    def _headers(self):
        if not self._is_logged_in:
            self._login()

        return {"Content-type": "application/json"}

    def _login(self):
        payload = {"email": self.email, "password": "password"}
        response = self._session.request("POST", f"{self._url}/api/login/", json=payload)
        response.raise_for_status()
        self._is_logged_in = True

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def patch(self, path, **kwargs):
        return self.request("PATCH", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)

    def request(self, method, path, **kwargs):
        return self._session.request(method, f"{self._url}{path}", headers=self._headers, **kwargs)

    def raw_request(self, method, path, **kwargs):
        return requests.request(method, f"{self._url}{path}", **kwargs)

    def close_session(self):
        self._session.close()
