from dataclasses import dataclass
from datetime import datetime
from dateutil.tz import tzutc
from typing import Dict, Any


@dataclass
class Subreddit:
    id: str
    display_name: str
    display_name_prefixed: str
    name: str
    title: str
    public_description: str
    description: str
    subreddit_type: str
    subscribers: int
    created_utc: datetime
    accounts_active: str
    url: str
    icon_img: str
    banner_img: str
    over18: bool

    @staticmethod
    def from_dict(response: Dict[str, Any]) -> "Subreddit":
        return Subreddit(
            id=response["data"]["id"],
            display_name=response["data"]["display_name"],
            display_name_prefixed=response["data"]["display_name_prefixed"],
            name=response["data"]["name"],
            title=response["data"]["title"],
            public_description=response["data"]["public_description"],
            description=response["data"]["description"],
            subreddit_type=response["data"]["subreddit_type"],
            subscribers=response["data"]["subscribers"],
            created_utc=datetime.fromtimestamp(
                response["data"]["created_utc"], tz=tzutc()
            ),
            accounts_active=response["data"]["accounts_active"],
            url=response["data"]["url"],
            icon_img=response["data"]["icon_img"],
            banner_img=response["data"]["banner_img"],
            over18=response["data"]["over18"],
        )
