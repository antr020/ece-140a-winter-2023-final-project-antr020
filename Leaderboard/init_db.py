# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists Users;")

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE Users (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      user_name   VARCHAR(60) NOT NULL unique,
      student_id  integer NOT NULL,
      email       VARCHAR(50) NOT NULL unique,
      password    VARCHAR(20) NOT NULL,
      created_at  TIMESTAMP
    );

    CREATE TABLE if not exists sessions (
        session_id varchar(64) primary key,
        session_data json not null,
        created_at timestamp not null default current_timestamp
    );


  """)
except:
  print("Users table already exists. Not recreating it.")


