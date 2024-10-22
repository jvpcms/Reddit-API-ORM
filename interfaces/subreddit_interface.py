import requests
from ..endpoints import Endpoints
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import RedditClient


class SubredditInterface:
    def __init__(self, client: "RedditClient"):
        self.client = client

    def mine(self, where: str = "subscriber"):
        url = Endpoints.subreddits_where_subscirbed
        headers = self.client.default_headers

        response = requests.get(url, headers=headers)
        return response.json()