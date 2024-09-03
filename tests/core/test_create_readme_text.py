import json

from sprout.core.create_readme_text import create_readme_text


def test_create_readme_text_with_valid_json():
    # Arrange
    json_string = '{"name": "My Package", "version": "1.0.0", "description": "Sample"}'
    json_object = json.loads(json_string)

    # Act
    result = create_readme_text(json_object)

    expected_output = (
        "This is the README file for the package.\n\n"
        "{\n"
        '    "name": "My Package",\n'
        '    "version": "1.0.0",\n'
        '    "description": "Sample"\n'
        "}"
    )

    # Assert
    assert result == expected_output
