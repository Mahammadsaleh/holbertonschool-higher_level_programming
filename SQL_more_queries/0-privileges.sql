-- Connect to MySQL server
mysql -u your_username -p

-- Run the following commands in MySQL prompt

-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Exit MySQL prompt
exit;

