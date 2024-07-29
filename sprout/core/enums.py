from enum import Enum


class DataType(Enum):
	ANY = ("any", "Any")
	ARRAY = ("array", "Array")
	BOOLEAN = ("boolean", "Boolean")
	DATE = ("date", "Date")
	DATE_YEAR = ("date_year", "Year")
	DATETIME = ("datetime", "Datetime")
	DURATION = ("duration", "Duration")
	GEOJSON = ("geojson", "Geojson")
	GEOPOINT = ("geopoint", "Geopoint")
	INTEGER = ("integer", "Integer")
	NUMBER = ("number", "Number")
	OBJECT = ("object", "Object")
	STRING = ("string", "String")
	TIME = ("time", "Time")
	YEAR = ("year", "Year")
	YEAR_MONTH = ("yearmonth", "Month in Year")

	@property
	def value(self) -> str:
		return self._value_[0]

	@property
	def display_name(self) -> str:
		return self._value_[1] 

	@classmethod
	def all(cls) -> "list[tuple[str, str]]":
		return [(data_type.value, data_type.display_name) for data_type in cls]
	
	@classmethod
	def get_display_name(cls, value: str) -> str:
		for data_type in cls:
			if data_type.value == value:
				return data_type.display_name
		raise ValueError(f"No DataType with value {value}")
