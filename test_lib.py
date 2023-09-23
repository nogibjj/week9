import lib
import polars as pl

def test_printDF():
    df = pl.read_csv("nba.csv")
    lib.printDF(df)

def test_printDescribe():
    df = pl.read_csv("nba.csv")
    lib.printDescribe(df)

def test_printMedia():
    df = pl.read_csv("nba.csv")
    lib.printMedian(df, "Age")
    lib.printMedian(df, "Weight")
    lib.printMedian(df, "Salary")


def test_visualize():
    df = pl.read_csv("nba.csv")
    lib.visualize(df, "Age")
    lib.visualize(df, "Weight")
    lib.visualize(df, "Salary")


    
    

