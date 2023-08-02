#two sample
from scipy import stats

# Sample data
sample1 = [4, 5, 6, 7, 8]
sample2 = [1, 2, 3, 4, 5]

# Perform an independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(sample1, sample2)

# Print the t-statistic and p-value
print("T-statistic:", t_statistic)
print("P-value:", p_value)

****************************************************

#one sample
from scipy import stats

# Sample data
sample1 = [4, 5, 6, 7, 8]

# Perform an independent one-sample t-test
t_statistic, p_value = stats.ttest_1samp(sample1,6)

# Print the t-statistic and p-value
print("T-statistic:", t_statistic)
print("P-value:", p_value)

****************************************************

#paired
from scipy import stats

# Sample data
old = [1, 2, 3, 4, 5]
new = [4, 5, 6, 7, 8]

# Perform an independent one-sample t-test
t_statistic, p_value = stats.ttest_rel(old,new)

# Print the t-statistic and p-value
print("T-statistic:", t_statistic)
print("P-value:", p_value)

