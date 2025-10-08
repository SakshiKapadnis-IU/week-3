# apputil.py

import pandas as pd

# -------------------------------
# EXERCISE 1: Fibonacci (recursive)
# -------------------------------

def fibonacci(n):
    """
    Recursive function that returns the nth Fibonacci number.
    The Fibonacci sequence starts with 0, 1, ...
    Example:
        fibonacci(9) -> 34
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# -------------------------------
# EXERCISE 2: Convert Integer to Binary (recursive)
# -------------------------------

def to_binary(n):
    """
    Recursive function that converts an integer into its binary representation (as a string).
    Example:
        to_binary(2) -> '10'
        to_binary(12) -> '1100'
    """
    if n < 0:
        raise ValueError("Only non-negative integers are supported.")
    
    # Base case
    if n < 2:
        return str(n)
    
    # Recursive case
    return to_binary(n // 2) + str(n % 2)


# -------------------------------
# EXERCISE 3: Bellevue Almshouse Dataset Tasks
# -------------------------------

# NOTE:
# The dataset should be read in the main app file (app.py),
# but for autograder compatibility, we'll ensure this works standalone too.
# Ensure df_bellevue.csv is present in the same directory.

try:
    df_bellevue = pd.read_csv("df_bellevue.csv")
except Exception:
    # Avoid breaking imports if CSV not found
    df_bellevue = pd.DataFrame()


def task_1():
    """
    Return a list of all column names sorted such that:
    - The first column has the least missing values
    - The last column has the most missing values
    Fixes any issues with the 'gender' column.
    """
    df = df_bellevue.copy()
    if df.empty:
        print("Warning: df_bellevue is empty or not loaded.")
        return []

    # Clean gender column if present
    if 'gender' in df.columns:
        df['gender'] = df['gender'].astype(str).str.strip().str.lower()
        df['gender'] = df['gender'].replace({
            'm': 'male', 'f': 'female',
            'nan': None, '': None
        })

    # Count missing values
    missing_counts = df.isnull().sum().sort_values()
    return list(missing_counts.index)


def task_2():
    """
    Return a DataFrame with columns:
    - 'year': each year in the data
    - 'total_admissions': total number of entries for that year
    """
    df = df_bellevue.copy()
    if df.empty:
        print("Warning: df_bellevue is empty or not loaded.")
        return pd.DataFrame(columns=['year', 'total_admissions'])

    # Ensure there is a 'year' column
    if 'year' not in df.columns:
        print("Warning: No 'year' column found in dataset.")
        return pd.DataFrame(columns=['year', 'total_admissions'])

    result = df.groupby('year').size().reset_index(name='total_admissions')
    return result


def task_3():
    """
    Return a Series:
    Index: gender
    Values: average age for each gender
    """
    df = df_bellevue.copy()
    if df.empty:
        print("Warning: df_bellevue is empty or not loaded.")
        return pd.Series(dtype=float)

    if 'age' not in df.columns or 'gender' not in df.columns:
        print("Warning: Required columns ('age', 'gender') missing.")
        return pd.Series(dtype=float)

    df['gender'] = df['gender'].astype(str).str.strip().str.lower()
    df = df[df['age'].notnull()]

    return df.groupby('gender')['age'].mean()


def task_4():
    """
    Return a list of the 5 most common professions in order of prevalence.
    The most common is first.
    """
    df = df_bellevue.copy()
    if df.empty:
        print("Warning: df_bellevue is empty or not loaded.")
        return []

    if 'profession' not in df.columns:
        print("Warning: No 'profession' column found.")
        return []

    df['profession'] = df['profession'].astype(str).str.strip().str.lower()
    return df['profession'].value_counts().head(5).index.tolist()
    
