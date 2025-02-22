from reddit_api.utils.factory import Utils, get_utils
from reddit_api.config.factory import Config, get_config

from reddit_api.services.reddit_client import RedditClient


class Services:
    reddit_client: RedditClient

    def __init__(self, config: Config, utils: Utils):
        self.reddit_client = RedditClient(config, utils)


def get_services():
    utils = get_utils()
    config = get_config()

    return Services(config, utils)
