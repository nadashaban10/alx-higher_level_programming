-- craete cities in the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE cities IF NOT EXISTS (
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) AND IS NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
	);

