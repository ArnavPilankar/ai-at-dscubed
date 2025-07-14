import psycopg2
import os
import json
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def read_sql_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def run_ddl():
    sql = read_sql_file("DDL/create_experiment_table.sql")
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    print("DDL executed successfully.")

def run_dml():
    sql = read_sql_file("DML/insert_experiments.sql")
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    print("DML executed successfully.")

def run_second_ddl():
    sql = read_sql_file("DDL/create_best_models_table.sql")
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    print("downstream table created")

def run_second_dml():
    sql = read_sql_file("DML/refresh_best_models.sql")
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    print("downstream table refreshed")

def view_table(table_name, limit=5, order_by="accuracy"):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name} ORDER BY {order_by} DESC LIMIT %s;", (limit,))
            rows = cur.fetchall()
            col_names = [desc[0] for desc in cur.description]

            print("\n Table Preview:\n")
            for row in rows:
                row_dict = dict(zip(col_names, row))  # map column names to values
                print(json.dumps(row_dict, indent=2, default=str))

                
if __name__ == "__main__":
    run_ddl()
    run_dml()
    run_second_ddl()
    run_second_dml()
    view_table("project_two.arnav")
    view_table("project_two.arnav_best_models", order_by="best_accuracy")