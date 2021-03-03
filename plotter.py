"""
Ploting the coefficient matrix
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def co_matrix(data):
    count = 0
    cm = np.identity(31)
    for i in range(31-1):
        for j in range(i+1, 31):
            cm[i, j] = data[count]
            cm[j, i] = data[count]
            count+=1
    #print(count)
    return cm

def RMD(data, all=False):
    value = []
    for i in range(data.shape[1]-3-1):
        for j in range(i+1, data.shape[1]-3):
            dist = np.linalg.norm(data[:,i] - data[:,j])
            #print(dist)
            value.append(dist)
            #value.append(0 if np.linalg.norm(data[:,i] - data[:,j]) > 0.5 else 1)
    if all:
        return value
    else: 
        print(value)
        return np.average(value)


"""
# Linear coefficient matrix
all_coef = np.load("coefficients.npy", allow_pickle=True)
co_mat = co_matrix(all_coef[10])
norm_mat = 2.*(co_mat - np.min(co_mat))/np.ptp(co_mat)-1 # between [-1, 1]
"""

"""
# Draw the RMD Max coefficient 
wavelet_data = np.load("wavlet_data.npy", allow_pickle=True)
rec_value = []
for intense in wavelet_data:
    rec_value.append(RMD(intense, all=True))

np.save("all_RMD_value", np.array(rec_value))

rmd_data = np.load("all_RMD_value.npy", allow_pickle=True)
print(rmd_data.shape)
print(rmd_data[0].shape)
co_mat = co_matrix(rmd_data[5])
norm_mat = 2.*(co_mat - np.min(co_mat))/np.ptp(co_mat)-1 # between [-1, 1]
"""

# Draw Beta_coefficient matrix
all_coef = np.load("beta_coefficients.npy", allow_pickle=True)
co_mat = co_matrix(all_coef[47])
norm_mat = 2.*(co_mat - np.min(co_mat))/np.ptp(co_mat)-1 # between [-1, 1]

sns.heatmap(norm_mat, annot=False)
plt.title("Normalized max co-efficient value matrix, Beta")
plt.show()  
