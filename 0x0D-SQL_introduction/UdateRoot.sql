USE mysql;

UPDATE user SET authentication_string = PASSWORD('081419') WHERE User = 'root';

FLUSH PRIVILEGES;