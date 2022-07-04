import sqlite3
from cryptography.fernet import Fernet

conn = sqlite3.connect('journals.db')
c = conn.cursor()

c.execute("""CREATE TABLE journals (
        id integer PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        title text NOT NULL,
        site text,
        url text NOT NULL,
        date DATETIME NOT NULL
)""")


#c.execute("""CREATE TABLE users(
#        id integer PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
#        firstname text NOT NULL,
#        lastname text NOT NULL,
#        birthdate DATETIME NOT NULL,
#     email text UNIQUE NOT NULL,
#    password text NOT NULL,
#   role text default 'user' NOT NULL
#)""")


conn.commit()
conn.close()