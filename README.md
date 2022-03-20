# Rental Test Task

## Installation

This project uses poetry, a virtual environment manager for Python. To install, use `poetry install`.

Next clone `rental_test_task/local_settings.py.example` as `rental_test_task/local_settings.py` and configure the settings within how you like.

Then migrate the database using `poetry run python manage.py migrate`.

Now you can create a super user and enter some test data into the database through the admin interface. Then you can also navigate to `<BASEURL>/reservations/` and find the table of reservations.

## Tests

Tests use factory-boy for simulating models and making it much easier to create new rows.

Once everything has been installed, you can also run `poetry run pytest` to run the test suite.
