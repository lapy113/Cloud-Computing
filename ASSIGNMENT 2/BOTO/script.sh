#!/bin/sh
yum -y install httpd
systemctl enable httpd
systemctl start httpd.service

mkdir dist
cd dist
wget https://lapy113.s3.amazonaws.com/dist.zip
unzip dist.zip
cd dist

cp -r * /var/www/html
