import argparse
import sqlite3
from . import config 

def create_db():
    conn = sqlite3.connect(config.DB_CONNECTION)
    c = conn.cursor()
    with open('./src/sql/up.sql', 'r') as f:
        c.executescript(f.read())

    conn.commit()
    conn.close()

def remove_db():
    conn = sqlite3.connect(config.DB_CONNECTION)
    c = conn.cursor()
    with open('./src/sql/down.sql', 'r') as f:
        c.executescript(f.read())

    conn.commit()
    conn.close()


