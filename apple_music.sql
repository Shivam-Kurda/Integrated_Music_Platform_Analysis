create database apple_music;
use apple_music;

CREATE TABLE Artist(
	Art_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name Varchar(50) NOT NULL,
    Birth_date date,
    followers int
    
);

CREATE TABLE Genre(
	Genre_ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Genre_Name Varchar(50) NOT NULL
);

CREATE TABLE customer(
	cust_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name Varchar(50) NOT NULL ,
    last_name Varchar(50) NOT NULL ,
    Birth_date date,
    Gender Varchar(10),
    Location VARCHAR(100)
);



CREATE TABLE Songs(
	Song_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Song_Name varchar(125) NOT NULL,
    Song_Release_Date date,
    Genre_ID int,
    ART_id int,
    FOREIGN KEY (Genre_ID) REFERENCES Genre(Genre_ID) ON DELETE CASCADE,
	FOREIGN KEY (Art_id) REFERENCES Artist(Art_id) ON DELETE CASCADE
);


CREATE TABLE Plays(
	Play_id int NOT NULL auto_increment PRIMARY KEY,
    Song_id int,
    Play_Date date,
    Cust_ID int,
    FOREIGN KEY (Song_id) REFERENCES Songs(Song_id) ON DELETE CASCADE,
    FOREIGN KEY  (Cust_ID) REFERENCES customer(Cust_ID) ON DELETE CASCADE
);



drop database apple_music;


show databases;


select * from artist;
select * from customer;
select * from genre;
select * from plays;
select * from songs;