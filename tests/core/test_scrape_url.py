from pytest import raises
from requests import JSONDecodeError

from sprout.core.scrape_url import scrape_url


def test_returns_dict_with_expected_content_when_url_contains_json():
    url = "https://datapackage.org/profiles/2.0/datapackage.json"
    url_content = scrape_url(url)

    expected_keys = [
        "$schema",
        "title",
        "description",
        "type",
        "required",
        "properties",
    ]
    expected_content_excerpt = (
        "'$schema': 'http://json-schema.org/draft-07/schema#', "
        "'title': 'Data Package', "
        "'description': 'Data Package', "
        "'type': 'object', "
        "'required': ['resources'], "
    )

    assert isinstance(url_content, dict)
    assert expected_keys == list(url_content.keys())
    assert expected_content_excerpt in str(url_content)


def test_raises_error_when_url_does_not_contain_json():
    url = "https://sprout.seedcase-project.org/"
    with raises(
        JSONDecodeError,
    ):
        scrape_url(url)
