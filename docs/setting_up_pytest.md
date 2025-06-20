# Setting up pytest

## Installing dependencies

```bash
pip install -r requirements-dev.txt
```

### Note:

`pytest-subtests` helps to identify and separate individual assertions raised in subtests, whereas these assertions would go unnoticed with only`pytest`

## Running tests

```bash
pytest
pytest -s # returns print statements from tests
```

## Configuring pytest

When testing locally, you may need to set a `DJANGO_SETTINGS_MODULE` in your environment variable for collecting tests with `pytest`.

To do this, create a `.env` file at project root and set your `DJANGO_SETTINGS_MODULE`:

```bash
# within your .env file

DJANGO_SETTINGS_MODULE = "museum_of_dreams_project.settings.local"
```
