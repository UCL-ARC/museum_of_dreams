#!/bin/bash

set -e  # exit on unhandled errors by default

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

fail_safe_run() {
    "$@" || log "WARNING: Command '$*' failed, continuing..."
}

if [ -f /var/app/current/manage.py ]; then
    # Start venv
    cd /var/app
    source venv/staging-LQM1lest/bin/activate
    cd current

    # Run migrations
    fail_safe_run manage.py migrate

    echo `date`
    
    fail_safe_run python manage.py showmigrations

    # Collect static files
    fail_safe_run python manage.py collectstatic --no-input --verbosity 0
else
    echo "manage.py not found."
    exit 1
fi
