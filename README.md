# Генератор отчётов 
Вариант исполнения генератора отчётов в формате word и excel
использовал: django_crispy_form, docxtpl


# Сама БД
файл: report_gen.sql

Установить БД PostgreSQL.
1. Для windows: https://www.postgresql.org/download/windows/
2. Для остальных операционных систем можно найти здесь: https://www.postgresql.org/download/

Необходимо создать каркас БД с помощью этих команд, которые необходимо 
выполнить в консоли <b>psql 

#### CREATE DATABASE report_gendb;
#### CREATE USER reportuser WITH PASSWORD 'bailando123';
#### ALTER ROLE reportuser SET client_encoding TO 'utf8';
#### ALTER ROLE reportuser SET default_transaction_isolation TO 'read committed';
#### ALTER ROLE reportuser SET timezone TO 'UTC';
#### GRANT ALL PRIVILEGES ON DATABASE reportdatabase TO reportuser;






