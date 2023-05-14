import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./matches_shots_possession.csv')
df_copy = df.copy()

def plot_bar(df_copy):
    avg_poss = df_copy.groupby('Result')['Poss'].mean()
    plt.figure(figsize=(10, 10))
    plt.bar(avg_poss.index, avg_poss.values, color=[
            '#FF8C00', '#228B22', '#4169E1'])
    plt.title('Average Possession for Result Categories')
    plt.xlabel('Result')
    plt.ylabel('Average Possession')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.gca().set_facecolor('#F5F5F5')
    for i, v in enumerate(avg_poss.values):
        plt.text(i, v + 1, str(round(v, 2)), ha='center',
                fontsize=12, fontweight='bold')
        
    plt.savefig('./output plots/avg_poss.png')

## use data augmentation to create more data
def increase_data(df_copy):
    df_augmented = pd.concat([df_copy] * 2, ignore_index=True)
    return df_augmented

# make a relation between poss and result ussing scatter plot
def plot_relation_res_pos(df):
    plt.figure(figsize=(8, 6))
    plt.boxplot([df[df['Result'] == 'W']['Poss'],
                df[df['Result'] == 'D']['Poss'],
                df[df['Result'] == 'L']['Poss']],
                labels=['Win', 'Draw', 'Lose'])
    plt.xlabel('Result')
    plt.ylabel('Possession')
    plt.title('Distribution of Possession by Result')
    plt.savefig('./output plots/pos_res.png')
    plt.show()


def plot_relation_res_SOT(df):
    plt.figure(figsize=(8, 6))
    plt.boxplot([df[df['Result'] == 'W']['SOT'],
                df[df['Result'] == 'D']['SOT'],
                df[df['Result'] == 'L']['SOT']],
                labels=['Win', 'Draw', 'Lose'])
    plt.xlabel('Result')
    plt.ylabel('shots on target')
    plt.title('Distribution of shots on target by Result')
    plt.savefig('./output plots/SOT_res.png')
    plt.show()
    

# df_augmented = increase_data(df_copy)
plot_bar(df_copy)
plot_relation_res_pos(df_copy)
plot_relation_res_SOT(df_copy)

