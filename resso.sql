create database resso;
use resso;

CREATE TABLE singer(
	aid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL,
    date_of_birth date,
    followers int
    
);

CREATE TABLE Genre(
	gid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL
);

CREATE TABLE user(
	cid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name Varchar(50) NOT NULL ,
    Date_of_Birth date,
    gender Varchar(10),
    location VARCHAR(100)
);


CREATE TABLE Songs(
	sid int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(125) NOT NULL,
    releasedate date,
    gid int,
    aid int,
    FOREIGN KEY (gid) REFERENCES Genre(gid) ON DELETE CASCADE,
	FOREIGN KEY (aid) REFERENCES singer(aid) ON DELETE CASCADE
);


CREATE TABLE Plays(
	pid int NOT NULL auto_increment PRIMARY KEY,
    sid int,
    playdate date,
    cid int,
    FOREIGN KEY (sid) REFERENCES Songs(sid) ON DELETE CASCADE,
    FOREIGN KEY  (cid) REFERENCES user(cid) ON DELETE CASCADE
);



drop database resso;

drop database resso;

select * from songs; 

delete from songs;
drop table songs;
drop table plays;
select * from plays;
select * from customer;



rename table user to customer;





drop database spotify;

select * from singer;
select * from user; 
select * from genre;
select * from songs;
select * from plays;

delete from user where cid=121;

delete from genre where genre_id=2;
