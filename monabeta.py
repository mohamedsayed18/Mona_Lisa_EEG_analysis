"""
Calculate beta value
"""

import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

avg_beta = []
"""
beta_people = np.load("beta_signal.npy", allow_pickle=True)
for person in beta_people:
    for intensity in person.T:
        beta_values = []
        for i in range(intensity.shape[1]-3-1): # alpha cut
            for j in range(intensity.shape[1]-3):
                p_coff, _ = pearsonr(intensity[:,i], intensity[:,j])
                beta_values.append(p_coff)
        avg_beta.append(np.average(beta_values))

#print(len(avg_beta))
#np.save("avg_beta", avg_beta)
"""

# Ploting 
betas = np.load("avg_beta.npy", allow_pickle=True)
# Normalize
betas_norm = 2.*(betas - np.min(betas))/np.ptp(betas)-1
inten = np.linspace(0.1,1, 10)
for i in range(0, 50, 10):
    plt.plot(inten, betas_norm[i:i+10])

plt.xlabel("intensity")
plt.ylabel("beta")
plt.show()