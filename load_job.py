import pandas as pd

def get_california_job_data():
    data = pd.read_csv("california_job_openings.csv")
    return data

