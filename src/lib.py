import matplotlib.pyplot as plt
import polars as pl

def printMedian(df, target):
    print("median of" + target + ": " + str(df[target].median()))

def printDescribe(df):
    print(df.describe())

def printDF(df):
    print(df)


def visualize(df, target):
    plt.figure(figsize=(10, 6))
    plt.hist(df[target], bins=10, edgecolor="k", alpha=0.7)
    title = "Distribution of " + target
    plt.title(title)
    plt.xlabel(target)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    loca = target + "_distribution_polar.png"
    plt.savefig(loca)
    plt.show()
    
