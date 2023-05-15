import pandas as pd

class free_kicks:
    
    def __init__(self):
        pass

    def preprocessing(self, filepath, season_year):
        df = pd.read_csv(filepath)
        # leave only the columns HomeTeam, AwayTeam,FTHG ,FTAG  , FTR, HF, AF, Hc, Ac
        df = df[['HomeTeam', 'AwayTeam', 'FTHG',
                 'FTAG', 'FTR', 'HF', 'AF', 'HC', 'AC']]
        # leave only rows wher team is liverpool either home or away
        df = df[(df['HomeTeam'] == 'Liverpool') | (df['AwayTeam'] == 'Liverpool')]
        # rename the columns
        df.rename(columns={'HF': 'HomeFouls', 'AF': 'AwayFouls', 'HC': 'HomeCorners', 'AC': 'AwayCorners'}, inplace=True)
        # add season year
        df['SeasonYear'] = season_year
        return df
    
    def get_free_kicks(self, df):
        # add column for free kicks = fouls + corners and column for goals scored by liverpool
        # check if liverpool is home or away and add the free kicks and goals accordingly
        df['FreeKicks'] = 0
        df['Goals'] = 0
        for index, row in df.iterrows():
            if row['HomeTeam'] == 'Liverpool':
                df.at[index, 'FreeKicks'] = row['AwayFouls'] + row['AwayCorners']
                df.at[index, 'Goals'] = row['FTHG']
            else:
                df.at[index, 'FreeKicks'] = row['HomeFouls'] + row['HomeCorners']
                df.at[index, 'Goals'] = row['FTAG']
        
        # leave only the columns SeasonYear, FreeKicks, Goals
        df = df[['SeasonYear', 'FreeKicks', 'Goals']]
        return df
        

if __name__ == "__main__":
   
    fk = free_kicks()
    df = []
    df_free_kicks = []
    # loop over 5 seasons
    for i in range(5):
        season_year = 17 + i
        filepath = f'{season_year}.csv'
        df.append(fk.preprocessing(filepath, season_year))
        df_free_kicks.append(fk.get_free_kicks(df[i]))
    # concat the dataframes
    df_free_kicks = pd.concat(df_free_kicks)
    # save the dataframe to csv
    df_free_kicks.to_csv('free_kicks_goals_out.csv', index=False)



    