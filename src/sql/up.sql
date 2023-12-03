CREATE TABLE IF NOT EXISTS item (
	id INTEGER PRIMARY KEY autoincrement,
	name TEXT,
	category TEXT,
	created DATETIME DEFAULT current_timestamp,
	weight FLOAT,
	available FLOAT,
	expiration DATE
);
