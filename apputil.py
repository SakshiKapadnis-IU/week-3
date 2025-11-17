import pandas as pd

# Load Bellevue Almshouse dataset
url = "https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv"
df_bellevue = pd.read_csv(url)

# ---------------------------------------
# Exercise 1 – Fibonacci
# ---------------------------------------
def fibonacci(n):
    """
    Return the nth Fibonacci number using recursion.
    Example: fibonacci(9) --> 34
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
    Convert a non-negative integer to binary (as a string) using recursion.
    Example: to_binary(12) --> '1100'
    """
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ---------------------------------------
# Exercise 3 – Bellevue dataset tasks
# ---------------------------------------

def task_1():
    """
    Return a list of column names sorted from fewest to most missing values.
    Cleans the gender column first (strip and lowercase).
    """
    df = df_bellevue.copy()
    
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    
    missing_counts = df.isna().sum()
    return missing_counts.sort_values().index.tolist()


def task_2():
    """
    Return a DataFrame with columns:
        - year
        - total_admissions (number of rows per year)
    """
    df = df_bellevue.copy()
    
    # Ensure 'date_in' column exists
    if "date_in" not in df.columns:
        print("date_in column missing")
        return pd.DataFrame(columns=["year", "total_admissions"])
    
    # Convert to datetime if not already
    df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
    
    # Extract the year
    df["year"] = df["date_in"].dt.year
    
    return df.groupby("year").size().reset_index(name="total_admissions")


def task_3():
    """
    Return a Series:
        - Index = gender
        - Values = average age
    """
    df = df_bellevue.copy()
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    return df.groupby("gender")["age"].mean()


def task_4():
    """
    Return a list of the 5 most common professions, ordered most to least frequent.
    """
    df = df_bellevue
    if "profession" not in df.columns:
        print("Profession column missing")
        return []
    return df["profession"].value_counts().head(5).index.tolist()

if __name__ == "__main__":
    print("Fibonacci 9:", fibonacci(9))         # Should print 34
    print("Binary 12:", to_binary(12))          # Should print '1100'
    print("Task 1 columns:", task_1())
    print("Task 2 DataFrame:\n", task_2())
    print("Task 3 Series:\n", task_3())
    print("Task 4 top 5 professions:", task_4())