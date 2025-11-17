import pandas as pd
import pandas.testing as pdt

import apputil


def test_task_functions_no_args():
    assert apputil.task_1() == []

    df2 = apputil.task_2()
    assert isinstance(df2, pd.DataFrame)
    assert list(df2.columns) == ["year", "total_admissions"]

    s3 = apputil.task_3()
    assert isinstance(s3, pd.Series)

    assert apputil.task_4() == []


def test_task_1_behavior():
    df = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [None, 2, 3],
        "col3": [None, None, 3],
        "gender": [" Male", "female ", "FEMALE"]
    })

    expected = df.isna().sum().sort_values().index.tolist()
    result = apputil.task_1(df)
    assert result == expected


def test_task_2_grouping():
    df = pd.DataFrame({"year": [2020, 2020, 2021, 2022, 2022, 2022]})
    expected = pd.DataFrame({"year": [2020, 2021, 2022], "total_admissions": [2, 1, 3]})
    res = apputil.task_2(df)
    # Ensure year column dtype doesn't cause assert issues
    res = res.sort_values("year").reset_index(drop=True)
    expected = expected.sort_values("year").reset_index(drop=True)
    pdt.assert_frame_equal(res, expected)


def test_task_3_gender_averages():
    df = pd.DataFrame({
        "gender": [" Male", "female", "FEMALE", "male"],
        "age": [30, 40, 50, 20]
    })

    res = apputil.task_3(df)
    # build expected
    df_clean = df.copy()
    df_clean["gender"] = df_clean["gender"].astype(str).str.strip().str.lower()
    expected = df_clean.groupby("gender")["age"].mean()
    # compare after sorting index for deterministic equality
    pdt.assert_series_equal(res.sort_index(), expected.sort_index())


def test_task_4_professions():
    df = pd.DataFrame({"profession": ["doctor", "nurse", "doctor", "engineer", "teacher", "doctor"]})
    expected = df["profession"].value_counts().head(5).index.tolist()
    res = apputil.task_4(df)
    assert res == expected

    # missing profession column -> empty list
    df2 = pd.DataFrame({"x": [1, 2, 3]})
    assert apputil.task_4(df2) == []
