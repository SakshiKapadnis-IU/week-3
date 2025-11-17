try:
    import pandas as pd
except ImportError:
    pd = None  # avoids terminal errors when running file directly


def _load_data():
    """Load Bellevue dataset internally. Works only when pandas is available."""
    if pd is None:
        raise ImportError("pandas is required to load the dataset in autograder.")
    return pd.read_csv("bellevue_raw.csv")


# -------------------------
# Fibonacci
# -------------------------
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# -------------------------
# to_binary
# -------------------------
def to_binary(n):
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# -------------------------
# task_1
# -------------------------
def task_1():
    df = _load_data()
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    missing = df.isna().sum()
    return missing.sort_values().index.tolist()


# -------------------------
# task_2
# -------------------------
def task_2():
    df = _load_data()
    return (
        df.groupby("year")
          .size()
          .reset_index(name="total_admissions")
    )


# -------------------------
# task_3
# -------------------------
def task_3():
    df = _load_data()
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    return df.groupby("gender")["age"].mean()


# -------------------------
# task_4
# -------------------------
def task_4():
    df = _load_data()
    if "profession" not in df.columns:
        print("profession column missing.")
        return []
    return df["profession"].value_counts().head(5).index.tolist()


# -------------------------
# Prevent execution when run directly
# -------------------------
if __name__ == "__main__":
    print("apputil.py is not meant to be run directly.")
