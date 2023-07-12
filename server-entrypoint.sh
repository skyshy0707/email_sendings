#!/bin/sh

until cd /code/src
do
    echo "Вход в директорию проекта"
done

python manage.py makemigrations

until python manage.py migrate
do 
    echo "Migrations db applying"
    sleep 2
done

python manage.py collectstatic --noinput
python manage.py create_superuser_from_settings
'
python manage.py create_user user1 --email=user1@mail.ru --first_name=Andrew --last_name=Smith --password=qwerty123456
python manage.py create_user user2 --email=user2@yandex.ru --first_name=Alex --last_name=Moore --password=qwerty123456
python manage.py create_user user3 --email=user3@yahoo.com --first_name=VasiliumBlazheniumGenoniumStol --last_name=Fahrenkroksgrajtenbijldberrgen --password=qwerty123456
python manage.py create_user user4 --email=user4@gmail.com --first_name=Alex --last_name=Smith --password=qwerty123456
python manage.py create_user user5 --first_name=Evgenii --last_name=Fresko --password=qwerty123456
'
python manage.py runserver "0.0.0.0:8000"