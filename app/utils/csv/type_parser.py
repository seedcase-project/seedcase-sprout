import datetime
from typing import Callable, Any
import dateutil.parser


class TypeParser:
    def __init__(self,
                 type_name: str,
                 parser_method: Callable[[str], Any]):
        self.type_name = type_name
        self.parse_method = parser_method

    def parse(self, val: str):
        return self.parse_method(val)

    def is_parsable(self, val: str):
        try:
            self.parse(val)
            return True
        except ValueError:
            return False


def parse_date(val: str) -> datetime.date:
    if len(val) < 8:
        # The dateutil parser is too optimistic when parsing strings
        # We need at least 8 numbers: 20240101
        raise ValueError("val is too short to be a date")

    dt = dateutil.parser.parse(val)
    if dt.hour == 0 and dt.minute == 0 and dt.second == 0 and dt.microsecond == 0:
        return dt.date()
    raise ValueError('Not a date')


def parse_time(val: str) -> datetime.time:
    if len(val) < 5:
        raise ValueError("We dont want to try and parse something below 5 char")
    return datetime.time.fromisoformat(val)


def parse_datetime(val: str) -> datetime.datetime:
    if len(val) < 8:
        # the dateutil parser is too optimistic when parsing strings we need at least 8
        raise ValueError("val is too short to be a date")
    return dateutil.parser.parse(val)


def parse_boolean(val: str) -> bool:
    val_lower_case = val.lower()
    if val_lower_case in ['true', 'yes', '1', 'y']:
        return True
    if val_lower_case in ['false', 'no', '0', 'n']:
        return False
    raise ValueError('Not boolean-like string')


TYPE_PARSER_HIERARCHY = [
    TypeParser("bool", parse_boolean),
    TypeParser("int", int),
    TypeParser("float", float),
    TypeParser("time", parse_time),
    TypeParser("date", parse_date),
    TypeParser("datetime", parse_datetime),
    TypeParser("str", lambda s: s)
]
