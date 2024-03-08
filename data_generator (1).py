
from faker import Faker
from faker_music import MusicProvider
import random
import mysql.connector
from datetime import datetime

fake=Faker('en_IN')
fake.add_provider(MusicProvider)


famous_singers = {
    1: ["Beyoncé", "Female", "1981-09-04"], 2: ["Adele", "Female", "1988-05-05"], 3: ["Taylor Swift", "Female", "1990-12-13"],
    4: ["Ed Sheeran", "Male", "1991-02-17"], 5: ["Justin Bieber", "Male", "1994-03-01"], 6: ["Ariana Grande", "Female", "1993-06-26"],
    7: ["Rihanna", "Female", "1988-02-20"], 8: ["Bruno Mars", "Male", "1985-10-08"], 9: ["Katy Perry", "Female", "1984-10-25"],
    10: ["Lady Gaga", "Female", "1986-03-28"], 11: ["Billie Eilish", "Female", "2001-12-18"], 12: ["Shawn Mendes", "Male", "1998-08-08"],
    13: ["Drake", "Male", "1986-10-24"], 14: ["Eminem", "Male", "1972-10-17"], 15: ["Michael Jackson", "Male", "1958-08-29"],
    16: ["Whitney Houston", "Female", "1963-08-09"], 17: ["Mariah Carey", "Female", "1970-03-27"], 18: ["Elvis Presley", "Male", "1935-01-08"],
    19: ["Bob Marley", "Male", "1945-02-06"], 20: ["Frank Sinatra", "Male", "1915-12-12"], 21: ["Freddie Mercury", "Male", "1946-09-05"],
    22: ["John Lennon", "Male", "1940-10-09"], 23: ["Celine Dion", "Female", "1968-03-30"], 24: ["David Bowie", "Male", "1947-01-08"],
    25: ["Prince", "Male", "1958-06-07"], 26: ["Madonna", "Female", "1958-08-16"], 27: ["Stevie Wonder", "Male", "1950-05-13"],
    28: ["John Legend", "Male", "1978-12-28"], 29: ["Alicia Keys", "Female", "1981-01-25"], 30: ["Justin Timberlake", "Male", "1981-01-31"],
    31: ["Dua Lipa", "Female", "1995-08-22"], 32: ["R. Kelly", "Male", "1967-01-08"], 33: ["Jay-Z", "Male", "1970-12-04"],
    34: ["Kanye West", "Male", "1977-06-08"], 35: ["Miley Cyrus", "Female", "1992-11-23"], 36: ["Sia", "Female", "1975-12-18"],
    37: ["Shakira", "Female", "1977-02-02"], 38: ["Selena Gomez", "Female", "1992-07-22"], 39: ["George Michael", "Male", "1963-06-25"],
    40: ["Lata Mangeshkar", "Female", "1929-09-28"], 41: ["Kishore Kumar", "Male", "1929-08-04"], 42: ["Asha Bhosle", "Female", "1933-09-08"],
    43: ["Mohammed Rafi", "Male", "1924-12-24"], 44: ["Arijit Singh", "Male", "1987-04-25"], 45: ["Shreya Ghoshal", "Female", "1984-03-12"],
    46: ["Udit Narayan", "Male", "1955-12-01"], 47: ["Sonu Nigam", "Male", "1973-07-30"], 48: ["Alka Yagnik", "Female", "1966-03-20"],
    49: ["Kumar Sanu", "Male", "1963-09-20"], 50: ["Jubin Nautiyal", "Male", "1983-06-14"]
}

song_names = ["Bohemian Rhapsody", "Imagine", "Like a Rolling Stone", "Hotel California", "Yesterday", "Billie Jean", "Purple Haze", "Let It Be", "Stairway to Heaven", "Blackbird", "Wonderwall", "Sweet Child o Mine", "Hey Jude", "Smells Like Teen Spirit", "Boys Dont Cry", "All You Need Is Love", "Brown Eyed Girl", "My Girl", "Stand by Me", "Every Breath You Take", "Johnny B. Goode", "I Want to Hold Your Hand", "Shape of You", "Despacito", "Thinking Out Loud", "Hello", "Uptown Funk", "Cant Stop the Feeling!", "Smooth Criminal", "Hotel California", "Bohemian Rhapsody", "Yesterday", "Imagine", "Let It Be", "Like a Rolling Stone", "Purple Haze", "Stairway to Heaven", "Wonderwall", "Hey Jude", "Smells Like Teen Spirit", "Blackbird", "Sweet Child o Mine", "Stand by Me", "Boys Dont Cry", "All You Need Is Love", "Brown Eyed Girl", "My Girl", "Every Breath You Take", "Johnny B. Goode", "I Want to Hold Your Hand", "Tum Hi Ho", "Mere Sapno Ki Rani Kab Aayegi Tu", "Tum Mile", "Kal Ho Naa Ho", "Jeene Laga Hoon", "Tera Ban Jaunga", "Dil Diyan Gallan", "Channa Mereya", "Tum Jo Aaye", "Gerua", "Tum Mile", "Pee Loon", "Tum Hi Ho", "Tum Se Hi", "Agar Tum Saath Ho", "Lag Ja Gale", "Janam Janam", "Ae Mere Humsafar", "Nashe Si Chadh Gayi", "Ae Mere Humsafar", "Raabta", "Tum Jo Aaye", "Ishq Wala Love", "Sun Saathiya", "Jeene Laga Hoon", "Tum Mile", "Bolna", "Tum Jo Aaye", "Ishq Di Baajiyaan", "Chhod Diya", "Bol Do Na Zara", "Tum Mile", "Janam Janam", "Lag Ja Gale", "Pee Loon", "Tum Jo Aaye", "Channa Mereya", "Gerua", "Tum Mile", "Tera Ban Jaunga", "Dil Diyan Gallan", "Tum Hi Ho", "Jeene Laga Hoon", "Tum Se Hi", "Agar Tum Saath Ho", "Kal Ho Naa Ho", "Chaiyya Chaiyya", "Mera Naam Chin Chin Chu", "Jai Ho", "Tum Mile", "Mere Sapno Ki Rani Kab Aayegi Tu", "Tum Hi Ho", "Tum Mile", "Kal Ho Naa Ho", "Jeene Laga Hoon", "Tera Ban Jaunga", "Dil Diyan Gallan", "Channa Mereya", "Tum Jo Aaye", "Gerua", "Tum Mile", "Pee Loon", "Tum Hi Ho", "Tum Se Hi", "Agar Tum Saath Ho", "Lag Ja Gale", "Janam Janam", "Ae Mere Humsafar", "Nashe Si Chadh Gayi", "Ae Mere Humsafar", "Raabta", "Tum Jo Aaye", "Ishq Wala Love", "Sun Saathiya", "Jeene Laga Hoon", "Tum Mile", "Bolna", "Tum Jo Aaye", "Ishq Di Baajiyaan", "Chhod Diya", "Bol Do Na Zara", "Tum Mile", "Janam Janam", "Lag Ja Gale", "Pee Loon", "Tum Jo Aaye", "Channa Mereya", "Gerua", "Tum Mile", "Tera Ban Jaunga", "Dil Diyan Gallan", "Tum Hi Ho", "Jeene Laga Hoon", "Tum Se Hi", "Agar Tum Saath Ho", "Kal Ho Naa Ho", "Chaiyya Chaiyya", "Mera Naam Chin Chin Chu", "Jai Ho", "Chak De India"]








# spotify
conn = mysql.connector.connect(host="localhost", user="root", passwd="Shivam@02", database="spotify")

def generating_artist_spotify():
    cur=conn.cursor()
    a=int(input("Enter starting entry : "))
    b=int(input("Enter last entry : "))

    for i in range(a,b+1):
        sql = "insert into artist values (NULL,'{}','{}','{}',{})".format(
                 famous_singers[i][0], famous_singers[i][2], famous_singers[i][1],random.randint(1000,10000))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_customers_spotify():
    cur=conn.cursor()
    n=int(input("Enter how many entries:"))
    for i in range(n):
        dict=fake.profile()
        sql = "insert into customer values (NULL,'{}','{}','{}','{}')".format(
            dict['name'],fake.date_of_birth(minimum_age=18, maximum_age=65), dict['sex'], dict['address'])
        cur.execute(sql)
    cur.execute("commit")
    cur.close()


def generating_genre_spotify():
    cur=conn.cursor()
    n=int(input("Enter how many entries : "))
    for i in range(n):
        name=input("Enter Genre Name : ")
        sql = "insert into genre values (NULL,'{}')".format(name)
        # sql = "insert into customer values (NULL,'{}')".format(fake.music_genre())
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_song_spotify():
    cur=conn.cursor()
    q1="select artist_id from artist"
    q2="select genre_id from genre"
    cur.execute(q1)
    rec=cur.fetchall()
    lartist=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lgenre=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into songs values (NULL,'{}','{}',{},{})".format(
            song_names[i],str(fake.date_between(datetime(1995,8,31),datetime(2023,9,20))),random.choice(lgenre),random.choice(lartist))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_plays_spotify():
    cur=conn.cursor()
    q1="select song_id from songs"
    q2="select customer_id from customer"
    cur.execute(q1)
    rec=cur.fetchall()
    lsong=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lcustomer=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into plays values (NULL,{},'{}',{})".format(
            random.choice(lsong),str(fake.date_between(datetime(1990,12,31),datetime(2023,9,20))),random.choice(lcustomer))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()


generating_artist_spotify()
generating_customers_spotify()
generating_genre_spotify()
generating_song_spotify()
generating_plays_spotify()

conn.close()








# # resso
conn = mysql.connector.connect(host="localhost", user="root", passwd="Shivam@02", database="resso")

def generating_artist_resso():
    cur=conn.cursor()
    a=int(input("Enter starting entry : "))
    b=int(input("Enter last entry : "))

    for i in range(a,b+1):
        sql = "insert into singer values (NULL,'{}','{}',{})".format(
                 famous_singers[i][0], famous_singers[i][2], random.randint(1000,10000))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_customers_resso():
    cur=conn.cursor()
    n=int(input("Enter how many entries : "))
    for i in range(n):
        dict=fake.profile()
        sql = "insert into user values (NULL,'{}','{}','{}','{}')".format(
            dict['name'],fake.date_of_birth(minimum_age=18, maximum_age=65), dict['sex'], dict['address'])
        cur.execute(sql)
    cur.execute("commit")
    cur.close()


def generating_genre_resso():
    cur=conn.cursor()
    n=int(input("Enter how many entries : "))
    for i in range(n):
        name=input("Enter Genre Name : ")
        sql = "insert into genre values (NULL,'{}')".format(name)
        # sql = "insert into customer values (NULL,'{}')".format(fake.music_genre())
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_song_resso():
    cur=conn.cursor()
    q1="select aid from singer"
    q2="select gid from genre"
    cur.execute(q1)
    rec=cur.fetchall()
    lartist=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lgenre=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into songs values (NULL,'{}','{}',{},{})".format(
            song_names[i],str(fake.date_between(datetime(1995,8,31),datetime(2023,9,20))),random.choice(lgenre),random.choice(lartist))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_plays_resso():
    cur=conn.cursor()
    q1="select sid from songs"
    q2="select cid from user"
    cur.execute(q1)
    rec=cur.fetchall()
    lsong=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lcustomer=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into plays values (NULL,{},'{}',{})".format(
            random.choice(lsong),str(fake.date_between(datetime(1990,12,31),datetime(2023,9,20))),random.choice(lcustomer))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

generating_artist_resso()
generating_customers_resso()
generating_genre_resso()
generating_song_resso()
generating_plays_resso()

conn.close()











# apple_music
conn = mysql.connector.connect(host="localhost", user="root", passwd="Shivam@02", database="apple_music")

def generating_artist_apple_music():
    cur=conn.cursor()
    a=int(input("Enter starting entry : "))
    b=int(input("Enter last entry : "))

    for i in range(a,b+1):
        sql = "insert into artist values (NULL,'{}','{}',{})".format(
                 famous_singers[i][0], famous_singers[i][2], random.randint(1000,10000))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_customers_apple_music():
    cur=conn.cursor()
    n=int(input("Enter how many entries:"))
    for i in range(n):
        dict=fake.profile()
        sql = "insert into customer values (NULL,'{}','{}','{}','{}','{}')".format(
            dict['name'].split()[0],dict['name'].split()[1],fake.date_of_birth(minimum_age=18, maximum_age=65), dict['sex'], dict['address'])
        cur.execute(sql)
    cur.execute("commit")
    cur.close()


def generating_genre_apple_music():
    cur=conn.cursor()
    n=int(input("Enter how many entries : "))
    for i in range(n):
        name=input("Enter Genre Name : ")
        sql = "insert into genre values (NULL,'{}')".format(name)
        # sql = "insert into customer values (NULL,'{}')".format(fake.music_genre())
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_song_apple_music():
    cur=conn.cursor()
    q1="select Art_id from artist"
    q2="select genre_id from genre"
    cur.execute(q1)
    rec=cur.fetchall()
    lartist=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lgenre=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into songs values (NULL,'{}','{}',{},{})".format(
            song_names[i],str(fake.date_between(datetime(1995,8,31),datetime(2023,9,20))),random.choice(lgenre),random.choice(lartist))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_plays_apple_music():
    cur=conn.cursor()
    q1="select song_id from songs"
    q2="select cust_id from customer"
    cur.execute(q1)
    rec=cur.fetchall()
    lsong=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lcustomer=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into plays values (NULL,{},'{}',{})".format(
            random.choice(lsong),str(fake.date_between(datetime(1990,12,31),datetime(2023,9,20))),random.choice(lcustomer))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

generating_artist_apple_music()
generating_customers_apple_music()
generating_genre_apple_music()
generating_song_apple_music()
generating_plays_apple_music()

conn.close()










# # # youtube_music
conn = mysql.connector.connect(host="localhost", user="root", passwd="Shivam@02", database="youtube_music")

def generating_artist_youtube_music():
    cur=conn.cursor()
    a=int(input("Enter starting entry : "))
    b=int(input("Enter last entry : "))

    for i in range(a,b+1):
        sql = "insert into artist values (NULL,'{}','{}',{})".format(
                 famous_singers[i][0], famous_singers[i][2],random.randint(1000,10000))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_customers_youtube_music():
    cur=conn.cursor()
    n=int(input("Enter how many entries:"))
    for i in range(n):
        dict=fake.profile()
        sql = "insert into customer values (NULL,'{}','{}','{}','{}')".format(
            dict['name'],fake.date_of_birth(minimum_age=18, maximum_age=65), dict['sex'], dict['address'])
        cur.execute(sql)
    cur.execute("commit")
    cur.close()


def generating_genre_youtube_music():
    cur=conn.cursor()
    n=int(input("Enter how many entries : "))
    for i in range(n):
        name=input("Enter Genre Name : ")
        sql = "insert into genre values (NULL,'{}')".format(name)
        # sql = "insert into customer values (NULL,'{}')".format(fake.music_genre())
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_song_youtube_music():
    cur=conn.cursor()
    q1="select artist_ from artist"
    q2="select genre_ from genre"
    cur.execute(q1)
    rec=cur.fetchall()
    lartist=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lgenre=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into songs values (NULL,'{}','{}',{},{})".format(
            song_names[i],str(fake.date_between(datetime(1995,8,31),datetime(2023,9,20))),random.choice(lgenre),random.choice(lartist))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

def generating_plays_youtube_music():
    cur=conn.cursor()
    q1="select song_ from songs"
    q2="select cust_ from customer"
    cur.execute(q1)
    rec=cur.fetchall()
    lsong=[i[0] for i in rec]
    cur.execute(q2)
    rec=cur.fetchall()
    lcustomer=[i[0] for i in rec]
    n=int(input("Enter how many entries : "))
    for i in range(n):
        sql = "insert into plays values (NULL,{},'{}',{})".format(
            random.choice(lsong),str(fake.date_between(datetime(1990,12,31),datetime(2023,9,20))),random.choice(lcustomer))
        cur.execute(sql)
    cur.execute("commit")
    cur.close()

generating_artist_youtube_music()
generating_customers_youtube_music()
generating_genre_youtube_music()
generating_song_youtube_music()
generating_plays_youtube_music()

conn.close()