#!/bin/bash
if [ -f /var/app/current/manage.py ]; then
    # Start venv
    cd /var/app
    source venv/staging-LQM1lest/bin/activate
    cd current

    # Run migrations
    python manage.py migrate mod_app 0009
    echo `python manage.py showmigrations`
    python manage.py migrate mod_app 0010a --fake
    python manage.py migrate mod_app 0010b --fake

    echo `python manage.py showmigrations`
    python manage.py migrate
    echo `python manage.py showmigrations`

    # Collect static files
    python manage.py collectstatic --no-input --verbosity 0
else
    echo "manage.py not found."
    exit 1
fi
