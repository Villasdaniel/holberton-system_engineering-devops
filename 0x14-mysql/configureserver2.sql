-- creates the database tyrell_corp in the server.
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- use tyrell_corp database.
USE tyrell_corp;

-- create table nexus6
CREATE TABLE IF NOT EXISTS nexus6 (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, name VARCHAR(256)NOT NULL);

-- insert inputs
INSERT INTO tyrell_corp.nexus6 (name, id) Values('elrami', 1);

-- grant select permisions to holberton_user over nexus6 table of tyrell_corp db
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- creates the MySQL server new user replica_user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';

-- grant replication to slave 'replica_user'@'%'
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- grant select permisions to holberton_user over user table of mysql db
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- update privileges
FLUSH PRIVILEGES;