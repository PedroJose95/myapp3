DROP DATABASE if exists DB;
CREATE DATABASE db;
\connect db;

CREATE EXTENSION "uuid-ossp";
CREATE TABLE productos (
	sku uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	price money,
	title varchar(80),
	long_description text
);

INSERT INTO productos (price, title, long_description)VALUES
	(12.4, 'ejemplo1', 'producto ejmeplo 1'),
	(3.50, 'ejemplo2', 'producto ejemplo 2');
