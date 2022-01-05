import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

path = "C:/Users/irfan/OneDrive/Desktop/MO TECH/avocado-updated-2020.csv"
df = pd.read_csv(path)
df.index

print(df['type'].value_counts(dropna=False))
print(df['geography'].value_counts(dropna=False))

mk = df['geography'] == 'Los Angeles'
px.line(df[mk], x='date', y='average_price', color='type')

mk = df['geography'] == 'Los Angeles'
px.line(df[mk], x='date', y='average_price', color='type')
