create database spotify;
use spotify;

CREATE TABLE Artist(
	artist_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    artist_name Varchar(50) NOT NULL,
    dob date,
    gender Varchar(10),
    followers int
   
);

CREATE TABLE Genre(
	genre_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL
);

CREATE TABLE CUSTOMER(
	customer_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL ,
    birthdate date,
    gender Varchar(10),
    address VARCHAR(100)
);



CREATE TABLE Songs(
	song_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(125) NOT NULL,
    release_date date,
    genre_id int,
    artist_id int,
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id) ON DELETE CASCADE,
	FOREIGN KEY (artist_id) REFERENCES Artist(artist_id) ON DELETE CASCADE
);



CREATE TABLE Plays(
	play_id int NOT NULL auto_increment PRIMARY KEY,
    song_id int,
    play_date date,
    customer_id int,
    FOREIGN KEY (song_id) REFERENCES Songs(song_id) ON DELETE CASCADE,
    FOREIGN KEY  (customer_id) REFERENCES customer(customer_id) ON delete CASCADE
);





drop database spotify;

-- select * from songs; 

-- delete from songs;
-- drop table songs;
-- drop table plays;
-- select * from plays;
-- select * from customer;

SELECT * FROM PLAYS;
select * from customer;

-- set foreign_key_checks = 1;

ALTER TABLE plays
ADD CONSTRAINT fk_plays_customer
FOREIGN KEY (customer_id) 
REFERENCES customer(customer_id) 
ON delete CASCADE;

-- ALTER TABLE plays ENGINE = InnoDB;

desc plays;

update customer
set customer_id = 1001
where customer_id = 719;

ALTER TABLE plays DROP FOREIGN KEY fk_plays_customer;

-- Update data or fix any issues

-- Add the foreign key constraint back
ALTER TABLE plays
ADD CONSTRAINT fk_plays_customer
FOREIGN KEY (customer_id) 
REFERENCES customer(customer_id) 
ON UPDATE CASCADE;


rename table user to customer;





drop database spotify;

select * from artist;
select * from customer; 
select * from genre;
select * from songs;
select * from plays;

delete from genre where genre_id=2;
delete from artist where artist_id=40;
