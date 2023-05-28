from datetime import datetime
from random import randrange
from sqlite3 import connect

COUNT_INSERTS = int(input("Count input: "))


if __name__ == '__main__':
    with connect("/Users/vasilykoltsov/PycharmProjects/pythonProject4/industrial_safety_project/db.sqlite3") as conn:
        conn.executemany("""
        INSERT INTO industrial_safety_app_task 
            (temperature,
            pressure,
            mass,
            voltage,
            resistance,
            temperature1,
            pressure1,
            datetime) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", [(randrange(50, 400),
                        randrange(30, 100),
                        randrange(150, 165),
                        randrange(180, 230),
                        randrange(30, 50),
                        randrange(50, 400),
                        randrange(30, 100), datetime.now()) for _ in range(COUNT_INSERTS)])
