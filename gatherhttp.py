"""
Low level gather.town HTTP api calls.
"""
import json
import urllib.parse
from typing import Any, Dict, List

import requests as requests


def create_room(api_key: str, name: str, source_space: str, reason: str = '') -> str:
    """
    Create a new space, per their documentation, should be `create_space`.
    :param api_key: Your api key
    :param name: Name of the space you want to create
    :param source_space: the id of the space to copy maps from
    :param reason: (optional) this only matters because some features are restricted by use case
    :return: path of the newly created space, append to `https://gather.town/` to get linkable URL
    """
    raise NotImplementedError


def create_space(api_key: str, name: str, source_space: str, reason: str = '') -> str:
    """
    Same as `create_room`, per their docs, this is what the call should be named.
    :param api_key:
    :param name:
    :param source_space:
    :param reason:
    :return:
    """
    return create_room(api_key, name, source_space, reason)


def get_map(api_key: str, space_id: str, map_id: str) -> Dict[str, Any]:
    """
    Gets the contents of a map.
    :param api_key: your api key
    :param space_id: id of space for the map you want to retrieve
    :param map_id: id of map within the space
    :return: undocumented dictionary with map contents. Ask on the forum for questions
    """
    response = requests.get(url=_create_url('getMap'), params=_get_map_params(api_key, space_id, map_id))
    assert response.status_code == 200
    return json.loads(response.content)


def get_map_v2(api_key: str, space_id: str, map_id: str) -> Dict[str, Any]:
    response = requests.get(url=_create_url_v2('getMap', space_id), json=_get_map_params(api_key, space_id, map_id))
    assert response.status_code == 200
    return json.loads(response.content)


def set_map_v1(api_key: str, space_id: str, map_id: str, map_content: str) -> None:
    raise NotImplementedError


def set_map_v2(api_key: str, space_id: str, map_id: str, map_contents: str) -> None:
    raise NotImplementedError


def get_email_guestlist(api_key: str, space_id: str) -> List[str]:
    raise NotImplementedError


def set_email_guestlist(api_key: str, space_id: str, guest_list: Dict[str, Dict[str, str]]) -> None:
    raise NotImplementedError


def _get_map_params(api_key: str, space_id: str, map_id: str) -> Dict[str, str]:
    return {'apiKey': api_key, 'spaceId': space_id.replace('/','\\'), 'mapId': map_id}


def _create_url_v2(action: str, space_id: str) -> str:
    return f"https://gather.town/api/v2/spaces/{urllib.parse.quote(space_id)}/{action}"


def _create_url(action: str) -> str:
    return f"https://gather.town/api/{action}"
