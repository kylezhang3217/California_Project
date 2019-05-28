import pandas as pd

def load_data():
    data = pd.read_csv("/Users/Kyle/PycharmProjects/California_Project/California_Project/datasets/housing.csv")
    print("abcs")
    return data