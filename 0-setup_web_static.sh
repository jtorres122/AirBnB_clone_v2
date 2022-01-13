#!/usr/bin/env bash
# Bash script sets up web servers for deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
mkdir -p ~/data/web_static/{releases/test,shared}
echo "<html>
  <head>
    Holberton School
  </head>
  <body>
    AirBnB clone deployed
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "42i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
