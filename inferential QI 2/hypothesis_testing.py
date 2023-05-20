import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, ttest_ind


# Does the number of fouls committed by Liverpool's opponents have a
# statistically significant impact on  goals scored?

# null hypothesis is that the number of fouls committed by Liverpool's opponents
# does not have a statistically significant impact on  goals scored
# alternative hypothesis is that the number of fouls committed by Liverpool's opponents
# does have a statistically significant impact on  goals scored

# To discover that, we have to perform a correlation test
# ccorrelation test returns corr coeff and p-value
# if p-value < .05 then reject the null hypothesis

class testing:

    def __init__(self):
        pass
    
    def correlation_test_pearsonr(self, df, significance_level=.05):
        corr_coeff, p_value = pearsonr(df['FreeKicks'], df['Goals'])
        print("Pearson Correlation Coefficient: ", corr_coeff)
        print("p-value: ", p_value)
        if p_value < significance_level:
            print("Reject the null hypothesis")
        else:
            print("Fail to reject the null hypothesis")
        fig = plt.figure()
        sns.regplot(x='FreeKicks', y='Goals', data=df)
        plt.savefig('output plots/pearson_correlation.png')

    def correlation_test_spearmanr(self, df, significance_level=.05):
        corr_coeff, p_value = spearmanr(df['FreeKicks'], df['Goals'])
        print("Spearman Correlation Coefficient: ", corr_coeff)
        print("p-value: ", p_value)
        if p_value < significance_level:
            print("Reject the null hypothesis")
        else:
            print("Fail to reject the null hypothesis")
     
    def t_test(self, df, significance_level=.05):
        t_stat, p_value = ttest_ind(df['FreeKicks'], df['Goals'])
        print("t-statistic: ", t_stat)
        print("p-value: ", p_value)
        if p_value < significance_level:
            print("Reject the null hypothesis")
        else:
            print("Fail to reject the null hypothesis")

if __name__ == "__main__":
    df = pd.read_csv('free_kicks_goals_out.csv')
    print(" shape of data  ",  df.shape)
    print("columns names" , df.columns)
    print(" unique values", df.nunique())
    # leave only columns needed
    _df = df[['FreeKicks', 'Goals']]
    test = testing()
    test.correlation_test_pearsonr(_df)
    test.correlation_test_spearmanr(_df)
    test.t_test(_df)
    # now we can see that there is a no correlation between the number of fouls
    # committed by Liverpool's opponents and the number of goals scored by Liverpool

