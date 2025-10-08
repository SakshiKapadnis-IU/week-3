# apputil.py

import pandas as pd

# -------------------------------
# EXERCISE 1: Fibonacci (recursive)
# -------------------------------

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# -------------------------------
# EXERCISE 2: Convert Integer to Binary (recursive)
# -------------------------------

def to_binary(n):
    if n < 0:
        raise ValueError("Only non-negative integers are supported.")
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# -------------------------------
# EXERCISE 3: Bellevue Almshouse Dataset Tasks
# -------------------------------

try:
    df_bellevue = pd.read_csv("df_bellevue.csv")
except Exception:
    df_bellevue = pd.DataFrame()


def task_1():
    """
    Return list of column names sorted by missing values (least -> most).
    Only fix gender column to correctly count missing values.
    """
    df = df_bellevue.copy()
    if df.empty:
        return []

    # Fix gender column: count blank strings as missing
    if 'gender' in df.columns:
        df['gender'] = df['gender'].replace('', pd.NA)

    # Sort columns by number of missing values
    return df.isnull().sum().sort_values().index.tolist()


def task_2():
    """
    Return a DataFrame:
    - 'year': each year in dataset
    - 'total_admissions': count per year
    Sorted by 'year' ascending.
    """
    df = df_bellevue.copy()
    if df.empty or 'year' not in df.columns:
        return pd.DataFrame(columns=['year', 'total_admissions'])

    result = df.groupby('year', as_index=False).size()
    result.columns = ['year', 'total_admissions']
    return result.sort_values('year').reset_index(drop=True)


def task_3():
    """
    Return Series: index = gender, value = average age
    """
    df = df_bellevue.copy()
    if df.empty or 'age' not in df.columns or 'gender' not in df.columns:
        return pd.Series(dtype=float)

    df['gender'] = df['gender'].replace('', pd.NA)
    df_clean = df[df['age'].notnull() & df['gender'].notnull()]
    return df_clean.groupby('gender')['age'].mean()


def task_4():
    """
    Return list of top 5 most common professions in order of prevalence.
    Ignore missing/empty entries.
    """
    df = df_bellevue.copy()
    if df.empty or 'profession' not in df.columns:
        return []

    df_clean = df[df['profession'].notnull() & (df['profession'].astype(str).str.strip() != '')]
    return df_clean['profession'].value_counts().head(5).index.tolist()