import pandas as pd

from helpers import clean_data

df = pd.read_csv("data/sample_simple.csv")
print(df.head())

clean_data()
