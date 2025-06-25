# Setting up pytest

## Installing dependencies

```bash
pip install -r requirements-dev.txt
```

### Note:

`pytest-subtests` helps to identify and separate individual assertions raised in subtests, whereas these assertions would go unnoticed with `pytest` alone.

## Configuring pytest

When testing locally, you need to set the environment variable `DJANGO_SETTINGS_MODULE`, this enables `pytest` to collect and run tests located within the repository.

To do this, create a `.env` file at project root and set your `DJANGO_SETTINGS_MODULE`:

```bash
# within your .env file

DJANGO_SETTINGS_MODULE = "museum_of_dreams_project.settings.local"
```

We have included a `.env.example` file in the repository root which includes the same setting listed above, you can rename this as `.env` for a quicker setup.

## Running tests

```bash
pytest
pytest -s # returns print statements from tests
```
