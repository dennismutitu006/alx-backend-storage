-- a script that creates a table called users.
-- if the table already exists script should not fail.


CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email varchar(255) UNIQUE NOT NULL,
	name varchar(255),
	PRIMARY KEY (id)
);
