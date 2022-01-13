#!/usr/bin/env bash
# Bash script sets up web servers for deployment of web_static

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p ~/data/web_static/{releases/test,shared}
echo "Deployment of web_static" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i "42i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
