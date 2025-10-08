# test_app.py

from apputil import fibonacci, to_binary, task_1, task_2, task_3, task_4
import pandas as pd

def run_tests():
    print("===== Testing fibonacci =====")
    try:
        print(f"fibonacci(0) = {fibonacci(0)}")  # Expected: 0
        print(f"fibonacci(1) = {fibonacci(1)}")  # Expected: 1
        print(f"fibonacci(5) = {fibonacci(5)}")  # Expected: 5
        print(f"fibonacci(9) = {fibonacci(9)}")  # Expected: 34
    except Exception as e:
        print("fibonacci failed:", e)

    print("\n===== Testing to_binary =====")
    try:
        print(f"to_binary(0) = {to_binary(0)}")   # Expected: '0'
        print(f"to_binary(2) = {to_binary(2)}")   # Expected: '10'
        print(f"to_binary(12) = {to_binary(12)}") # Expected: '1100'
    except Exception as e:
        print("to_binary failed:", e)

    print("\n===== Testing task_1 =====")
    try:
        cols = task_1()
        print(f"task_1 columns (sorted by missing values): {cols}")
    except Exception as e:
        print("task_1 failed:", e)

    print("\n===== Testing task_2 =====")
    try:
        df_years = task_2()
        print(df_years.head())
        print(df_years.dtypes)
    except Exception as e:
        print("task_2 failed:", e)

    print("\n===== Testing task_3 =====")
    try:
        avg_age = task_3()
        print(avg_age)
    except Exception as e:
        print("task_3 failed:", e)

    print("\n===== Testing task_4 =====")
    try:
        top5_prof = task_4()
        print(f"Top 5 professions: {top5_prof}")
    except Exception as e:
        print("task_4 failed:", e)

if __name__ == "__main__":
    run_tests()
