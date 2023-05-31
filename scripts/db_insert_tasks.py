from datetime import datetime
from pathlib import Path
from random import randrange
from sqlite3 import connect
from time import sleep

import click

BASE_DIR = Path(__file__).resolve().parent.parent / "industrial_safety_project"


@click.command
@click.argument("count_inserts", type=click.INT)
@click.argument("insert_at", type=click.INT)
def call_insert(count_inserts: int, insert_at: int):
    while True:
        start = datetime.now()
        print(f"{start=}")
        with connect(BASE_DIR / "db.sqlite3") as conn:
            conn.executemany(
                """
            INSERT INTO industrial_safety_app_task 
                (temperature,
                pressure,
                mass,
                voltage,
                resistance,
                temperature1,
                pressure1,
                datetime) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                [
                    (
                        randrange(50, 400),
                        randrange(30, 100),
                        randrange(150, 165),
                        randrange(180, 230),
                        randrange(30, 50),
                        randrange(50, 400),
                        randrange(30, 100),
                        datetime.now(),
                    )
                    for _ in range(count_inserts)
                ],
            )
        finish = datetime.now() - start
        print(f"{finish.total_seconds()=}")
        sleep(insert_at)


@click.group()
def cls():
    ...


cls.add_command(call_insert)

if __name__ == "__main__":
    cls()
