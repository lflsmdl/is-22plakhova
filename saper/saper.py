import sqlite3 as sq

from data_users import info_users

with sq.connect("saper.db") as con:
    cur = con.cursor()

    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, 
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")

# with sq.connect("saper.db") as con:
       # cur = con.cursor()
      #  cur.executemany("INSERT INTO users VALUES(6, "Алексей", 2, 22, 1000)")

with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?)", info_users)

# with sq.connect("saper.db") as con:
# cur = con.cursor()
# cur.execute("SELECT * FROM users")
# result = cur.fetchall()
# print(result)

with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE old > 20 AND score < 1000")
        result = cur.fetchall()
        print(result)

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    result1 = cur.fetchone()
    result2 = cur.fetchmany(2)
    print(result1)
    print(result2)

