# Museum of Dreams Website Project

The production website is hosted at http://museumofdreamworlds.eu-west-2.elasticbeanstalk.com/ and built from the `main` branch

The staging one is http://museumofdreams.eu-west-2.elasticbeanstalk.com/ and is built from the `development` branch

Development should be done locally and staged to the website. At present this is not a production version.

## Getting Started

To work on this project as is, clone the repo into an appropriate folder (eg. `museum_of_dreams_project`). Create a venv at the top level and start it. Then install the requirements and launch the app

```
python3 -m venv modvenv
source modvenv/bin/activate

pip install -r requirements-base.txt
python manage.py runserver
```

If it's your first time initialising the app on your machine, you may need to run migrations and create a superuser

```
python manage.py migrate
python manage.py createsuperuser
```

### Running tests

Running tests is not advised on AWS as you should only push to the respective branches when you've finished testing locally.
To run the tests locally, run

```
python manage.py test mod_app/tests
```

---

### See these other files for recreating the setup etc.

#### [Setting up from scratch](docs/fullSetup.md)

#### [Current AWS Settings](docs/AWScurrentSetup.md)

#### [AWS chatbot](docs/AWSchatbot.md)
