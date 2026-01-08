import time
import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    # Connexion utilisant les variables d'environnement
    return psycopg2.connect(
        host="db",
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
    )

@app.route('/')
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"App connectée à : {db_version}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)