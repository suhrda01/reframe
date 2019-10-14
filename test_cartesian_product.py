import pandas as pd
from reframe import Relation

def test_cartesian_product1():
    data_real1 = {'country': ['USA', 'Canada', 'France'], 'continent': ['North America', 'North America', 'Europe']}
    data_real2 = {'gnp': [1234,5678], 'population': [100,250]}
    df1 = pd.DataFrame(data=data_real1)
    df2 = pd.DataFrame(data=data_real2)
    r1 = Relation(df1)
    r2 = Relation(df2)
    r = r1.cartesian_product(r2)

    data_expected = {'country': ['USA', 'USA', 'Canada', 'Canada', 'France', 'France'], 'continent': ['North America', 'North America', 'North America', 'North America', 'Europe', 'Europe'], 'gnp': [1234,5678,1234,5678,1234,5678], 'population': [100,250,100,250,100,250]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    assert r.equals(r_expected)

def test_cartesian_product2():
    data_real1 = {'student': ['Abby', 'Billy', 'Carson']}
    data_real2 = {'grade': ['A', 'A', 'B'], 'course': ['Math', 'Science', 'Math']}
    df1 = pd.DataFrame(data=data_real1)
    df2 = pd.DataFrame(data=data_real2)
    r1 = Relation(df1)
    r2 = Relation(df2)
    r = r1.cartesian_product(r2)

    data_expected = {'student': ['Abby', 'Abby', 'Abby', 'Billy', 'Billy', 'Billy', 'Carson', 'Carson', 'Carson'], 'grade': ['A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B'], 'course': ['Math', 'Science', 'Math', 'Math', 'Science', 'Math', 'Math', 'Science', 'Math']}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    assert r.equals(r_expected)

def test_cartesian_product3():
    data_real1 = {'student': ['Abby', 'Billy', 'Carson']}
    data_real2 = {'grade': ['B', 'A'], 'course': ['Math', 'Science']}
    df1 = pd.DataFrame(data=data_real1)
    df2 = pd.DataFrame(data=data_real2)
    r1 = Relation(df1)
    r2 = Relation(df2)
    r = r1.cartesian_product(r2)

    data_expected = {'student': ['Abby', 'Abby', 'Billy', 'Billy', 'Carson', 'Carson'], 'grade': ['B', 'A', 'B', 'A', 'B', 'A'], 'course': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science']}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    assert r.equals(r_expected)