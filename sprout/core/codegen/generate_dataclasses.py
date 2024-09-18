import subprocess
from pathlib import Path

from sprout.core.fetch_json_from_url import fetch_json_from_url
from sprout.core.write_json import write_json

SCHEMA_URL = "https://datapackage.org/profiles/2.0/datapackage.json"
CODEGEN = Path("sprout", "core", "codegen")
SCHEMA_PATH = CODEGEN / "schema.json"
OUTPUT_PATH = CODEGEN / "generated_properties.py"
CUSTOM_TEMPLATE_DIR = CODEGEN
CUSTOM_FORMATTERS_MODULE = f"{".".join(CODEGEN.parts)}.custom_formatters"


def run_codegen():
    """Uses datamodel-codegen to extract dataclasses from the specified JSON schema.

    The output is post-processed using custom templating and a custom formatter.
    """
    subprocess.run([
        "datamodel-codegen",
        "--input", SCHEMA_PATH,
        "--input-file-type", "jsonschema",
        "--output", OUTPUT_PATH,
        "--output-model-type", "dataclasses.dataclass",
        "--custom-template-dir", CUSTOM_TEMPLATE_DIR,
        "--custom-formatters", CUSTOM_FORMATTERS_MODULE,
        "--custom-file-header", "# ruff: noqa",
        "--enum-field-as-literal", "all",
        "--use-one-literal-as-default",
        "--use-standard-collections",
        "--use-title-as-name",
        "--use-union-operator",
        "--snake-case-field",
        "--special-field-name-prefix", "ignore",
        "--use-field-description",
        "--use-schema-description",
        "--use-double-quotes",
        "--reuse-model",
        "--force-optional",
        "--target-python-version", "3.12"
    ], check=True)


def main():
    """Downloads, preprocesses and extracts dataclasses from the Data Package schema."""
    try:
        schema = fetch_json_from_url(SCHEMA_URL)

        # edit the schema to simplify the generated class structure
        resource_items = schema["properties"]["resources"]["items"]
        del resource_items["oneOf"][0]
        table_schema_properties = resource_items["properties"]["schema"]["properties"]
        del table_schema_properties["fields"]
        table_schema_fkey_items = table_schema_properties["foreignKeys"]["items"]
        table_schema_fkey_items["properties"] = (
            table_schema_fkey_items["oneOf"][0]["properties"]
        )
        del table_schema_fkey_items["oneOf"]

        write_json(schema, SCHEMA_PATH)

        run_codegen()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        SCHEMA_PATH.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
