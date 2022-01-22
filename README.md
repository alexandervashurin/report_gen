# Генератор отчётов 
Вариант исполнения генератора отчётов в формате word и excel(если 
необходимо добавлю )
использовал: django_crispy_form, docxtpl

## Для создания БД


нужно выполнить:

CREATE DATABASE reportdatabase;
CREATE USER reportuser WITH PASSWORD 'bailando123';
ALTER ROLE reportuser SET client_encoding TO 'utf8';
ALTER ROLE reportuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE reportuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE reportdatabase TO reportuser;


для развертывания тестовой базы использовать скрипт 
first_sql.sql



