# ---------------------------------------
# apputil.py
# Week 3 Coding Exercise
# ---------------------------------------

# Import only what autograder expects
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
    return fibonacci(n-1) + fibonacci(n-2)


# ---------------------------------------
# Exercise 2 – Convert integer to binary
# ---------------------------------------

def to_binary(n):
    """Convert a non-negative integer to its binary representation recursively."""
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ---------------------------------------
# Exercise 3 – Bellevue tasks
# ---------------------------------------

def task_1(df):
    """Return list of column names sorted by missing values (fewest → most)."""
    # Clean gender column
    if "gender" in df.columns:
        df_copy = df.copy()
        df_copy["gender"] = df_copy["gender"].astype(str).str.strip().str.lower()
    else:
        df_copy = df.copy()
    missing_counts = df_copy.isna().sum()
    return missing_counts.sort_values().index.tolist()


def task_2(df):
    """Return a DataFrame with columns: year, total_admissions."""
    return df.groupby("year").size().reset_index(name="total_admissions")


def task_3(df):
    """Return a Series: index=gender, values=average age."""
    df_copy = df.copy()
    if "gender" in df_copy.columns:
        df_copy["gender"] = df_copy["gender"].astype(str).str.strip().str.lower()
    return df_copy.groupby("gender")["age"].mean()


def task_4(df):
    """Return a list of the 5 most common professions (most → least)."""
    if "profession" not in df.columns:
        return []
    return df["profession"].value_counts().head(5).index.tolist()


# ---------------------------------------
# Optional: local test runner (won't affect autograder)
# ---------------------------------------

if __name__ == "__main__":
    # Example usage
    print("Fibonacci 9:", fibonacci(9))
    print("Binary 12:", to_binary(12))

    # Load CSV locally from URL for testing (optional)
    url = "https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv"
    try:
        df_bellevue = pd.read_csv(url)
        print("Task 1 columns:", task_1(df_bellevue))
        print("Task 2 totals:\n", task_2(df_bellevue).head())
        print("Task 3 avg age:\n", task_3(df_bellevue).head())
        print("Task 4 top professions:", task_4(df_bellevue))
    except Exception as e:
        print("Could not load Bellevue CSV locally:", e)