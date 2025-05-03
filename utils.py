import pandas as pd
def load_data():
    file_path = r"C:\Users\Sebastiano Plaku\OneDrive\Desktop\HWR\Subjects\SoSe2025\Enterprise Architecture for Big Data\git_kata\git_kata\data\titanic.csv"
    return pd.read_csv(file_path)