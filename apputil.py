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
    """Convert a non-negative integer to its binary representation recursively."""
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ---------------------------------------
# Exercise 3 – Bellevue tasks
# ---------------------------------------
def task_1(df):
    """
    Return a list of column names sorted by number of missing values (fewest → most).
    Cleans 'gender' column before counting missing values.
    """
    df_copy = df.copy()
    if "gender" in df_copy.columns:
        df_copy["gender"] = df_copy["gender"].astype(str).str.strip().str.lower()
    return df_copy.isna().sum().sort_values().index.tolist()


def task_2(df):
    """
    Return a DataFrame with two columns:
        year
        total_admissions (count of rows per year)
    """
    return df.groupby("year").size().reset_index(name="total_admissions")


def task_3(df):
    """
    Return a Series:
        index = gender
        values = average age for that gender
    """
    df_copy = df.copy()
    if "gender" in df_copy.columns:
        df_copy["gender"] = df_copy["gender"].astype(str).str.strip().str.lower()
    return df_copy.groupby("gender")["age"].mean()


def task_4(df):
    """
    Return a list of the 5 most common professions (most → least frequent).
    """
    if "profession" not in df.columns:
        return []
    return df["profession"].value_counts().head(5).index.tolist()