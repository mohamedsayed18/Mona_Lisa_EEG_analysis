"""
Task 4:
chi-square: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html
T-test:     

H0

"""
from scipy.stats import chisquare
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu

import numpy as np

# TODO Person at max value and data
all_people = np.load("alpha_signal.npy", allow_pickle=True)[0,5] #
chi, p_value = chisquare(all_people[:, :31])  #complete value

#print(chi, p_value)

# T-test check if the channels means are equal
t_val, p_val = ttest_ind(all_people[:,0], all_people[:,1])
print(t_val, p_val) # Display as coefficients matrix

# 
w_val, p_vall = mannwhitneyu(all_people[:,0], all_people[:,1])