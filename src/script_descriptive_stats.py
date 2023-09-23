import polars as pl
import lib

# def main():
#     df = pl.read_csv("nba.csv")
#     print(df)
#     print(df.describe())
#     print("median of age: " + str(df["Age"].median()))
#     print("median of weight: " + str(df["Weight"].median()))
#     print("median of salary: " + str(df["Salary"].median()))
#     plt.figure(figsize=(10, 6))
#     plt.hist(df["Age"], bins=10, edgecolor="k", alpha=0.7)
#     plt.title("Distribution of Age")
#     plt.xlabel("Age")
#     plt.ylabel("Frequency")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig("Age_distribution_polar.png")
#     plt.show()

#     plt.figure(figsize=(10, 6))
#     plt.hist(df["Weight"], bins=10, edgecolor="k", alpha=0.7)
#     plt.title("Distribution of Weight")
#     plt.xlabel("Weight")
#     plt.ylabel("Frequency")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig("Weight_distribution_polar.png")
#     plt.show()

#     plt.figure(figsize=(10, 6))
#     plt.hist(df["Salary"], bins=10, edgecolor="k", alpha=0.7)
#     plt.title("Distribution of Salary")
#     plt.xlabel("Salary")
#     plt.ylabel("Frequency")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig("Salary_distribution_polar.png")
#     plt.show()


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
