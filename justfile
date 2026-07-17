@_default:
    just --list --unsorted

# Run all build-related recipes in the justfile
run-all: install-deps update-quarto-theme format-all check-all test-all build-all

# Run all formatters
format-all: format-python format-md format-docstrings

# Run all checks
check-all: check-python check-unused check-security check-spelling check-urls

# Run all tests
test-all: test-python

# Run all builds
build-all: build-contributors build-website build-readme

# List all TODO items in the repository
list-todos:
  grep -R -n \
    --exclude="*.code-snippets" \
    --exclude-dir=.quarto \
    --exclude=justfile \
    --exclude=_site \
    "TODO" *

# Install the pre-commit hooks
install-precommit:
  uvx pre-commit install
  uvx pre-commit autoupdate
  uvx pre-commit run --all-files

# Update the Quarto seedcase-theme extension
update-quarto-theme:
  # Add theme if it doesn't exist, update if it does
  quarto update seedcase-project/seedcase-theme --no-prompt

# Install Python package dependencies
install-deps:
  uv sync --all-extras --dev --upgrade

# Reformat Python code to match coding style and general structure
format-python:
  # Separate fix to format imports
  uvx ruff check --select I --fix
  uvx ruff check --fix
  uvx ruff format

# Reformat Python dostrings
format-docstrings:
  uvx format-docstring \
    --docstring-style google \
    --include-arg-types false \
    --include-arg-defaults false \
    --include-return-and-yield-types false \
    --fix-rst-backticks false \
    src/

# Format Markdown files
format-md:
  # Use both rumdl and panache, for different purposes
  uvx rumdl fmt --silent
  uvx --from panache-cli panache format . --quiet

# Check Python code for any errors that need manual attention
check-python:
  # Check formatting
  uvx ruff check .
  # Check types
  uvx pyrefly check

# Run basic security checks on the package
check-security:
  uvx bandit -r src/

# Check for spelling errors in files
check-spelling:
  uvx typos --config .config/typos.toml

# Check that URLs work
check-urls:
  lychee . \
    --verbose \
    --extensions md,qmd,py \
    --exclude "github\.com" \
    --exclude-path "_badges.qmd"

# Check for unused code in the package and its tests
check-unused:
  # exit code=0: No unused code was found
  # exit code=3: Unused code was found
  # Three confidence values:
  # - 100 %: function/method/class argument, unreachable code
  # - 90 %: import
  # - 60 %: attribute, class, function, method, property, variable
  # There are some things should be ignored though, with the allowlist.
  # Create an allowlist with `vulture --make-allowlist`
  uvx vulture --min-confidence 100 src/ tests/ **/vulture-allowlist.py

# Run the Python tests
test-python:
  uv run pytest
  # Make the badge from the coverage report
  uv run genbadge coverage \
    -i coverage.xml \
    -o htmlcov/coverage.svg

# Build the Python docstrings as a section in the website using quartodoc
build-quartodoc:
  # To let Quarto know where python is.
  export QUARTO_PYTHON=.venv/bin/python3
  # Delete any previously built files from quartodoc.
  # -f is to not give an error if the files don't exist yet.
  rm -rf docs/reference
  uv run quartodoc build

# Build the documentation website using Quarto
build-website: build-quartodoc
  uv run quarto render --execute

# Re-build the README file from the Quarto version
build-readme:
  uvx --from quarto quarto render README.qmd --to gfm

# Generate a Quarto include file with the contributors
build-contributors:
  sh ./tools/get-contributors.sh seedcase-project/seedcase-sprout > docs/includes/_contributors.qmd

# Preview the website with automatic reload on changes
preview-website: build-quartodoc
  uvx --from quarto quarto preview

# Check for and apply updates from the template
update-from-template:
  # Do not update existing source files
  uvx copier update --trust --defaults $(find src/seedcase_sprout -type f -printf "--exclude %p ")

# Reset repo changes to match the template
reset-from-template:
  uvx copier recopy --trust --defaults
