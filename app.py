import psycopg2
from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


def get_db_connection():
    return psycopg2.connect(app.config['DATABASE_URL'])


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT NOW()')
    result = cursor.fetchall()
    conn.close()
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
