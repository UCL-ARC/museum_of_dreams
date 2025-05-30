#!/bin/bash
if [ -f /var/app/current/manage.py ]; then
    # Start venv
    cd /var/app
    source venv/staging-LQM1lest/bin/activate
    cd current

    # Run migrations
    python manage.py migrate
    echo `date`
    echo `python manage.py showmigrations`

    # Collect static files
    #python manage.py collectstatic --no-input --verbosity 0
else
    echo "manage.py not found."
    exit 1
fi
