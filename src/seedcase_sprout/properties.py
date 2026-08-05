"""This module includes the dataclasses for the properties of a data package.

The properties are based on the Frictionless Data Package specification. They
are used as input for creating and editing the properties of data packages and
data resources and are intended to help users with the correct structure and
content of the properties.
"""
# NOTE: This content is modified from the auto-generated
# `generate_properties/generated_properties.py` file. Update the auto-generated
# properties file to add more dataclasses and move them into this file.

from abc import ABC
from dataclasses import asdict, dataclass
from typing import Any, Literal, Self
from uuid import uuid4

from dacite import Config, from_dict

from seedcase_sprout.internals import (
    _create_resource_data_path,
    _get_iso_timestamp,
    _to_camel_case,
)
from seedcase_sprout.sprout_checks.is_resource_name_correct import (
    _is_resource_name_correct,
)


@dataclass
class BaseProperties(ABC):
    """Base class for all `*Properties` classes."""

    @property
    def compact_dict(self) -> dict[str, Any]:
        """Converts a `*Properties` object to a `camelCase` dictionary.

        Applies recursively to nested `*Properties` objects. Also removes any
        keys with None values.

        Returns:
            A dictionary representation of the `*Properties` object with only
            non-None
                values.
        """
        return asdict(
            obj=self,
            dict_factory=lambda tuples: {  # type: ignore # typechecker can't determine output of lambda
                _to_camel_case(key): value for key, value in tuples if value is not None
            },
        )

    @classmethod
    def from_dict(cls: type[Self], data: dict[str, Any]) -> Self:
        """Creates a `*Properties` object with data from a dictionary.

        Args:
            cls: The class to create the `*Properties` object from.
            data: The data to fill the `*Properties` object with.

        Returns:
            A `*Properties` object with the properties from the dictionary.
        """
        return from_dict(
            data_class=cls,
            data=data,  # type: ignore[arg-type] # TODO: Not sure how to set type correctly from dacite.
            config=Config(
                # Expect keys in the input to be in camel case
                convert_key=_to_camel_case,
            ),
        )


@dataclass
class ContributorProperties(BaseProperties):
    """The people or organizations who contributed to this data package.

    Creates a dataclass object with all the necessary properties for a
    contributor. This would be given in the `contributors` field of a
    `SproutProperties` object.

    Attributes:
        title: The name of the contributor.
        path: A fully qualified URL pointing to a relevant location online for
            the contributor.
        email: An email address.
        given_name: The name a person has been given, if the contributor is a
            person.
        family_name: The familial name that a person inherits, if the
            contributor is a person.
        organization: An organizational affiliation for this contributor.
        roles: An array of strings describing the roles of the contributor.

    Examples:
        ```{python}
        import seedcase_sprout as sp
        print(sp.ContributorProperties())
        print(sp.ContributorProperties(title="Amir Smith"))
        ```
    """

    title: str | None = None
    path: str | None = None
    email: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    organization: str | None = None
    roles: list[str] | None = None


@dataclass
class LicenseProperties(BaseProperties):
    """The license(s) under which the package or resource is provided.

    Creates a dataclass object with all the necessary properties for a license,
    so that it can be added to the `licenses` field of a `SproutProperties`
    object.

    Attributes:
        name: Must be an Open Definition license identifier, see
            http://licenses.opendefinition.org/
        path: A fully qualified URL, or a POSIX file path.
        title: A human-readable title.

    Examples:
        ```{python}
        import seedcase_sprout as sp
        print(sp.LicenseProperties())
        ```
    """

    name: str | None = None
    path: str | None = None
    title: str | None = None


@dataclass
class SourceProperties(BaseProperties):
    """The raw sources for this data package.

    Attributes:
        title: The title of the source (e.g. document or organization).
        path: A fully qualified URL, or a POSIX file path.
        email: An email address.
        version: The version of the source.
    """

    title: str | None = None
    path: str | None = None
    email: str | None = None
    version: str | None = None


@dataclass
class ReferenceProperties(BaseProperties):
    """The destination part of a foreign key.

    Attributes:
        resource: The name of the resource within the current data package
            where the `fields` are located.
        fields: An array of strings of the same length as
            `TableSchemaForeignKeyProperties.fields`, specifying the field (or
            fields) that form the destination part of the foreign key.
    """

    resource: str | None = None
    fields: list[str] | None = None


@dataclass
class TableSchemaForeignKeyProperties(BaseProperties):
    """A foreign key in a table schema.

    A foreign key is a reference where values in a field (or fields) on the
    table ("resource" in data package terminology) described by the table
    schema connect to values in a field (or fields) on this or a separate table
    (resource).

    Attributes:
        fields: An array of strings specifying the field (or fields) on this
            resource that form the source part of the foreign key.
        reference: An object specifying the destination part of the foreign
            key.
    """

    fields: list[str] | None = None
    reference: ReferenceProperties | None = None


# Allowed types for a field in a table schema.
FieldType = Literal[
    "string",
    "number",
    "integer",
    "boolean",
    "object",
    "array",
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
class ConstraintsProperties(BaseProperties):
    """A dataclass that expresses constraints for validating field values.

    A constraint is a rule that dictates the given values, or range of values,
    that a variable or column can have in a dataset. For instance, a constraint
    for an "age" column could be that it must be greater than 0 but less than
    120.

    Attributes:
        required: Indicates whether a property must have a value for each
            instance.
        unique: When `true`, each value for the property must be unique.
        pattern: A regular expression pattern to test each value of the
            property against, where a truthy response indicates validity.
        enum: The value of the field must exactly match one of the values in
            the `enum` array.
        min_length: An integer that specifies the minimum length of a value.
        max_length: An integer that specifies the maximum length of a value.
        minimum: Specifies a minimum value for a field.
        maximum: Specifies a maximum value for a field.
        exclusive_minimum: Specifies an exclusive minimum value for a field.
        exclusive_maximum: Specifies an exclusive maximum value for a field.
        json_schema: A valid JSON schema object to validate field values. If a
            field value conforms to the provided JSON schema then this field
            value is valid.
    """

    required: bool | None = None
    unique: bool | None = None
    pattern: str | None = None
    enum: list[Any] | None = None
    min_length: int | None = None
    max_length: int | None = None
    minimum: str | float | int | None = None
    maximum: str | float | int | None = None
    exclusive_minimum: str | float | int | None = None
    exclusive_maximum: str | float | int | None = None
    json_schema: dict[str, Any] | None = None


@dataclass
class FieldProperties(BaseProperties):
    """A field in a table schema.

    Provides human-readable documentation as well as additional information
    that can be used to validate the field or create a user interface for data
    entry.

    Attributes:
        name: A name for this field. Must be unique amongst other field names
            in this table schema.
        title: A human readable label or title for this field.
        type: The data type of this field.
        format: The format for this field.
        description: A text description for this field.
        example: An example value for this field.
        constraints: The constraints applicable to this field.
        categories: A finite set of possible values for this field.
        categories_ordered: Specifies whether the order of appearance of the
            values in the `categories` property should be regarded as their
            natural order.
    """

    name: str | None = None
    title: str | None = None
    type: FieldType | None = None
    format: str | None = None
    description: str | None = None
    example: str | None = None
    constraints: ConstraintsProperties | None = None
    categories: list[str] | list[int] | None = None
    categories_ordered: bool | None = None


# Allowed strategies for matching fields in the table schema to fields the data source.
FieldsMatchType = Literal["exact", "equal", "subset", "superset", "partial"]


@dataclass
class TableSchemaProperties(BaseProperties):
    """A table schema for a data resource.

    Table schema is a simple language- and implementation-agnostic way to
    declare a schema for tabular data. Table schema is well suited for use
    cases around handling and validating tabular data in text formats such as
    CSV, but its utility extends well beyond this core usage, towards a range
    of applications where data benefits from a portable schema format.

    Attributes:
        fields: Specifies the fields in this table schema.
        fields_match: Specifies how fields in the table schema match the fields
            in the data source.
        primary_key: A primary key is a field name or an array of field names,
            whose values must uniquely identify each row in the table.
        unique_keys: A field or a set of fields that are required to have
            unique logical values in each row in the table.
        foreign_keys: A reference where values in a field (or fields) on the
            table (resource) described by this table schema connect to values
            in a field (or fields) on this or a separate table (resource).

    Examples:
        ```{python}
        import seedcase_sprout as sp
        print(sp.TableSchemaProperties(primary_key="id"))
        ```
    """

    fields: list[FieldProperties] | None = None
    fields_match: list[FieldsMatchType] | None = None
    primary_key: list[str] | str | None = None
    unique_keys: list[list[str]] | None = None
    foreign_keys: list[TableSchemaForeignKeyProperties] | None = None


@dataclass
class ResourceProperties(BaseProperties):
    """A data resource.

    A simple format to describe and package a single data resource such as an
    individual table or file. The essence of a data resource is a locator for
    the data it describes. A range of other properties can be declared to
    provide a richer set of metadata.

    Creates a dataclass object with all the necessary properties for a
    resource, which would be given in the `resources` field of a
    `SproutProperties` dataclass.

    Attributes:
        name: A simple name or identifier to be used for this resource. Should
            consist only of lowercase English alphanumeric characters plus
            characters in `.-_`.
        path: A path pointing to the data for this resource.
        type: Specifies the type of the resource.
        title: A human-readable title.
        description: A text description. Markdown is encouraged.
        sources: The raw sources for this resource.
        licenses: The license(s) under which the resource is published.
        format: The file format of this resource. Expected to be the standard
            file extension.
        mediatype: The media type of this resource. Can be any valid media type
            listed with
            [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml).
        encoding: The file encoding of this resource.
        bytes: The size of this resource in bytes.
        hash: The MD5 hash of this resource. Indicate other hashing algorithms
            with the {algorithm}:{hash} format.
        schema: A table schema for the resource data, compliant with the table
            schema specification.

    Examples:
        ```{python}
        import seedcase_sprout as sp
        print(sp.ResourceProperties())
        print(sp.ResourceProperties(name="blood-samples", title="Blood samples"))
        ```
    """

    name: str | None = None
    path: str | None = None
    type: Literal["table"] | None = None
    title: str | None = None
    description: str | None = None
    sources: list[SourceProperties] | None = None
    licenses: list[LicenseProperties] | None = None
    format: str | None = None
    mediatype: str | None = None
    encoding: str | None = None
    bytes: int | None = None
    hash: str | None = None
    schema: TableSchemaProperties | None = None

    def __post_init__(self) -> None:
        """Generates the path from the resource name after object creation."""
        self.path = (
            _create_resource_data_path(str(self.name))
            if _is_resource_name_correct(self.name)
            else None
        )


@dataclass
class SproutProperties(BaseProperties):
    """Properties for a data package.

    A simple container format for describing a coherent collection of data in a
    single "package". It provides the basis for convenient delivery,
    installation and management of datasets.

    Creates a dataclass object with all the necessary properties for the
    package.

    Attributes:
        name: A simple name or identifier to be used for this package. Should
            consist only of lowercase English alphanumeric characters plus
            characters in `.-_`.
        id: The unique identifier of this package.
        title: A human-readable title.
        description: A text description. Markdown is encouraged.
        homepage: The home on the web that is related to this package.
        version: A version string identifying the version of this package.
        created: The datetime on which this package was created.
        contributors: The people or organizations who contributed to this
            package.
        keywords: A list of keywords that describe this package.
        image: An image to represent this package.
        licenses: The license(s) under which this package is published.
        resources: Specifies the data resources in this data package, each
            compliant with the data resource specification.
        sources: The raw sources for this data package.

    Examples:
        ```{python}
        import seedcase_sprout as sp
        print(sp.SproutProperties())
        print(sp.SproutProperties(name="diabetes-cohort", title="Diabetes Cohort"))
        print(sp.SproutProperties(licenses=[sp.LicenseProperties(name="ODC-BY-1.0")]))

        # To allow multiline strings, use dedent.
        from textwrap import dedent
        print(sp.SproutProperties(
            title="Birds of North America",
            description=dedent('''
                # Markdown header

                A dataset of bird sightings. With some **bolding**.
                '''
            )
        ))
        ```
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

    @classmethod
    def from_default(
        cls,
        *,
        name: str | None = None,
        id: str | None = None,
        title: str | None = None,
        description: str | None = None,
        homepage: str | None = None,
        version: str | None = None,
        created: str | None = None,
        contributors: list[ContributorProperties] | None = None,
        keywords: list[str] | None = None,
        image: str | None = None,
        licenses: list[LicenseProperties] | None = None,
        resources: list[ResourceProperties] | None = None,
        sources: list[SourceProperties] | None = None,
    ) -> Self:
        """Creates a `SproutProperties` dataclass with default values.

        Default values (`id`, `version`, and `created`) can be overridden and
        unset values can be set using keyword arguments.

        Args:
            name: A simple name or identifier to be used for this package.
                Should consist only of lowercase English alphanumeric
                characters plus characters in `.-_`.
            id: The unique identifier of this package.
            title: A human-readable title.
            description: A text description. Markdown is encouraged.
            homepage: The home on the web that is related to this package.
            version: A version string identifying the version of this package.
            created: The datetime on which this package was created.
            contributors: The people or organizations who contributed to this
                package.
            keywords: A list of keywords that describe this package.
            image: An image to represent this package.
            licenses: The license(s) under which this package is published.
            resources: Specifies the data resources in this data package, each
                compliant with the data resource specification.
            sources: The raw sources for this data package.

        Returns:
            A `SproutProperties` dataclass with default values.

        Examples:
            ```{python}
            import seedcase_sprout as sp

            sp.SproutProperties.from_default(name="my-package", title="My Package...")
            ```
        """
        return cls(
            name=name,
            id=id or str(uuid4()),
            title=title,
            description=description,
            homepage=homepage,
            version=version or "0.1.0",
            created=created or _get_iso_timestamp(),
            contributors=contributors,
            keywords=keywords,
            image=image,
            licenses=licenses,
            resources=resources,
            sources=sources,
        )
