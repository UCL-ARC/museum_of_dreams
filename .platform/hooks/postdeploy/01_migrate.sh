#!/bin/bash
# container_commands:
#   01_migrate:
#     command: "source /var/app/venv/*/bin/activate && python manage.py migrate"
#     leader_only: true
# option_settings:
#   aws:elasticbeanstalk:application:environment:
#     DJANGO_SETTINGS_MODULE: museum_of_dreams_project.settings


source "$PYTHONPATH/activate" && {
    
    if [[ $EB_IS_COMMAND_LEADER == "true" ]];
    then 
        # log which migrations have already been applied
        python manage.py showmigrations;
        
        # migrate
        python manage.py migrate --noinput;
    else 
        echo "this instance is NOT the leader";
    fi
    
}