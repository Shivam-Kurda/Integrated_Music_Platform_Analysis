create database Youtube_Music;
use Youtube_Music;

CREATE TABLE Artist(
	artist_ int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL,
    dob date,
    Followers int
    
);

CREATE TABLE Genre(
	genre_ int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL
);

CREATE TABLE customer(
	cust_ int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL ,
    dob date,
    sex Varchar(10),
    address VARCHAR(100)
);



CREATE TABLE Songs(
	song_ int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(125) NOT NULL,
    releasedate date,
    genre_ int,
    artist_ int,
    FOREIGN KEY (genre_) REFERENCES Genre(genre_) ON DELETE CASCADE,
	FOREIGN KEY (artist_) REFERENCES artist(artist_) ON DELETE CASCADE
);


CREATE TABLE Plays(
	playid int NOT NULL auto_increment PRIMARY KEY,
    song_ int,
    playdate date,
    cust_ int,
    FOREIGN KEY (song_) REFERENCES Songs(song_) ON DELETE CASCADE,
    FOREIGN KEY  (cust_) REFERENCES customer(cust_) ON DELETE CASCADE
);




drop database youtube_music;

select * from artist;
select * from customer;
select * from genre;
select * from plays;
select * from songs;