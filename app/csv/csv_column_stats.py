from app.csv.type_parser import TypeParser, TYPE_PARSER_HIERARCHY


class CsvColumnStats:
    def __init__(self, name: str, type_parser: TypeParser = TYPE_PARSER_HIERARCHY[0]):
        self.name = name.strip()
        self.parser = type_parser
        self.is_empty_detected = False
        # We start from one because we assume the headers have been read
        self.row_count = 1

    def analyze(self, *values: str) -> str:
        for val in values:
            self.__derive_type(val)
        return self.parser.type_name

    def type(self) -> str:
        return self.parser.type_name

    def __derive_type(self, val: str):
        self.row_count = self.row_count + 1
        if val is None or val == "":
            self.is_empty_detected = True
            return self.parser

        val = val.strip()
        self.__derive_and_set_parser(val)
        return self.parser.type_name

    def __derive_and_set_parser(self, val: str) -> TypeParser:
        current_hierarchy_level = TYPE_PARSER_HIERARCHY.index(self.parser)

        for i in range(current_hierarchy_level, len(TYPE_PARSER_HIERARCHY)):
            parser = TYPE_PARSER_HIERARCHY[i]
            if parser.is_parsable(val):
                self.parser = parser
                return parser
