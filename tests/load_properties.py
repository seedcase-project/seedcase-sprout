from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from seedcase_sprout.properties import BaseProperties


def load_properties(path: Path, object_name: str) -> BaseProperties:
    """Loads a `BaseProperties` object from file."""
    spec = spec_from_file_location("test_module", path)
    assert spec
    assert spec.loader
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    properties: BaseProperties = getattr(module, object_name)
    return properties
