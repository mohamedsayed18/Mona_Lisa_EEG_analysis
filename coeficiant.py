"""
Coefficient matrix
"""

import numpy as np
import os
from scipy import signal
from scipy import stats
import matplotlib.pyplot as plt

def co_matrix(data):
    """
    I will made the diagonal zeros for calculation
    """
    count = 0
    #cm = np.identity(34)
    cm = np.zeros((34,34))
    for i in range(34-1):
        for j in range(i+1, 34):
            cm[i, j] = data[count]
            cm[j, i] = data[count]
            count+=1
    #print(count)
    return cm

all_coef = []
all_alphas = []



all_people = np.load("raw_signal.npy", allow_pickle=True)
alpha_data = np.load("alpha_signal.npy", allow_pickle=True)
beta_data = np.load("beta_signal.npy", allow_pickle=True)
#avgalpha_data = np.load("avg_alphas.npy", allow_pickle=True)
#beta_data = np.load("beta_signal.npy", allow_pickle=True)


"""
for person in beta_data:
    for intensity in person.T:
        coef_values = []
        alpha_values = []    
        for i in range(intensity.shape[1]-1):
            for j in range(i+1, intensity.shape[1]):
                p_coff, _ = stats.pearsonr(intensity[:,i], intensity[:,j])
                coef_values.append(p_coff)
                alpha_values.append(p_coff)
        all_alphas.append(np.average(alpha_values))
        all_coef.append(coef_values)

all_coef = np.array(all_coef)
all_alphas = np.array(all_alphas)

#np.save("beta_coefficients", all_coef)
#np.save("avg_alphas", all_alphas)
"""
all_coef = np.load("coefficients.npy", allow_pickle=True)
avg_alphas = np.load("avg_alphas.npy", allow_pickle=True)
#print(all_coef[0].shape)

p1_max = np.argmax(avg_alphas[:10])
p2_max = np.argmax(avg_alphas[10:20])
p3_max = np.argmax(avg_alphas[20:30])
p4_max = np.argmax(avg_alphas[30:40])
p5_max = np.argmax(avg_alphas[40:])
#all_max = np.argmax(avg_beta)

print(p1_max, p2_max, p3_max, p4_max, p5_max)  # person2, intensity=0.1 has the max
#print(all_max)

p1_mat = np.argmax(co_matrix(all_coef[p1_max])[:31, :31])//31, np.argmax(co_matrix(all_coef[p1_max])[:31, :31])%31
p2_mat = np.argmax(co_matrix(all_coef[p2_max+10])[:31, :31])//31, np.argmax(co_matrix(all_coef[p2_max+10])[:31, :31])%31
p3_mat = np.argmax(co_matrix(all_coef[p3_max+20])[:31, :31])//31, np.argmax(co_matrix(all_coef[p3_max+20])[:31, :31])%31
p4_mat = np.argmax(co_matrix(all_coef[p4_max+30])[:31, :31])//31, np.argmax(co_matrix(all_coef[p4_max+30])[:31, :31])%31
p5_mat = np.argmax(co_matrix(all_coef[p5_max+40])[:31, :31])//31, np.argmax(co_matrix(all_coef[p1_max+40])[:31, :31])%31

print(p1_mat, p2_mat, p3_mat, p4_mat, p5_mat)
