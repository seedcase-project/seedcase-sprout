from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Source:
    """Class representing the raw data sources for a package or resource."""

    title: str = ""
    path: str = ""
    email: str = ""
    version: str = ""


@dataclass
class Resource:
    """Class representing a Sprout data resource."""

    id: str = ""
    name: str = ""
    path: str = ""
    type: str = "table"
    title: str = ""
    description: str = ""
    homepage: str = ""
    sources: list[Source] = field(default_factory=list)
    format: str = "csv"
    mediatype: str = "text/csv"
    encoding: str = "utf-8"
    # TODO: add more properties and decide how to deal with hierarchy under 'schema'


@dataclass
class Contributor:
    """Class representing a contributor to a package."""

    title: str = ""
    path: str = ""
    email: str = ""
    givenName: str = ""
    familyName: str = ""
    organization: str = ""
    roles: list[str] = field(default_factory=list)


@dataclass
class License:
    """Class representing the license under which a package is published."""

    name: str = ""
    path: str = ""
    title: str = ""


@dataclass
class Package:
    """Class representing a Sprout data package."""

    id: str = ""
    name: str = ""
    title: str = ""
    description: str = ""
    homepage: str = ""
    version: str = "0.1.0"
    created: str = field(
        default_factory=lambda: datetime.now()
        .astimezone()
        .isoformat(timespec="seconds")
    )
    contributors: list[Contributor] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    image: str = ""
    licenses: list[License] = field(default_factory=list)
    resources: list[Resource] = field(default_factory=lambda: [Resource()])
    sources: list[Source] = field(default_factory=list)
