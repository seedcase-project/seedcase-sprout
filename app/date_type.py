class DataType:
    """
    Class representing a "sprout" type. A sprout type has a name and a description.
    Furthermore, the DataType contains a mapping to a pandas_type and a python_type.
    This

    Example: Text
        The "Text" is represented like this:
        DateType("Text", "A text string", "str", "object")


    """
    def __init__(self, name: str, description: str, pandas_type: str, python_type: str):
        self.name = name
        self.description = description
        self.pandas_type = pandas_type
        self.python_type = python_type

    def get(self, id: str):
        return TYPES[id]

# All the valid sprout types are contained in this dictionary. The keys should never
# change, but we can change all the other fields
TYPES = {
    "INT": DataType("Whole Number", "An int", "int64", "int"),
    "FLOAT": DataType("Decimal", "A decimal or float", "float64", "float"),
    "TEXT": DataType("Text", "A text", "object", "str"),
    "BOOL": DataType("Yes/No", "Yes or No", "bool", "bool"),
    "TIME": DataType("Time", "A time", "deltatime64[ns]", "deltatime"),
    "DATETIME": DataType("Date+Time", "Date+Time", "datetime64[ns]", "datetime"),
}

# We need to reference the sprout types in the database. We can do this by using
# something called "choices" in a Django model. It accepts a list of tuples
# Example: [("INT", "Whole Number"), ("FLOAT", "Decimal"), ...]
TYPE_CHOICES = [(k, v.name) for k, v in TYPES.items()]
