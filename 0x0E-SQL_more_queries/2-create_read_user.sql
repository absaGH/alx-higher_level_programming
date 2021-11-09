-- creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 have only SELECT privilege in the database hbtn_0d_2
-- The password of user_0d_2 is set to user_0d_2_pwd
-- Even if the database hbtn_0d_2 already exists, the script willn't fail
-- Even if the user user_0d_2 already exists, the script willn't fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
