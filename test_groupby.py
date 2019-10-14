import pandas as pd
from reframe import Relation

def test_groupby1():
    data_real = {'country': ['USA', 'Canada', 'France'], 'continent': ['North America', 'North America', 'Europe']}
    df = pd.DataFrame(data=data_real)
    r = Relation(df)
    r = r.groupby('continent').count('country')

    data_expected = {'continent': ['Europe', 'North America'], 'count_country': [1, 2]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    assert r.equals(r_expected)

def test_groupby2():
    #This query does not necessarily represent a useful query, but is only intended to test the functionality
    data_real = {'major': ['CS', 'CS', 'Math', 'Math', 'DS'], 'gradyear': [2016, 2019, 2015, 2020, 2020]}
    df = pd.DataFrame(data=data_real)
    r = Relation(df)
    r = r.groupby('major').max('gradyear')

    data_expected = {'major': ['CS', 'DS', 'Math'], 'max_gradyear': [2019, 2020, 2020]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    assert r.equals(r_expected)

def test_groupby3():
    data_real = {'course': ['DBMS', 'OSA', 'ML', 'OSA', 'OSA'], 'student': ['Abby', 'Abby', 'Abby', 'Bob', 'Carson']}
    df = pd.DataFrame(data=data_real)
    r = Relation(df)
    r = r.groupby('student').count('course')

    data_expected = {'student': ['Abby', 'Bob', 'Carson'], 'count_course': [3, 1, 1]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    assert r.equals(r_expected)    