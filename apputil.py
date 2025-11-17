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
    """Convert an integer to its binary string representation using recursion."""
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ------------------------------------------------------------------
# Exercise 3 – Each task receives df_bellevue as an argument
# ------------------------------------------------------------------

def task_1(df):
    """
    Return a list of column names sorted by number of missing values
    (fewest missing → most missing). Fixes the gender column first.
    """
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()

    missing_counts = df.isna().sum()
    return missing_counts.sort_values().index.tolist()


def task_2(df):
    """
    Return a DataFrame with:
      - year
      - total_admissions (count of entries per year)
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
      values = average age for that gender
    """
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    return df.groupby("gender")["age"].mean()


def task_4(df):
    """
    Return a list of the five most common professions,
    sorted from most to least frequent.
    """
    if "profession" not in df.columns:
        print("profession column missing.")
        return []

    return df["profession"].value_counts().head(5).index.tolist()
