import sqlite3 as sq


# def readAva(n):
#     try:
#         with open(f"avas/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False


with sq.connect("cars.db") as con:
    cur = con.cursor()

    # cur.executescript(
    #     """CREATE TABLE IF NOT EXISTS users (
    #         name TEXT,
    #         ava BLOB,
    #         score INTEGER
    #     );
    # """
    # )

    with open("sql_damp.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)
