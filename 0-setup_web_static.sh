#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static


sudo apt update
sudo apt upgrade
sudo apt install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
printf %s "{
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
} "> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu /data/
sudo chgrp -hR ubuntu /data/
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
        }
    location /hbnb_static {
        alias /data/web_static/current;
        index index.hmtl index.htm;
        }
}" > /etc/nginx/sites-available/default
sudo service nginx restart
