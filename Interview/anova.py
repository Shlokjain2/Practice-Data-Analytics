#one way anova
import scipy.stats as stats

# Sample data for three groups
group1 = [1, 2, 3, 4, 5]
group2 = [2, 4, 6, 8, 10]
group3 = [3, 6, 9, 12, 15]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3)

# Print the results
print("F-Statistic:", f_statistic)
print("p-value:", p_value)

****************************************************

#two way anova
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the data into a pandas DataFrame
data = pd.read_csv('data.csv')

# Perform two-way ANOVA using the formula API
model = ols('response ~ factor1 * factor2', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)


***********************************************************

# Importing libraries
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a dataframe
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
						'Watering': np.repeat(['daily', 'weekly'], 15),
						'height': [14, 16, 15, 15, 16, 13, 12, 11,
									14, 15, 16, 16, 17, 18, 14, 13,
									14, 14, 14, 15, 16, 16, 17, 18,
									14, 13, 14, 14, 14, 15]})


# Performing two-way ANOVA
model = ols('height ~ C(Fertilizer) + C(Watering) +\
C(Fertilizer):C(Watering)',
			data=dataframe).fit()
result = sm.stats.anova_lm(model, type=2)

# Print the result
print(result)