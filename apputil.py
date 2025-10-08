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
    Fix gender column only if needed to count missing values correctly.
    """
    df = df_bellevue.copy()
    if df.empty:
        return []

    # Fix gender column NaN issues without altering column names
    if 'gender' in df.columns:
        df['gender'] = df['gender'].replace(['', 'nan'], pd.NA)

    # Sort columns by missing values
    missing_counts = df.isnull().sum()
    sorted_cols = missing_counts.sort_values().index.tolist()
    return sorted_cols


def task_2():
    """
    Return DataFrame with:
    - 'year': each year in dataset
    - 'total_admissions': total rows per year
    """
    df = df_bellevue.copy()
    if df.empty or 'year' not in df.columns:
        return pd.DataFrame(columns=['year', 'total_admissions'])

    result = df.groupby('year').size().reset_index(name='total_admissions')
    return result


def task_3():
    """
    Return Series:
    Index: gender
    Values: average age for that gender
    """
    df = df_bellevue.copy()
    if df.empty or 'age' not in df.columns or 'gender' not in df.columns:
        return pd.Series(dtype=float)

    # Clean gender column
    df['gender'] = df['gender'].replace(['', 'nan'], pd.NA)
    df = df[df['age'].notnull()]
    return df.groupby('gender')['age'].mean()


def task_4():
    """
    Return list of top 5 most common professions in order of prevalence.
    """
    df = df_bellevue.copy()
    if df.empty or 'profession' not in df.columns:
        return []

    # Count raw values exactly as they appear
    top5 = df['profession'].value_counts().head(5).index.tolist()
    return top5
    
