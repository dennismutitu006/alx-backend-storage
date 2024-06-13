-- this script creates a table users with similar requirments as q0.
-- country, enumeration of countries: US, CO and TN, never null (= default wi
-- be the first element of the enumeration, here US)


CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
