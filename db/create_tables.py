import sqlite3

#Create db
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
#create ouroborostore table
c.execute('''CREATE TABLE IF NOT EXISTS ouroborostore
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            precio_normal TEXT NOT NULL,
            precio_oferta TEXT,
            enlace TEXT NOT NULL);''')
conn.commit()
