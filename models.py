from marshmallow import fields, Schema, validates_schema, ValidationError
from utils import *

VALID_CMD_PARAMS: Dict[str, Callable] = {
    "filter": filter_query,
    "sort": sort_query,
    "map": map_query,
    "unique": unique_query,
    "limit": limit_query,
    "regex": regexp_filter,
}

PATH: str = 'data/apache_logs.txt'


def create_query(cmd: str, param: str, data: Optional[List[str]]) -> List[str] | tuple:
    try:
        if data is None:
            with open(PATH, 'r', encoding='utf-8') as f:
                sorted_data: List[str] = list(map(lambda x: x.strip(), f))
        else:
            sorted_data = data

    except FileNotFoundError as e:
        return e, 400

    return VALID_CMD_PARAMS[cmd](param=param, data=sorted_data)


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values['cmd'] not in VALID_CMD_PARAMS.keys():
            raise ValidationError('cmd1 not in valid parameters')
        return values


class ManyRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
