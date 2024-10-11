# Seedcase Sprout: Grow your data in a structured and healthy way

Sprout is a component of the Seedcase framework that aims to take data
created or collected for research studies and "grow" it in a structured
way using modern data engineering best practices.

Sprout is the backbone of the Seedcase family; this is where data is
uploaded, described, and stored.

Seedcase Sprout is designed to receive data files and guide the user
through adding metadata to the research data that the user of Seedcase
would like to store in a responsible way.

## Install

Seedcase Sprout can be installed in two ways. The first is to install it
as a user, and the second is to install it as a contributor.

### Installation for users

To install Seedcase Sprout as a user, you will need to have `pip`, and
`pipenv` installed. Once you've ensured that these are up-to-date, you
can use the following command to install Seedcase Sprout:

``` bash
pip install seedcase_sprout@git+https://github.com/seedcase-project/seedcase-sprout
```

### Installation for contributors

If you would like to contribute to Seedcase Sprout, you should first
read the contribution guidelines in the [CONTRIBUTING]() file. Then
return here to install poetry and clone the repository.

TODO: add link

The Seedcase project uses Poetry to manage dependencies. If you haven't
worked with Poetry before, you will find an excellent introduction to it
in the [Poetry documentation](https://python-poetry.org/docs/). If you
have worked with it before you can find a quick guide to installing it
below.

To install Poetry, run:

``` bash
pipx install poetry
```

To run any Python commands within this project, always append the
command with `poetry run`, for instance:

``` bash
poetry run python manage.py runserver
```

Or with the justfile:

``` bash
just start-app
```

````{=html}
<!-- 
... which will run the Django project locally.

### Running the application with docker

You can run the Django application with docker:

``` bash
# Run application
docker compose up -d

Check "http://localhost:8000"

# Terminate application
docker compose down
```

Or with the `justfile`:

``` bash
just start-docker
just stop-docker
```
 -->
````
