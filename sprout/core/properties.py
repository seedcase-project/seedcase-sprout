# NOTE: This content is modified from the auto-generated
# `generate_properties/generated_properties.py` file. Update the auto-generated
# properties file to add more dataclasses and move them into this file.


from dataclasses import dataclass, field
from typing import Any, Literal


@dataclass
class ContributorProperties:
    """The people or organizations who contributed to this Data Package.

    Attributes:
        - title (str | None): The name of the contributor.
        - path (str | None): A fully qualified URL pointing to a relevant
        location online for the contributor.
        - email (str | None): An email address.
        - given_name (str | None): A string containing the name a person has been
        given, if the contributor is a person.
        - family_name (str | None): A string containing the familial name that a person
        inherits, if the contributor is a person.
        - organization (str | None): An organizational affiliation for this
        contributor.
        - roles (list[str] | None): An array of strings describing the roles of the
        contributor.
    """

    title: str | None = None
    path: str | None = None
    email: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    organization: str | None = None
    roles: list[str] | None = None


@dataclass
class LicenseProperties:
    """The license(s) under which the package or resource is provided.

    Attributes:
        - name (str | None): An Open Definition license identifier,
        see http://licenses.opendefinition.org/
        - path (str | None): A fully qualified URL, or a POSIX file path.
        - title (str | None): A human-readable title.
    """

    name: str | None = None
    path: str | None = None
    title: str | None = None


@dataclass
class SourceProperties:
    """The raw sources for this Data Package.

    Attributes:
        - title (str | None): The title of the source (e.g. document or organization).
        - path (str | None): A fully qualified URL, or a POSIX file path.
        - email (str | None): An email address.
        - version (str | None): The version of the source.
    """

    title: str | None = None
    path: str | None = None
    email: str | None = None
    version: str | None = None


@dataclass
class TableDialectProperties:
    r"""Table Dialect describes how tabular data is stored in a file.

    It supports delimited text files like CSV, semi-structured formats like JSON
    and YAML, and spreadsheets like Microsoft Excel.

    Attributes:
        - header (bool | None): Specifies if the file includes a header row,
        always as the first row in the file.
        - header_rows (list[int] | None): Specifies the row numbers for the header.
        - header_join (str | None): Specifies how multiline-header files have to join
        the resulting header rows.
        - comment_rows (list[int] | None): Specifies what rows have to be omitted from
        the data.
        - comment_char (str | None): Specifies that any row beginning with
        this one-character string, without preceding whitespace, causes the
        entire line to be ignored.
        - delimiter (str | None): A character sequence to use as the field
        separator.
        - line_terminator (str | None): Specifies the character sequence that
        must be used to terminate rows.
        - quote_char (str | None): Specifies a character to use for quoting in
        case the `delimiter` needs to be used inside a data cell.
        - double_quote (bool | None): Controls the handling of `quote_char` inside
        data cells. If true, two consecutive quotes are interpreted as one.
        - escape_char (str | None): Specifies a one-character string to use as
        the escape character. Mutually exclusive with `quote_char`.
        - null_sequence (str | None): Specifies the null sequence, for
        example, `\N`.
        - skip_initial_space (bool | None): Specifies the interpretation of
        whitespace immediately following a delimiter. If false, whitespace
        immediately after a delimiter should be treated as part of the
        subsequent field.
        - property (str | None): Specifies where a data array is located in the
        data structure.
        - item_type (Literal['array', 'object'] | None): Specifies whether `property`
        contains an array of arrays or an array of objects.
        - item_keys (list[str] | None): Specifies the keys for extracting rows from
        data arrays where `item_type` is `object`.
        - sheet_number (int | None): Specifies the sheet number of a table in a
        spreadsheet file.
        - sheet_name (str | None): Specifies the sheet name of a table in a spreadsheet
        file.
        - table (str | None): Specifies the name of a table in a database.
    """

    header: bool | None = True
    header_rows: list[int] | None = field(default_factory=lambda: [1])
    header_join: str | None = " "
    comment_rows: list[int] | None = field(default_factory=lambda: [1])
    comment_char: str | None = None
    delimiter: str | None = ","
    line_terminator: str | None = "\r\n"
    quote_char: str | None = '"'
    double_quote: bool | None = True
    escape_char: str | None = None
    null_sequence: str | None = None
    skip_initial_space: bool | None = False
    property: str | None = None
    item_type: Literal["array", "object"] | None = None
    item_keys: list[str] | None = None
    sheet_number: int | None = None
    sheet_name: str | None = None
    table: str | None = None


@dataclass
class ReferenceProperties:
    """The destination part of a foreign key.

    Attributes:
        - resource: (str | None): The name of the resource within the current Data
        Package where the `fields` are located.
        - fields: (list[str] | None): An array of strings of the same length as
        `TableSchemaForeignKeyProperties.fields`, specifying the field (or fields)
        that form the destination part of the foreign key.
    """

    resource: str | None = None
    fields: list[str] | None = None


@dataclass
class TableSchemaForeignKeyProperties:
    """A foreign key in a Table Schema.

    A foreign key is a reference where values in a field (or fields) on the table
    ("resource" in Data Package terminology) described by the Table Schema connect to
    values in a field (or fields) on this or a separate table (resource).

    Attributes:
        - fields (list[str] | None): An array of strings specifying the field (or
        fields) on this resource that form the source part of the foreign key.
        - reference (ReferenceProperties | None): An object specifying the
        destination part of the foreign key.
    """

    fields: list[str] | None = None
    reference: ReferenceProperties | None = None


@dataclass
class MissingValueProperties:
    """Values that, when encountered in the source, should be considered as not present.

    Attributes:
        - value (str | None): String representing the missing value.
        - label (str | None): A human-readable label for the missing value.
    """

    value: str | None = None
    label: str | None = None


# Allowed types for a field in a Table Schema.
FieldType = Literal[
    "string",
    "number",
    "integer",
    "boolean",
    "object",
    "array",
    "list",
    "datetime",
    "date",
    "time",
    "year",
    "yearmonth",
    "duration",
    "geopoint",
    "geojson",
    "any",
]


@dataclass
class ConstraintsProperties:
    """A class that expresses constraints for validating field values.

    Attributes:
        - required (bool | None): Indicates whether a property must have a
        value for each instance.
        - unique (bool | None): When `true`, each value for the property
        must be unique.
        - pattern (str | None): A regular expression pattern to test each
        value of the property against, where a truthy response indicates
        validity.
        - enum (list | None): The value of the field must exactly match one of
        the values in the `enum` array.
        - min_length (int | None): An integer that specifies the minimum
        length of a value.
        - max_length (int | None): An integer that specifies the maximum
        length of a value.
        - minimum (str | float | int | None): Specifies a minimum value for a field.
        - maximum (str | float | int | None): Specifies a maximum value for a field.
        - exclusive_minimum (str | float | int | None): Specifies an exclusive minimum
        value for a field.
        - exclusive_maximum (str | float | int | None): Specifies an exclusive maximum
        value for a field.
        - json_schema (dict[str, Any] | None): A valid JSON Schema object to
        validate field values. If a field value conforms to the provided
        JSON Schema then this field value is valid.
    """

    required: bool | None = None
    unique: bool | None = None
    pattern: str | None = None
    enum: list | None = None
    min_length: int | None = None
    max_length: int | None = None
    minimum: str | float | int | None = None
    maximum: str | float | int | None = None
    exclusive_minimum: str | float | int | None = None
    exclusive_maximum: str | float | int | None = None
    json_schema: dict[str, Any] | None = None


@dataclass
class FieldProperties:
    """A field in a Table Schema.

    Provides human-readable documentation as well as additional information that can
    be used to validate the field or create a user interface for data entry.

    Attributes:
        - name (str | None): A name for this field. Must be unique amongst other field
        names in this Table Schema.
        - title (str | None): A human readable label or title for this field.
        - type (FieldType | None): The data type of this field.
        - format (str | None): The format for this field.
        - description (str | None): A text description for this field.
        - example (str | None): An example value for this field.
        - constraints (ConstraintsProperties | None): The constraints applicable to
        this field.
        - categories (list[str] | list[int] | None): A finite set of possible values
        for this field.
        - categories_ordered (bool | None): Specifies whether the order of appearance
        of the values in the `categories` property should be regarded as their natural
        order.
        - missing_values (list[str] | list[MissingValueProperties] | None): Values that,
        when encountered in the source, should be considered as not present. Takes
        precedence over the schema-level property.
    """

    name: str | None = None
    title: str | None = None
    type: FieldType | None = None
    format: str | None = "default"
    description: str | None = None
    example: str | None = None
    constraints: ConstraintsProperties | None = None
    categories: list[str] | list[int] | None = None
    categories_ordered: bool | None = None
    missing_values: list[str] | list[MissingValueProperties] | None = field(
        default_factory=lambda: [""]
    )


# Allowed strategies for matching fields in the Table Schema to fields the data source.
FieldsMatchType = Literal["exact", "equal", "subset", "superset", "partial"]


@dataclass
class TableSchemaProperties:
    """A Table Schema for a Data Resource.

    Table Schema is a simple language- and implementation-agnostic way to declare a
    schema for tabular data. Table Schema is well suited for use cases around handling
    and validating tabular data in text formats such as CSV, but its utility extends
    well beyond this core usage, towards a range of applications where data benefits
    from a portable schema format.

    Attributes:
        - fields (list[FieldProperties] | None): Specifies the fields in this Table
        Schema.
        - fields_match (FieldsMatchType | None): Specifies how fields in the Table
        Schema match the fields in the data source.
        - primary_key (list[str] | str | None): A primary key is a field name
        or an array of field names, whose values must uniquely identify
        each row in the table.
        - unique_keys (list[list[str]] | None): A field or a set of fields that are
        required to have unique logical values in each row in the table.
        - foreign_keys (list[TableSchemaForeignKeyProperties] | None): A reference where
        values in a field (or fields) on the table (resource) described by this Table
        Schema connect to values in a field (or fields) on this or a separate table
        (resource).
        - missing_values (list[str] | list[MissingValueProperties] | None): Values that,
        when encountered in the source, should be considered as not present.
    """

    fields: list[FieldProperties] | None = None
    fields_match: FieldsMatchType | None = "exact"
    primary_key: list[str] | str | None = None
    unique_keys: list[list[str]] | None = None
    foreign_keys: list[TableSchemaForeignKeyProperties] | None = None
    missing_values: list[str] | list[MissingValueProperties] | None = field(
        default_factory=lambda: [""]
    )


@dataclass
class ResourceProperties:
    """A Data Resource.

    A simple format to describe and package a single data resource such as an
    individual table or file. The essence of a Data Resource is a locator for
    the data it describes. A range of other properties can be declared to provide a
    richer set of metadata.

    Attributes:
        - name (str | None): A simple name or identifier to be used for this resource.
        Should consist only of lowercase English alphanumeric characters plus characters
        in `.-_`.
        - id (str | None): The unique identifier of this resource.
        - path (str | None): A path pointing to the data for this resource.
        - data (Any | None): Inline data for this resource.
        - type (Literal['table'] | None): Specifies the type of the resource.
        - title (str | None): A human-readable title.
        - description (str | None): A text description. Markdown is encouraged.
        - sources (list[SourceProperties] | None): The raw sources for this resource.
        - licenses (list[LicenseProperties] | None): The license(s) under which the
        resource is published.
        - format (str | None): The file format of this resource. Expected to be the
        standard file extension.
        - mediatype (str | None): The media type of this resource. Can be any
        valid media type listed with [IANA]
        (https://www.iana.org/assignments/media-types/media-types.xhtml).
        - encoding (str | None): The file encoding of this resource.
        - bytes (int | None): The size of this resource in bytes.
        - hash (str | None): The MD5 hash of this resource. Indicate other
        hashing algorithms with the {algorithm}:{hash} format.
        - dialect (TableDialectProperties | None): The tabular dialect of the resource
        data.
        - schema (TableSchemaProperties | None): A Table Schema for the resource data,
        compliant with the Table Schema specification.
    """

    name: str | None = None
    id: str | None = None
    path: str | None = None
    data: Any | None = None
    type: Literal["table"] | None = None
    title: str | None = None
    description: str | None = None
    sources: list[SourceProperties] | None = None
    licenses: list[LicenseProperties] | None = None
    format: str | None = None
    mediatype: str | None = None
    encoding: str | None = "utf-8"
    bytes: int | None = None
    hash: str | None = None
    dialect: TableDialectProperties | None = None
    schema: TableSchemaProperties | None = None


@dataclass
class PackageProperties:
    """A Data Package.

    A simple container format for describing a coherent collection of data in a single
    "package". It provides the basis for convenient delivery, installation and
    management of datasets.

    Attributes:
        - name (str | None): A simple name or identifier to be used for this package.
        Should consist only of lowercase English alphanumeric characters plus characters
        in `.-_`.
        - id (str | None): The unique identifier of this package.
        - title (str | None): A human-readable title.
        - description (str | None): A text description. Markdown is encouraged.
        - homepage (str | None): The home on the web that is related to this Data
        Package.
        - version (str | None): A version string identifying the version of the package.
        - created (str | None): The datetime on which this package was created.
        - contributors (list[ContributorProperties] | None): The people or organizations
        who contributed to this Data Package.
        - keywords (list[str] | None): A list of keywords that describe this package.
        - image (str | None): An image to represent this package.
        - licenses (list[LicenseProperties] | None): The license(s) under which this
        package is published.
        - resources (list[ResourceProperties] | None): Specifies the Data Resources
        in this Data Package, each compliant with the Data Resource specification.
        - sources (list[SourceProperties] | None): The raw sources for this Data
        Package.
    """

    name: str | None = None
    id: str | None = None
    title: str | None = None
    description: str | None = None
    homepage: str | None = None
    version: str | None = None
    created: str | None = None
    contributors: list[ContributorProperties] | None = None
    keywords: list[str] | None = None
    image: str | None = None
    licenses: list[LicenseProperties] | None = None
    resources: list[ResourceProperties] | None = None
    sources: list[SourceProperties] | None = None