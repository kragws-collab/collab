import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")


df = pd.read_csv("https://raw.githubusercontent.com/evgpat/stepik_from_idea_to_mvp/main/datasets/students.csv")

# print(df.info())
# print(df.describe(include='object'))

sns.histplot(df['math score'], kde = True)
plt.show()
