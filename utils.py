import re
from typing import Optional, List, Any, Dict, Callable


def filter_query(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: List[str]) -> List[str]:
    column_num: int = int(param)
    return list(map(lambda x: x.split(' ')[column_num], data))


def unique_query(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
    return list(set(data))


def sort_query(param: str, data: List[str]) -> List[str]:
    reverse: bool = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: List[str]) -> List[str]:
    limit: int = int(param)
    return list(data)[:limit]


def regexp_filter(param: str, data: List[str]) -> List[str]:
    regexp: re.Pattern = re.compile(param)
    return list(filter(lambda x: re.search(regexp, x), data))
