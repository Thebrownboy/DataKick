import pandas as pd

class possession:

    def __init__(self):
        pass
    
    def clean_data(self, file_path):
        df = pd.read_csv(file_path)
        # only keep columns Comp, Result, Poss
        df = df[['Comp', 'Result', 'Poss']]
        # leave only rows with Comp == 'Premier League'
        df = df[df['Comp'] == 'Premier League']
        # drop column Comp
        df = df.drop(columns=['Comp'])
        return df
    
    def df_to_csv(self, df):
        df.to_csv('possession_out.csv', index=False)
    

if __name__ == '__main__':

    possession = possession()
    list = []
    for i in range(1, 7):
        filepath = './data source/matches_statistics_csv/matches_statistics' + str(i) + '.csv'
        df = possession.clean_data(filepath)
        print(df.shape, i)
        list.append(df)
    
    df = pd.concat(list)
    print(df.shape)
    possession.df_to_csv(df)
    
