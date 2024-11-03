from typing import Any, Dict, List, Type, TypeVar, Union, overload
from models.subreddit_model import Subreddit
from models.post_model import Post
from models.user_model import User


ModelType = TypeVar("ModelType", Subreddit, Post, User)


@overload
def parse(response: Dict[str, Any], model: Type[ModelType]) -> ModelType: ...


@overload
def parse(
    response: Dict[str, Any], model: Type[ModelType], *, many: bool
) -> List[ModelType]: ...


def parse(
    response: Dict[str, Any], model: Type[ModelType], *, many: bool = False
) -> Union[ModelType, List[ModelType]]:
    """Parse API response into class intance(s)"""

    if not hasattr(model, "from_dict"):
        raise ValueError(f"{model} does not have a from_dict method")

    if many:
        children = response["response"]["children"]
        return [model.from_dict(child) for child in children]

    return model.from_dict(response)