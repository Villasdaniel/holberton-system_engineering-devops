-- creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- grant replication to client
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- update privileges
FLUSH PRIVILEGES;