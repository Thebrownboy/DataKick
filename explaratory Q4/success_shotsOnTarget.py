import pandas as pd

class shotsOnTarget:

    def __init__(self):
        pass

    def clean_data(self, file_path):
        df = pd.read_csv(file_path)
        # only keep columns HomeTeam, AwayTeam, FTR, HST, AST
        df = df[['HomeTeam', 'AwayTeam', 'FTR', 'HST', 'AST']]
        # leave only rows with HomeTeam == 'Liverpool' OR AwayTeam == 'Liverpool'
        df = df[(df['HomeTeam'] == 'Liverpool') | (df['AwayTeam'] == 'Liverpool')]
        # count the number of shots on target for Liverpool case it wins either as HomeTeam or AwayTeam
        df['SOT'] = df.apply(lambda row: row['HST'] if row['HomeTeam'] == 'Liverpool' and row['FTR'] == 'H' else row['AST'] if row['AwayTeam'] == 'Liverpool' and row['FTR'] == 'A' else 0, axis=1)
        # count the number of shots on target for Liverpool case it loses either as HomeTeam or AwayTeam
        df['SOT'] = df.apply(lambda row: row['HST'] if row['HomeTeam'] == 'Liverpool' and row['FTR'] == 'A' else row['AST'] if row['AwayTeam'] == 'Liverpool' and row['FTR'] == 'H' else row['SOT'], axis=1)
        # count the number of shots on target for Liverpool case it draws either as HomeTeam or AwayTeam
        df['SOT'] = df.apply(lambda row: row['HST'] if row['FTR'] == 'D' else row['SOT'], axis=1)
        # add result column to the dataframe W, L, D 
        df['Result'] = df.apply(lambda row: 'W' if row['HomeTeam'] == 'Liverpool' and row['FTR'] == 'H' 
            else 'W' if row['AwayTeam'] == 'Liverpool' and row['FTR'] == 'A' 
            else 'L' if row['HomeTeam'] == 'Liverpool' and row['FTR'] == 'A' 
            else 'L' if row['AwayTeam'] == 'Liverpool' and row['FTR'] == 'H' 
            else 'D' if row['FTR'] == 'D' else 0, axis=1)
        # drop columns HomeTeam, AwayTeam, FTR, HST, AST
        df = df.drop(columns=['HomeTeam', 'AwayTeam', 'FTR', 'HST', 'AST'])
        #  give each row a unique index
        df = df.reset_index(drop=True)
        return df

    def df_to_csv(self, df):
        df.to_csv('matches_shots_out.csv', index=False)

if __name__ == '__main__':
    shotsOnTarget = shotsOnTarget()
    list = []
    for i in range(1, 7):
        filepath = './data source/shotsOnTarget_csv/shotsOnTarget' + str(i) + '.csv'
        df = shotsOnTarget.clean_data(filepath)
        print(df.shape, i)
        list.append(df)

    df = pd.concat(list)
    print(df.shape)
    shotsOnTarget.df_to_csv(df)
