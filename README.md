# Seedcase Sprout: Grow your data in a structured and healthy way

Sprout is a component of the Seedcase ecosystem that aims to take data created or collected for research studies and "grow" it in a structured way using modern best practices for storing data.

Sprout is the backbone of the Seedcase family, this is where data is uploaded, described and stored based on a relational database design. Sprout is also the application which contains the user administration part of Seedcase (although this may change at a later date) sitting it its own set of tables.

Seedcase Sprout is designed to receive data files and guide the user through adding meta data to the research data that the user of Seedcase would like to store in a responsible way.

Check out our [app](https://seedcase-sprout.fly.dev/) where you can upload a csv file with data and experience how to add metadata.

## Installation

This project uses Poetry to manage dependencies. To install Poetry, run:

```
pipx install poetry
```

To run any Python commands within this project, always append the command with `poetry run`, for instance:

```
poetry run python manage.py runserver
```

Or with the justfile:

```
just start-app
```

... which will run the Django project locally.

### Running the application with docker

You can run the Django application with docker:

```
# Run application
docker compose up -d

Check "http://localhost:8000"

# Terminate application
docker compose down
```

Or with the `justfile`:

```
just start-docker
just stop-docker
```
