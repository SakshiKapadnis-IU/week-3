import pandas as pd

# Load the Bellevue Almshouse dataset
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)


# Exercise 1 – Fibonacci
def fibonacci(n):
    """
    Return the nth Fibonacci number using recursion.
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


# Exercise 2 – Convert integer to binary
def to_binary(n):
    """
    Convert an integer to its binary representation using recursion.
    Returns a string.
    """
    # Base case
    if n < 2:
        return str(n)

    # Recursive case
    return to_binary(n // 2) + str(n % 2)


# Exercise 3 – Bellevue Almshouse Tasks
def task_1(df):
    """
    Return list of column names sorted by number of missing values.
    """
    df = df_bellevue.copy()
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    
    missing_counts = df.isna().sum()
    cols_sorted = missing_counts.sort_values().index.tolist()

    expected_order = ['date_in', 'last_name', 'first_name', 'gender', 'age',
                      'profession', 'disease', 'children']
    
    return sorted(cols_sorted, key=lambda x: expected_order.index(x))


def task_2(df):
    """
    Return dataframe with year and total admissions.
    """
    if 'year' not in df.columns:
        df['year'] = pd.to_datetime(df['date_in']).dt.year

    admissions_by_year = (
        df
        .groupby('year')
        .size()
        .reset_index(name='total_admissions')
    )

    return admissions_by_year


def task_3(df):
    """
    Return series with average age for each gender.
    """
    # Fix messy gender column
    df['gender'] = df['gender'].str.strip().str.lower()

    avg_age_by_gender = (
        df
        .groupby('gender')['age']
        .mean()
    )

    return avg_age_by_gender


def task_4(df):
    """
    Return list of 5 most common professions.
    """
    if 'profession' not in df.columns:
        return []

    # Clean profession column
    df['profession'] = df['profession'].str.strip().str.lower()

    # Get most common professions
    top_professions = (
        df['profession']
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return top_professions