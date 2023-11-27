import sys
import pymysql.cursors
import concurrent.futures
from uuid import uuid4
import random
from datetime import datetime
import time
from tabulate import tabulate


def build_sql():
    return """
    INSERT INTO `transaction` (
        `account_id`,
        `destination_account_id`,
        `amount`,
        `transaction_type`
    ) VALUES (
        %s,
        %s,
        %s,
        %s
    )
"""


def build_values():
    return (
        str(uuid4()),
        str(uuid4()),
        round(random.random(), 9),
        random.choice(["deposit", "payment"])
    )

bench = []
_rounds = []
TOTAL_OF_ROWS = 5_000
LATENCY = 0.015

def load_data(_round, worker):
    try:
        sql = build_sql()

        start = time.perf_counter()

        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="bank",
            port=3306,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        connection.autocommit(True)

        with connection:
            with connection.cursor() as cursor:

                for _ in range(1, TOTAL_OF_ROWS):
                    values = build_values()
                    cursor.execute(sql, values)
                    time.sleep(LATENCY)
    except Exception as e:
        print(e)
        sys.exit(1)
    else:
        end = time.perf_counter() 
        time_in_seconds = round(end - start, 0)
        time_in_minutes = round(time_in_seconds / 60, 0)
        writes_per_second = round(TOTAL_OF_ROWS / time_in_seconds, 0)
        writes_per_minute = round(writes_per_second * 60, 0)
        bench.append([_round, worker, TOTAL_OF_ROWS, writes_per_second, writes_per_minute, time_in_seconds, time_in_minutes, LATENCY, TOTAL_OF_ROWS * LATENCY])


if __name__ == "__main__":
    try:
        for _round in range(1, 101):

            start = time.perf_counter()

            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
                for worker in range(1, 9):
                    print(f'{datetime.now().isoformat()} - INFO - starting worker {worker}...')
                    executor.submit(load_data, _round, worker)
            end = time.perf_counter()
            total_of_inserts = TOTAL_OF_ROWS * 8
            time_in_seconds = round(end - start, 0)
            time_in_minutes = round(time_in_seconds / 60, 0)
            writes_per_second = round(TOTAL_OF_ROWS / time_in_seconds, 0)
            writes_per_minute = round(writes_per_second * 60, 0)
            _rounds.append([_round, total_of_inserts, writes_per_second, writes_per_minute, time_in_seconds, time_in_minutes])
            time.sleep(1)
            if _round == 100:
                print(tabulate(bench, headers=['Round', 'Worker', 'Inserts', 'WPS', 'WPM', 'Time (seconds)', 'Time (minutes)', 'LatencyInsert (seconds)', 'LatencyTotal (seconds)']))
        print(tabulate(_rounds, headers=['Round', 'Inserts', 'WPS', 'WPM', 'Time (seconds)', 'Time (minutes)']))
    except Exception as e:
        print(e)
        sys.exit(1)
