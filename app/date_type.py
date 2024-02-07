class DataType:
    """
    Class representing a "sprout" type. A sprout type has a name and a description.
    Furthermore, the DataType contains a mapping to a pandas_type and a python_type.
    This

    Example: Text
        The "Text" is represented like this:
        DateType("Text", "A text string", "str", "object")


    """
    def __init__(self, id: str, name: str, description: str, pandas_type: str, python_type: str):
        self.id = id
        self.name = name
        self.description = description
        self.pandas_type = pandas_type
        self.python_type = python_type


# All DateTypes variables
INT_DT = DataType("INT", "Whole Number", "An int", "int64", "int")
FLOAT_DT = DataType("FLOAT", "Decimal", "A decimal or float", "float64", "float")
TEXT_DT = DataType("TEXT", "Text", "A text", "object", "str")
BOOL_DT = DataType("BOOL", "Yes/No", "Yes or No", "bool", "bool")
TIME_DT = DataType("TIME", "Time", "A time", "deltatime64[ns]", "deltatime")
DATETIME_DT = DataType("DATETIME", "Date+Time", "Date+Time", "datetime64[ns]", "datetime")


# Valid DateTypes in a list
TYPES = [INT_DT, FLOAT_DT, TEXT_DT, BOOL_DT, TIME_DT, DATETIME_DT]

# We need to reference the sprout types in the database. We can do this by using
# something called "choices" in a Django model. It accepts a list of tuples
# Example: [("INT", "Whole Number"), ("FLOAT", "Decimal"), ...]
TYPE_CHOICES = [(t.id, t.name) for t in TYPES]
