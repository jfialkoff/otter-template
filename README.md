# Otter Template

Otter Template is a base template for Django projects that makes it
super easy to get started on a new Django project. This branch
(`master`) is best for projects that don't have complicated frontends.
For projects with complicated frontends, the `pipeline` branch is
recommended.

## How to Use

To use this project, follow these steps:

1. Set up your virtual environment.
2. Download and unpack the project into your root directory.
3. Run setup (`$ python scripts/otter-setup.py`) and enter the requested
   information.
4. (optional) Remove `scripts/otter-setup.py`. This shouldn't be run
   again.
5. Commit all files to your git repository.
6. Install requirements (`$ pip install -r requirements/dev.txt`)
7. Pin requirements: Run `$ pip freeze` for a full list of requirements
   and versions. Update files in `requirements/` with the installed
   (i.e., most up-to-date) versions.
6. Run your web server (`$ python manage.py runserver`).

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
