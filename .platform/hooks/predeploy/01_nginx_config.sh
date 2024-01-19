#!/bin/bash

# Update Nginx configuration to allow larger file uploads

# Path to the Nginx configuration file
nginx_conf_path="/etc/nginx/conf.d/elasticbeanstalk/02_file_uploads.conf"

# Maximum allowed file size in the client request (in this example, 3GB)
client_max_body_size="3000M"

# Check if the Nginx configuration file exists
if [ ! -f "$nginx_custom_conf" ]; then
    # Create the custom configuration file
    echo "server {" > "$nginx_custom_conf"
    echo "    client_max_body_size $client_max_body_size;" >> "$nginx_custom_conf"
    echo "}" >> "$nginx_custom_conf"

    # Restart Nginx to apply the changes
    service nginx restart
fi
