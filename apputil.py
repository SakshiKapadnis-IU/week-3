# ---------------------------------------
# Exercise 1 – Fibonacci
# ---------------------------------------

def fibonacci(n):
    """
    Return the nth Fibonacci number using simple recursion.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------------------------------
# Exercise 2 – Convert integer to binary
# ---------------------------------------

def to_binary(n):
    """
    Convert a non-negative integer into a binary string using recursion.
    """
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ------------------------------------------------------------------
# Exercise 3 – Each task receives df_bellevue as an argument
# ------------------------------------------------------------------

def task_1(df):
    """
    Return a list of column names sorted by the number of missing values,
    from fewest missing to most missing.

    The dataframe should NOT be modified, so cleaning is done on a copy.
    """
    df_copy = df.copy()

    if "gender" in df_copy.columns:
        df_copy["gender"] = (
            df_copy["gender"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

    missing_counts = df_copy.isna().sum()
    return missing_counts.sort_values().index.tolist()


def task_2(df):
    """
    Return a DataFrame with two columns:
        year
        total_admissions  (number of rows for each year)
    """
    return (
        df.groupby("year")
          .size()
          .reset_index(name="total_admissions")
    )


def task_3(df):
    """
    Return a Series where:
        index  = gender
        values = average age for that gender

    The dataframe must remain unchanged, so cleaning happens on a copy.
    """
    df_copy = df.copy()
    df_copy["gender"] = (
        df_copy["gender"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    return df_copy.groupby("gender")["age"].mean()


def task_4(df):
    """
    Return a list containing the five most common professions,
    ordered from most to least frequent.

    If the profession column is missing, return an empty list.
    """
    if "profession" not in df.columns:
        return []

    return df["profession"].value_counts().head(5).index.tolist()
