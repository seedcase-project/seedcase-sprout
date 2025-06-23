<p align=center>
    <a href="https://sprout.seedcase-project.org/">
        <img src="https://raw.githubusercontent.com/seedcase-project/seedcase-sprout/main/_extensions/seedcase-project/seedcase-theme/logos/navbar-logo-seedcase-sprout.svg" height="150" alt="Link to Sprout website"/>
    </a>
</p>

## seedcase-sprout: Grow structured, organised, and usable data

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/seedcase-project/seedcase-sprout/badge)](https://scorecard.dev/viewer/?uri=github.com/seedcase-project/seedcase-sprout)
[![Build package](https://github.com/seedcase-project/seedcase-sprout/actions/workflows/build-package.yml/badge.svg)](https://github.com/seedcase-project/seedcase-sprout/actions/workflows/build-package.yml)
[![Build documentation](https://github.com/seedcase-project/seedcase-sprout/actions/workflows/build-website.yml/badge.svg)](https://github.com/seedcase-project/seedcase-sprout/actions/workflows/build-website.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/seedcase-project/seedcase-sprout/main.svg)](https://results.pre-commit.ci/latest/github/seedcase-project/seedcase-sprout/main)
[![code coverage](https://raw.githubusercontent.com/seedcase-project/seedcase-sprout/coverage/coverage.svg?raw=true)](https://htmlpreview.github.io/?https://raw.githubusercontent.com/seedcase-project/seedcase-sprout/coverage/index.html)

Sprout is one component of the [Seedcase
Project](https://seedcase-project.org) framework that aims to take data
created or collected for research studies and "grow" it in a structured
way using modern data engineering best practices. Sprout is designed to
organise, describe, and store data for effective discovery, management,
and analysis.

Check out our [website](https://sprout.seedcase-project.org/) for more
information, such as an
[overview](https://sprout.seedcase-project.org/docs/overview/), how to
use it [guide](https://sprout.seedcase-project.org/docs/guide/), or
to read about the
[design](https://sprout.seedcase-project.org/docs/design/). For 
a list of changes, see our
[changelog](https://sprout.seedcase-project.org/docs/releases/) page.

## Install

Seedcase Sprout can be installed in two ways. The first is to install it
as a user, and the second is to install it as a contributor.

To install Sprout for general use, see our [Installation
Guide](https://sprout.seedcase-project.org/docs/guide/installation).

### Installing as a contributor

To install Sprout for development or contribution, you first need to install [uv](https://docs.astral.sh/uv/). We use uv to manage our project, including
dependencies. Their website has a more detailed guide on using uv, but
below are some simple instructions to get you started.

To install uv, run:

``` bash
pipx install uv
```

Then, open a terminal so that the working directory is the root of this
project (`seedcase-sprout/`) and run:

``` bash
just install-deps
```

## Contributing and re-use

If you would like to contribute, please check out our
[guidebook](https://guidebook.seedcase-project.org/) for more specific
details on how we work and develop. It is a regularly evolving document,
so is at various states of completion.

This project is licensed under the [MIT
License](https://github.com/seedcase-project/seedcase-sprout/blob/main/LICENSE.md).

<!-- TODO: Include citation information here after upload to Zenodo -->
