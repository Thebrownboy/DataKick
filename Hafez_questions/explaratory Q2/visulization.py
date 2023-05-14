from matplotlib import axes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('top_players_out.csv')
df_copy = df.copy()
print(df_copy.shape)

df_copy = df_copy.groupby('Team').head(5)


def plot_top_players_Total_goals_assists():
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Top Players in the Premier League 2021/2022', fontsize=20)
    # set the title of each subplot
    axes[0, 0].set_title('Liverpool', fontsize=15)
    axes[0, 1].set_title('Manchester City', fontsize=15)
    axes[1, 0].set_title('Manchester United', fontsize=15)
    axes[1, 1].set_title('Tottenham Hotspur', fontsize=15)
    # plot the data
    sns.barplot(x='Total', y='Player', data=df_copy[df_copy['Team'] == 'Liverpool'],
                ax=axes[0, 0], palette='Blues_d')
    sns.barplot(x='Total', y='Player', data=df_copy[df_copy['Team'] == 'Manchester City'],
                ax=axes[0, 1], palette='Blues_d')
    sns.barplot(x='Total', y='Player', data=df_copy[df_copy['Team'] == 'Manchester United'],
                ax=axes[1, 0], palette='Blues_d')
    sns.barplot(x='Total', y='Player', data=df_copy[df_copy['Team'] == 'Tottenham Hotspur'],
                ax=axes[1, 1], palette='Blues_d')

    # set the label of x-axis
    axes[0, 0].set_xlabel('Total Goals + Assists', fontsize=15)
    axes[0, 1].set_xlabel('Total Goals + Assists', fontsize=15)
    axes[1, 0].set_xlabel('Total Goals + Assists', fontsize=15)
    axes[1, 1].set_xlabel('Total Goals + Assists', fontsize=15)
    # set the label of y-axis
    axes[0, 0].set_ylabel('Player', fontsize=15)
    axes[0, 1].set_ylabel('Player', fontsize=15)
    axes[1, 0].set_ylabel('Player', fontsize=15)
    axes[1, 1].set_ylabel('Player', fontsize=15)
    # set the limit of x-axis
    axes[0, 0].set_xlim(0, 40)
    axes[0, 1].set_xlim(0, 40)
    axes[1, 0].set_xlim(0, 40)
    axes[1, 1].set_xlim(0, 40)
    # set the limit of y-axis
    axes[0, 0].set_ylim(-1, 5)
    axes[0, 1].set_ylim(-1, 5)
    axes[1, 0].set_ylim(-1, 5)
    axes[1, 1].set_ylim(-1, 5)
    # set the size of x-axis
    axes[0, 0].tick_params(axis='x', labelsize=12)
    axes[0, 1].tick_params(axis='x', labelsize=12)
    axes[1, 0].tick_params(axis='x', labelsize=12)
    axes[1, 1].tick_params(axis='x', labelsize=12)
    # set the size of y-axis
    axes[0, 0].tick_params(axis='y', labelsize=12)
    axes[0, 1].tick_params(axis='y', labelsize=12)
    axes[1, 0].tick_params(axis='y', labelsize=12)
    axes[1, 1].tick_params(axis='y', labelsize=12)
    # set the size of the figure
    fig.tight_layout()
    # save the figure as a png file in the folder output plots
    fig.savefig('output plots/Top_Players_Total_goals_assists.png')


def plot_top_players_Goals_SoT():
    # create a figure with 4 subplots in terms of SoT
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Top Players in the Premier League 2021/2022', fontsize=20)
    # set the title of each subplot
    axes[0, 0].set_title('Liverpool', fontsize=15)
    axes[0, 1].set_title('Manchester City', fontsize=15)
    axes[1, 0].set_title('Manchester United', fontsize=15)
    axes[1, 1].set_title('Tottenham Hotspur', fontsize=15)
    # plot the data
    sns.barplot(x='SoT', y='Player', data=df_copy[df_copy['Team'] == 'Liverpool'],
                ax=axes[0, 0], palette='Accent')
    sns.barplot(x='SoT', y='Player', data=df_copy[df_copy['Team'] == 'Manchester City'],
                ax=axes[0, 1], palette='Accent')
    sns.barplot(x='SoT', y='Player', data=df_copy[df_copy['Team'] == 'Manchester United'],
                ax=axes[1, 0], palette='Accent')
    sns.barplot(x='SoT', y='Player', data=df_copy[df_copy['Team'] == 'Tottenham Hotspur'],
                ax=axes[1, 1], palette='Accent')
    # set the label of x-axis
    axes[0, 0].set_xlabel('Shots on Target', fontsize=15)
    axes[0, 1].set_xlabel('Shots on Target', fontsize=15)
    axes[1, 0].set_xlabel('Shots on Target', fontsize=15)
    axes[1, 1].set_xlabel('Shots on Target', fontsize=15)
    # set the label of y-axis
    axes[0, 0].set_ylabel('Player', fontsize=15)
    axes[0, 1].set_ylabel('Player', fontsize=15)
    axes[1, 0].set_ylabel('Player', fontsize=15)
    axes[1, 1].set_ylabel('Player', fontsize=15)
    # set the limit of x-axis
    axes[0, 0].set_xlim(0, 30)
    axes[0, 1].set_xlim(0, 30)
    axes[1, 0].set_xlim(0, 30)
    axes[1, 1].set_xlim(0, 30)
    # set the limit of y-axis
    axes[0, 0].set_ylim(-1, 5)
    axes[0, 1].set_ylim(-1, 5)
    axes[1, 0].set_ylim(-1, 5)
    axes[1, 1].set_ylim(-1, 5)
    # set the size of x-axis
    axes[0, 0].tick_params(axis='x', labelsize=12)
    axes[0, 1].tick_params(axis='x', labelsize=12)
    axes[1, 0].tick_params(axis='x', labelsize=12)
    axes[1, 1].tick_params(axis='x', labelsize=12)
    # set the size of y-axis
    axes[0, 0].tick_params(axis='y', labelsize=12)
    axes[0, 1].tick_params(axis='y', labelsize=12)
    axes[1, 0].tick_params(axis='y', labelsize=12)
    axes[1, 1].tick_params(axis='y', labelsize=12)
    # set the size of the figure
    fig.tight_layout()
    # save the figure as a png file in the folder output plots
    fig.savefig('output plots/Top_Players_Shots_on_Target 1.png')

# plot_top_players_Goals_SoT_2() to plot the data in terms of shots on target for All PLAYERS 
# using  countplot instead of barplot such that show count of shots on target for each player grouped by team
def plot_top_players_Goals_SoT_2():
    # create a figure with 4 subplots in terms of SoT
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Top Players in the Premier League 2021/2022', fontsize=20, )
    # set the title of each subplot
    axes[0, 0].set_title('Liverpool', fontsize=15)
    axes[0, 1].set_title('Manchester City', fontsize=15)
    axes[1, 0].set_title('Manchester United', fontsize=15)
    axes[1, 1].set_title('Tottenham Hotspur', fontsize=15)
    # plot the data
    sns.countplot(x='SoT', hue='Player', data=df_copy[df_copy['Team'] == 'Liverpool'],
                ax=axes[0, 0], palette='Accent')
    sns.countplot(x='SoT', hue='Player', data=df_copy[df_copy['Team'] == 'Manchester City'],
                ax=axes[0, 1], palette='Blues_d')
    sns.countplot(x='SoT', hue='Player', data=df_copy[df_copy['Team'] == 'Manchester United'],
                ax=axes[1, 0], palette='Blues_d')
    sns.countplot(x='SoT', hue='Player', data=df_copy[df_copy['Team'] == 'Tottenham Hotspur'],
                ax=axes[1, 1], palette='Blues_d')
    # expand the x axis to show more values and y axis make it smaller and and color the background of the plot and 
    # make lables with another colors
    axes[0, 0].set_xlabel('Shots on Target', fontsize=15)
    axes[0, 1].set_xlabel('Shots on Target', fontsize=15)
    axes[1, 0].set_xlabel('Shots on Target', fontsize=15)
    axes[1, 1].set_xlabel('Shots on Target', fontsize=15)
    # set the label of y-axis
    axes[0, 0].set_ylabel('Player', fontsize=15)
    axes[0, 1].set_ylabel('Player', fontsize=15)
    axes[1, 0].set_ylabel('Player', fontsize=15)    
    axes[1, 1].set_ylabel('Player', fontsize=15)
    # set the limit of x-axis
    axes[0, 0].set_xlim(0, 5)
    axes[0, 1].set_xlim(0, 5)
    axes[1, 0].set_xlim(0, 5)
    axes[1, 1].set_xlim(0, 5)
    # set the limit of y-axis
    axes[0, 0].set_ylim(-1, 1)
    axes[0, 1].set_ylim(-1, 1)
    axes[1, 0].set_ylim(-1, 1)
    axes[1, 1].set_ylim(-1, 1)
    # set the size of x-axis
    axes[0, 0].tick_params(axis='x', labelsize=12)
    axes[0, 1].tick_params(axis='x', labelsize=12)
    axes[1, 0].tick_params(axis='x', labelsize=12)
    axes[1, 1].tick_params(axis='x', labelsize=12)
    # set the size of y-axis
    axes[0, 0].tick_params(axis='y', labelsize=12)
    axes[0, 1].tick_params(axis='y', labelsize=12)
    axes[1, 0].tick_params(axis='y', labelsize=12)
    axes[1, 1].tick_params(axis='y', labelsize=12)
    # color of the background of the plot
    axes[0, 0].set_facecolor('lightpink')
    axes[0, 1].set_facecolor('lightpink')
    axes[1, 0].set_facecolor('lightpink')
    axes[1, 1].set_facecolor('lightpink')
    # MAKE y axis start from 0
    axes[0, 0].set_ylim(bottom=0)
    axes[0, 1].set_ylim(bottom=0)
    axes[1, 0].set_ylim(bottom=0)
    axes[1, 1].set_ylim(bottom=0)
    # set the size of the figure
    fig.tight_layout()
    # save the figure as a png file in the folder output plots
    fig.savefig('output plots/Top_Players_Shots_on_Target 2.png')

    
plot_top_players_Total_goals_assists()
plot_top_players_Goals_SoT()
plot_top_players_Goals_SoT_2()





