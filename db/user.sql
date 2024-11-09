CREATE USER 'games_client'@'%' IDENTIFIED BY 'basedbased';
GRANT ALL PRIVILEGES on games.* to 'games_client'@'%';
FLUSH PRIVILEGES;