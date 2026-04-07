import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Lisa Wilder in 3308!'

@app.route('/db_test')
def testing():
    conn = pyscopg2.connect("postgresql://basketball_1xwx_user:P0P32rPoGNUdTMSUjkyaEZXWEpVSYd89@dpg-d7aflcvfte5s73b45d20-a/basketball_1xwx")
    conn.close()
    return "Database connection successful."