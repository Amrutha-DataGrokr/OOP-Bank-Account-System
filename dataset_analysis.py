
import pandas as pd
import numpy as np


#======================================================================#
#                       Dataset Loading                                #
#======================================================================#

def load_dataset(filename):
    df = pd.read_csv(filename)
    return df


#======================================================================#
#                       Dataset Inspection                             #
#======================================================================#

def inspect_dataset(df):

    # Dataset Shape
    print("Dataset Shape:")
    print(df.shape)

    # Dataset Columns
    print("\nColumn Names:")
    print(df.columns.tolist())

    # First 5 Records
    print("\nFirst 5 Records:")
    print(df.head(5))

    # Dataset Information
    print("\nDataset Information:")
    df.info()

    # Missing Values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate Records
    print("\nDuplicate Records:")
    print(df.duplicated().sum())

#======================================================================#
#                       Data Cleaning                                  #
#======================================================================#

def clean_dataset(df):

    # Filling missing Age with median
    df["Age"] = df["Age"].fillna(df["Age"].median())

    # Dropping Cabin column
    df.drop(columns=["Cabin"], inplace=True)

    # Filling missing Embarked with mode
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    print("\nUpdated Shape:")
    print(df.shape)

    return df

#======================================================================#
#                       Pandas Analysis                                #
#======================================================================#

def perform_pandas_analysis(df):
    # GroupBy Analysis
    group_summary = (
        df.groupby("Pclass")
        .agg(
            TotalPassengers=("PassengerId", "count"),
            TotalSurvived=("Survived", "sum"),
            AverageAge=("Age", "mean"),
            AverageFare=("Fare", "mean")
        )
        .reset_index()
    )

    print("\nPassenger Class Summary:")
    print(group_summary)

    # Calculating Survival Percentage
    group_summary["SurvivalRate"] = (
        group_summary["TotalSurvived"] /
        group_summary["TotalPassengers"]
    ) * 100

    print("\nPassenger Class Summary with Survival Rate:")
    print(group_summary)

    # Top 10 Passengers by Fare
    top_10 = df.nlargest(10, "Fare")[["Name", "Fare"]]

    print("\nTop 10 Passengers by Fare:")
    print(top_10)

    # Filtering: Pclass = 1 and Survived = 1
    filtered_df = df[
        (df["Pclass"] == 1) &
        (df["Survived"] == 1)
    ]

    print(
        "\nNo. of Survived Passengers from Pclass-1:",
        filtered_df.shape[0]
    )

    # Merging df and group_summary
    merged_df = pd.merge(
        df,
        group_summary,
        on="Pclass",
        how="left"
    )

    print("\nMerged Dataset Shape:")
    print(merged_df.shape)

    print("\nFirst 5 Records of Merged Dataset:")
    print(merged_df.head())

    print("\nMerged Dataset Columns:")
    print(merged_df.columns.tolist())

    return merged_df

#======================================================================#
#                       NumPy Analysis                                 #
#======================================================================#

def perform_numpy_analysis(df):
    # Mean of Passenger Age
    print(
        "\nMean of Passenger Age:",
        np.mean(df["Age"])
    )

    # Standard Deviation of Passenger Age
    print(
        "\nStandard Deviation of Passenger Age:",
        np.std(df["Age"])
    )

    # 25th Percentile
    print(
        "\n25th Percentile of Passenger Age:",
        np.percentile(df["Age"], 25)
    )

    # 75th Percentile
    print(
        "\n75th Percentile of Passenger Age:",
        np.percentile(df["Age"], 75)
    )

    # Correlation between Age and Fare
    correlation = np.corrcoef(
        df["Age"],
        df["Fare"]
    )[0, 1]

    print(
        "\nCorrelation Coefficient between Age and Fare:",
        correlation
    )

#======================================================================#
#                       Main Execution                                 #
#======================================================================#

if __name__ == "__main__":

    # Load Dataset
    df = load_dataset("titanic.csv")

    # Inspect Dataset
    inspect_dataset(df)

    # Clean Dataset
    df = clean_dataset(df)

    # Pandas Analysis
    merged_df = perform_pandas_analysis(df)

    # NumPy Analysis
    perform_numpy_analysis(df)
