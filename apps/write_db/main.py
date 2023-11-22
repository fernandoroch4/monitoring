import sys
import pymysql.cursors
import concurrent.futures
from uuid import uuid4
import random
from datetime import datetime


def build_sql():
    return """
    INSERT INTO `transactions` (
        `account_id`,
        `destination_account_id`,
        `amount`,
        `transaction_type`
    ) VALUES (
        %s,
        %s,
        %s,
        %s,
    )
"""


def build_values():
    return (
        str(uuid4()),
        str(uuid4()),
        round(random.random() * 10_000, 9),
        random.choice(["deposit", "payment"]),
    )


def load_data(connection, cursor, worker):
    sql = build_sql()

    for num in range(1, 100_001):
        values = build_values()
        cursor.execute(sql, values)
        print(
            f"{datetime.now().isoformat()} - INFO - inserting data with worker {worker} row {num})"
        )

        if num % 1_000 == 0:
            connection.commit()
            print(
                f"{datetime.now().isoformat()} - INFO - committing data with worker {worker}"
            )


if __file__ == "__main__":
    try:
        connection = pymysql.connect(
            host="db",
            user="root",
            password="root",
            database="bank",
            port=3306,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

        with connection:
            with connection.cursor() as cursor:
                with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
                    for worker in range(1, 9):
                        executor.submit(load_data, connection, cursor, worker)
    except Exception as e:
        print(e)
        sys.exit(1)
