import enum

import psycopg2

from config import Config


def get_db_connection():
    return psycopg2.connect(Config.DATABASE_URL)


class UserFieldNames(enum.Enum):
    id = "id"
    first_name = "first_name"
    last_name = "last_name"
    date_of_birth = "date_of_birth"
    gender = "gender"
    interests = "interests"
    city = "city"
    profile_page = "profile_page"
    password = "password"


user_table_create_statement = """
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender VARCHAR(10),
    interests TEXT[],
    city VARCHAR(100),
    profile_page VARCHAR(255),
    password VARCHAR(100)
);
"""

# user_table_insert_statement = """
# INSERT INTO Users (first_name, last_name, date_of_birth, gender, interests, city, profile_page)
# VALUES ('Name', 'Lastname', '1990-01-01', 'Male', '{"Interest_1", "Interest_2"}', 'The City', 'http://link_to_profile');
# """


def prepare_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(user_table_create_statement)

    conn.commit()
    conn.close()
