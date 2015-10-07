# Otter Template - Pipeline

This Otter Template uses `django-compressor` for managing complicated
front-ends that employ SASS, JSX, etc. Once you complete setup you'll
have the React version of ToDoMVC running.

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

### Create a Heroku instance
    $ heroku create

### Configure your instance to use multiple build packs

This template uses `pip` and `npm`. The latter is used to install
`babel` which is used by `django-compressor` to translate `jsx` files to
`js` files. To configure your instance accordingly:

    $ heroku buildpacks:set https://github.com/ddollar/heroku-buildpack-multi.git

### Deploy your application

    $ git push heroku master
    $ heroku run python manage.py migrate

### Set a SECRET_KEY
You'll also need to set a `SECRET_KEY`. You can use
[this tool](http://www.miniwebtool.com/django-secret-key-generator/)
to generate one. Then,

1. Go to heroku.com.
2. Choose your app from the apps list.
3. Click on the "Settings" tab.
4. Click "Reveal config vars" if you haven't previously.
5. Enter a new config var using "SECRET_KEY" as the key, and the random
   string you created earlier as the value.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-pipeline] (https://django-pipeline.readthedocs.org/en/latest/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
