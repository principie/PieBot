CREATE DATABASE users;

USE users;

CREATE TABLE user_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

ALTER TABLE user_details	
ADD course_name VARCHAR(255);

SELECT * FROM user_details;