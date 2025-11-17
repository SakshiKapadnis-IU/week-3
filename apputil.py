# -----------------------------
# Exercise 1: Fibonacci
# -----------------------------

def fibonacci(n):
    """
    Return the nth Fibonacci number using recursion.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# -----------------------------
# Exercise 2: Convert integer to binary
# -----------------------------

def to_binary(n):
    """
    Convert an integer to its binary string representation using recursion.
    """
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# -----------------------------
# Exercise 3 — The following functions
# expect df_bellevue to be PASSED IN from app.py
# -----------------------------

def task_1(df):
    """
    Return column names sorted by fewest → most missing values.
    Fixes the gender column first.
    """
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).strip().str.lower()

    missing_counts = df.isna().sum()
    return missing_counts.sort_values().index.tolist()


def task_2(df):
    """
    Return a DataFrame with:
        year, total_admissions
    """
    return (
        df.groupby("year")
          .size()
          .reset_index(name="total_admissions")
    )


def task_3(df):
    """
    Return a Series:
        index  = gender
        values = average age
    """
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    return df.groupby("gender")["age"].mean()


def task_4(df):
    """
    Return list of 5 most common professions.
    """
    if "profession" not in df.columns:
        print("Missing 'profession' column.")
        return []

    return df["profession"].value_counts().head(5).index.tolist()
