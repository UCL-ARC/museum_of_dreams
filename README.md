# Museum of Dreams Project - Website

![Static Badge](https://img.shields.io/badge/built_with-Django_4.2-blue) ![Static Badge](https://img.shields.io/badge/OpenProps-1883e3) ![Static Badge](https://img.shields.io/badge/CKEditor4-8a2be2) ![Static Badge](https://img.shields.io/badge/hosted-232F3E?logo=amazonwebservices)

The production website is hosted at http://museumofdreamworlds.eu-west-2.elasticbeanstalk.com/ and built from the `main` branch

The staging one is http://museumofdreams.eu-west-2.elasticbeanstalk.com/ and is built from the `development` branch

The offical versions are https://museumofdreamworlds.org and https://staging.museumofdreamworlds.org

Development should be done locally and pushed to the staging website where researchers can test features and sign off on them before putting the code on production.

## [See our documentation & help guide](docs/table-of-contents.md)

## Getting Started

To work on this project as is, clone the repo into an appropriate folder (eg. `museum_of_dreams_project`). Create a venv at the top level and start it. Then install the requirements and launch the app. We use `requirements-base.txt` as AWS looks for `requirements.txt` and we don't need to install MySQL locally (we use a local sqlite db).

```
python venv modvenv
source modvenv/bin/activate

pip install -r requirements-base.txt
python manage.py runserver
```

If it's your first time initialising the app on your machine, you may need to run migrations and create a superuser

```
python manage.py migrate
python manage.py createsuperuser
```

To populate the db with data, run

```
python manage.py loaddata path/to/dump/file
```

### AWS

This project is hosted on AWS, if you do not have access to the account, let [Amanda Ho-Lyn](mailto:a.ho-lyn@ucl.ac.uk) know and she will arrange this.
You may find it beneficial to read through the [the documentation](docs/table-of-contents.md) to gain an understanding of the architecture of the project. Also have a look at the [development SOP](docs/developmentSOP.md) for an idea of the general development flow.

### Running tests

Running tests is not advised on AWS as you should only push to the respective branches when you've finished testing locally.
To run the tests locally, run

```
python manage.py test mod_app/tests
```

### Technologies used

This project uses a number of technologies, including:

- [Django 4.2](https://docs.djangoproject.com/en/4.2/)
- [OpenProps](https://open-props.style/#colors) (CSS variable package)
- [CK Editor 4](https://ckeditor.com/docs/ckeditor4/latest/index.html)
- [Fuse.js](https://www.fusejs.io/)
- [AWS](aws.com)

Others which have tangentially helped with development:

- Hypothesis
- Figma

---
