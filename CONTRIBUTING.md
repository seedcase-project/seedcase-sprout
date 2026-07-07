# Contributing

## :bug: Issues and bugs

The easiest way to contribute is to report issues or bugs that you might find
while using Sprout. You can do this by creating a
[new](https://github.com/seedcase-project/seedcase-sprout/issues/new/choose)
issue on our GitHub repository.

## :pencil2: Adding or modifying content

If you would like to contribute content, please check out our
[guidebook](https://guidebook.seedcase-project.org/) for more specific details
on how we work and develop. It is a regularly evolving document, so is at
various states of completion.

To contribute to Sprout, you first need to install
[uv](https://docs.astral.sh/uv/) and
[justfile](https://just.systems/man/en/packages.html). We use uv and justfile to
manage our package, such as to run checks and test the package. Both the uv and
justfile websites have a more detailed guide on using uv, but below are some
simple instructions to get you started.

It's easiest to first [install
uv](https://docs.astral.sh/uv/getting-started/installation/) and then install
justfile and the other tools needed with uv. Once you've installed uv, install
the other tools by running:

```bash
uv tool install rust-just pyrefly ruff
```

We install Ruff and Pyrefly to make these tools available to other tools and to
VS Code.

We keep all our development workflows in the `justfile`, so you can explore it
to see what commands are available. To see a list of commands available, run:

```bash
just
```

As you contribute, make sure your changes will pass our tests by opening a
terminal so that the working directory is the root of this project's repository
and running:

```bash
just run-all
```

When committing changes, please try to follow [Conventional
Commits](https://decisions.seedcase-project.org/why-conventional-commits/) as
Git messages. Using this convention allows us to be able to automatically create
a release based on the commit message by using
[Cocogitto](https://decisions.seedcase-project.org/why-semantic-release-with-cocogitto/).
If you don't use Conventional Commits when making a commit, we will revise the
pull request title to follow that format. That's because we squash merges when
merging pull requests, so all other commits in the pull request will be squashed
into one commit.

## :file_folder: Explanation of files and folders

- `.github/`: Contains GitHub-specific files, such as issue and pull request
  templates, workflows,
  [dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide)
  configuration, pull request templates, and a
  [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
  file.
- `tools/vulture-allowlist.py`: List of variables that shouldn't be flagged by
  [Vulture](https://github.com/jendrikseipp/vulture) as unused.
- `tools/get-contributors.sh`: Script to get list of package contributors.
- `tests/`: Test files for the package.
- `src/`: Source code for the package.
- `docs/`: Documentation about using and developing the Python package.
- `.config/`: Contains configuration files for various tools used in the
  package, such as:
  - `quartodoc.py`: Custom [`quartodoc`](https://machow.github.io/quartodoc/)
    renderer.
  - `ruff.toml`: [Ruff](https://docs.astral.sh/ruff/) configuration file for
    linting and formatting Python code.
  - `rumdl.toml` and `panache.toml`: [rumdl](https://rumdl.dev) and
    [Panache](https://panache.bz) configuration file for formatting Markdown
    files in the project.
  - `cog.toml`: [Cocogitto](https://docs.cocogitto.io) configuration file for
    managing versions.
  - `cliff.toml`: [git-cliff](https://git-cliff.org) configuration file for
    creating the changelog.
- `.copier-answers.yml`: Contains the answers you gave when copying the package
  from the template. **You should not modify this file directly.**
- `.pre-commit-config.yaml`: [Pre-commit](https://pre-commit.com/) configuration
  file for managing and running checks before each commit.
- `.typos.toml`: [typos](https://github.com/crate-ci/typos) spell checker
  configuration file.
- `justfile`: [`just`](https://just.systems/man/en/) configuration file for
  scripting package tasks.
- `.editorconfig`: Editor configuration file for
  [EditorConfig](https://editorconfig.org/) to maintain consistent coding styles
  across different editors and IDEs.
- `CHANGELOG.md`: Changelog file for tracking changes in the package.
- `CITATION.cff`: Structured citation metadata for your package.
- `CONTRIBUTING.md`: Guidelines for contributing to the package.
- `_metadata.yml`: Quarto metadata file for the website, including information
  about the package, such as the titles and GitHub names.
- `_quarto.yml`: Quarto configuration file for the website, including settings
  for the website, such as the theme, navigation, and other options.
- `pyproject.toml`: Main Python package configuration file defining metadata and
  dependencies.
- `uv.lock`: Lockfile used by [`uv`](https://docs.astral.sh/uv/) to record exact
  versions of installed dependencies.
