# Генератор отчётов 
Вариант исполнения генератора отчётов в формате word и excel
использовал: django_crispy_form, docxtpl


# Сама БД
файл: report_gen.sql

2. Установить БД PostgreSQL.
устанавливаем docker, docker-compose. Переходим в папку /docker_images_db_pgadmin,
запускаем в терминале: docker-compose up -d
В дальнейшем работаем с docker-образами.

Необходимо создать каркас БД с помощью этих команд, которые необходимо  

запускаем эти скрипты:
#### ALTER ROLE reportuser SET client_encoding TO 'utf8';
#### ALTER ROLE reportuser SET default_transaction_isolation TO 'read committed';
#### ALTER ROLE reportuser SET timezone TO 'UTC';
#### GRANT ALL PRIVILEGES ON DATABASE reportdatabase TO reportuser;

