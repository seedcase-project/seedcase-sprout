from seedcase_sprout import (
    ContributorProperties,
    LicenseProperties,
    PackageProperties,
    ResourceProperties,
    as_readme_text,
)


def test_creates_readme():
    """Should be able to create a README for a set of properties."""
    properties = PackageProperties(
        name="diabetes-hypertension-study",
        title="Diabetes and Hypertension Study",
        homepage="www.my-page.com/diabetes-2021",
        id="123-abc-123",
        description="This is my package.",
        version="2.0.0",
        created="2024-05-14T05:00:01+00:00",
        contributors=[
            ContributorProperties(
                title="Jamie Jones",
                email="jamie_jones@example.com",
                path="example.com/jamie_jones",
                roles=["creator"],
            )
        ],
        resources=[
            ResourceProperties(
                title="First Resource", description="This is my first resource."
            ),
            ResourceProperties(
                title="Second Resource", description="This is my second resource."
            ),
        ],
        licenses=[
            LicenseProperties(
                name="ODC-BY-1.0",
                path="https://opendatacommons.org/licenses/by",
                title="Open Data Commons Attribution License 1.0",
            ),
            LicenseProperties(
                name="APL-1.0",
                path="https://opensource.org/license/apl1-0-php",
                title="Adaptive Public License 1.0",
            ),
        ],
    )
    assert as_readme_text(properties)


def test_creates_readme_with_empty_values():
    """Should be able to create a README for an empty set of properties."""
    assert as_readme_text(PackageProperties())
