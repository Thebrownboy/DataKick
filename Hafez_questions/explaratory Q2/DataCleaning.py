import pandas as pd


class data_cleaning:
    def __init__(self):
        pass

    def clean_data(self, file_path, team_name):
        df = pd.read_csv(file_path)
        df = df.dropna()
        # only keep columns Player, Gls, Ast,
        df = df[['Player', 'Gls', 'Ast', 'SoT']]
        df['Team'] = team_name
        return df

    def merge_data(self, df1, df2, df3, df4):
        df = pd.concat([df1, df2, df3, df4])
        df['Total'] = df['Gls'] + df['Ast']
        df = df.sort_values(by='Total', ascending=False)
        return df

    def df_to_csv(self, df):
        df.to_csv('top_players_out.csv', index=False)

    # def merge_2_files(self, file1, file2): # for SoT
    #     df1 = pd.read_csv(file1)
    #     df2 = pd.read_csv(file2)
    #     # leave columns Player, SoT
    #     df1 = df1[['Player', 'SoT']]
    #     # merge df1 and df2 on column Player
    #     df = pd.merge(df1, df2, on='Player')
    #     df.to_csv('totnham_statistics.csv', index=False)


if __name__ == '__main__':
    liverpool_file_path = 'liverpool_statistics.csv'
    mancity_file_path = 'mancity_statistics.csv'
    manunited_file_path = 'manunited_statistics.csv'
    totnham_file_path = 'totnham_statistics.csv'
    # temp_path = 'temp.csv'
    data_cleaning = data_cleaning()
    # __ = data_cleaning.merge_2_files(temp_path, totnham_file_path)
    df_liverpool = data_cleaning.clean_data(liverpool_file_path, 'Liverpool')
    df_mancity = data_cleaning.clean_data(mancity_file_path, 'Manchester City')
    df_manunited = data_cleaning.clean_data(
        manunited_file_path, 'Manchester United')
    df_totnham = data_cleaning.clean_data(
        totnham_file_path, 'Tottenham Hotspur')
    # use merge_data function to merge all dataframes
    df = data_cleaning.merge_data(
        df_liverpool, df_mancity, df_manunited, df_totnham)
    _ = data_cleaning.df_to_csv(df)
    print(df.head(6))
