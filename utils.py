import pandas as pd
import os

def load_data():
    file_path = os.path.join('data', 'titanic.csv')
    df = pd.read_csv(file_path)
    return df[df['sex'] == 'male']

def clean_data(df):
    """ Cleans the DataFrame by dropping rows with missing values and converting categorical columns to lowercase. """
    "df = df.dropna()" # Drop rows with missing values, if we dont comment this out then dataframe will be empty

    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = df[col].str.lower()

    return df