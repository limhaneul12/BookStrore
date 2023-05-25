#!/bin/sh

echo "migration 을 시작합니다"
echo "현재 경로 --> " $(pwd)

cd kyobo

python manage.py makemigrations accounts
python manage.py makemigrations authentication 
python manage.py makemigrations store

python manage.py migrate