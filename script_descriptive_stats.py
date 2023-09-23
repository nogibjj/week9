import polars as pl
import lib

def main():
    df = pl.read_csv("nba.csv")
    lib.printDF(df)
    lib.printDescribe(df)
    lib.printMedian(df, "Age")
    lib.printMedian(df, "Weight")
    lib.printMedian(df, "Salary")
    lib.visualize(df, "Age")
    lib.visualize(df, "Weight")
    lib.visualize(df, "Salary")

main()
