import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS emplyees(
    prenom text,
    nom text
)
""")

d = {"prenom":"Paul","nom":"Richard"}
c.execute("INSERT INTO employees VALUES (:prenom, :nom",)

conn.commit()
conn.close()