import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read data
df = pd.read_csv('./matches_shots_possession.csv')
df_copy = df.copy()
df_copy['Result'] = df_copy.apply(lambda row: 1 if row['Result'] == 'W' else 0 if row['Result'] == 'D' else -1, axis=1)
# # plot scatter plot
plt.figure(figsize=(10, 10))
plt.scatter(df_copy['SOT'], df_copy['Poss'], c=df_copy['Result'])
plt.colorbar()
plt.xlabel('Shots on target')
plt.ylabel('Possession')
#plt.show()
# save it in png in folder output plots
plt.savefig('./output plots/correlation.png')
# calculate correlation coefficient
corr = df_copy.corr()
print(corr)
# plot heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(corr, annot=True, cmap='coolwarm')
#plt.show()
# save it in png in folder output plots
plt.savefig('./output plots/correlation_heatmap.png')
