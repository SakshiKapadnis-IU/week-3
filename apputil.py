import pandas as pd

# ---------------------------------------
# Exercise 1 – Fibonacci
# ---------------------------------------
def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------------------------------
# Exercise 2 – Convert integer to binary
# ---------------------------------------
def to_binary(n):
    """Convert an integer to its binary representation using recursion."""
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ---------------------------------------
# Exercise 3 – Load CSV internally for tasks
# ---------------------------------------
def load_df():
    """Load the Bellevue dataset for the tasks."""
    return pd.read_csv("bellevue_raw.csv")


def task_1():
    """
    Return a list of column names sorted by number of missing values
    (fewest missing → most missing). Clean gender column first.
    """
    df = load_df().copy()
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()

    missing_counts = df.isna().sum()
    return missing_counts.sort_values().index.tolist()


def task_2():
    """
    Return a DataFrame with:
      - year
      - total_admissions (number of entries per year)
    """
    df = load_df()
    return df.groupby("year").size().reset_index(name="total_admissions")


def task_3():
    """
    Return a Series:
      index = gender
      values = average age for that gender
    """
    df = load_df().copy()
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    return df.groupby("gender")["age"].mean()


def task_4():
    """
    Return a list of the five most common professions,
    ordered from most → least frequent.
    """
    df = load_df()
    if "profession" not in df.columns:
        return []
    return df["profession"].value_counts().head(5).index.tolist()


# Optional: test locally
if __name__ == "__main__":
    print("Fibonacci 9:", fibonacci(9))
    print("Binary 12:", to_binary(12))
    print("Task 1 columns:", task_1())
    print("Task 2 totals:\n", task_2())
    print("Task 3 avg age:\n", task_3())
    print("Task 4 top professions:", task_4())