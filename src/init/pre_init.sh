#!/bin/bash
# friday setup script
# run as sudo

apt install mysql-server -y
mysql_install_db
mysqld --initialize

service mysql status

pip install psycopg2 sqlalchemy
apt install python-mysqldb -y
