use mysql;

show variables like 'validate_password%';

SET GLOBAL validate_password_policy=LOW;

create user vsearch@localhost identified by 'qwer1234';

create database vsearchlogDB;

grant all privileges on vsearchlogDB.* to vsearch@localhost;

flush privileges;