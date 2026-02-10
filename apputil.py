import pandas as pd

# 1
def fibonacci(n):
    """
    Return the nth Fibonacci number using recursion.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 2
def to_binary(n):
    """
    Convert an integer to its binary representation using recursion.
    Returns an integer (not a string).
    """
    if n < 2:
        return n
    return int(str(to_binary(n // 2)) + str(n % 2))

# 3
# Load dataset
df_bellevue = pd.read_csv("data/bellevue_almshouse.csv")

def task_1(df):
    """
    Return list of column names sorted by least to most missing values.
    """
    df = df.copy()
    if "gender" in df.columns:
        df["gender"] = df["gender"].replace("", pd.NA)
    missing_counts = df.isna().sum()
    return missing_counts.sort_values().index.tolist()


def task_2(df):
    """
    Return DataFrame with year and total admissions per year.
    """
    df = df.copy()
    if "year" not in df.columns:
        print("Year column missing from dataset.")
    admissions_by_year = df.groupby("year").size().reset_index(name="total_admissions")
    return admissions_by_year


def task_3(df):
    """
    Return Series with average age per gender.
    """
    df = df.copy()
    if "gender" in df.columns:
        # Normalize gender: strip whitespace and convert to lowercase
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    avg_age_by_gender = df.groupby("gender")["age"].mean()
    return avg_age_by_gender


def task_4(df):
    """
    Return list of 5 most common professions in order of prevalence.
    """
    df = df.copy()
    if "profession" not in df.columns:
        return []
    professions = df["profession"].dropna().value_counts().head(5).index.tolist()
    return professions