"""
Analysing the EEG data for seeing monaliza

Todo:
* Reading .dat file done (done)
Draw a heat map https://likegeeks.com/python-correlation-matrix/
# edit the path of the files
Display data as strings or table https://stackoverflow.com/questions/35684318/numpy-2d-array-to-table
"""
import numpy as np
import os
from scipy import signal
from scipy import stats
import matplotlib.pyplot as plt

def co_matrix(data):
    count = 0
    cm = np.identity(33)
    for i in range(33):
        for j in range(i+1, 33):
            cm[i, j] = data[count]
            cm[j, i] = data[count]
            count+=1

# Read data
all_participants = []
data_alpha = []
data_beta = []

person_data = []
alphas = []
all_alphas = []
co_values = []  # Carry the values of the coof. matrix

alpha_cut = [8, 12]
beta_cut = [15, 30]

"""
# Store all data for all participant in file
for folder in os.listdir("/media/mohamed/C03CCDB43CCDA62E/tutorials/Innopolis/Year_2/Neuroscience/Neuroscience_Inno2021/Project2/Datasets/"):
    # loop for each particpant
    if folder.startswith("Participant"):
        #loop all intensities
        for filename in os.listdir("/media/mohamed/C03CCDB43CCDA62E/tutorials/Innopolis/Year_2/Neuroscience/Neuroscience_Inno2021/Project2/Datasets/"+folder+"/Figs_for_spectra/"):
            signals = np.loadtxt("/media/mohamed/C03CCDB43CCDA62E/tutorials/Innopolis/Year_2/Neuroscience/Neuroscience_Inno2021/Project2/Datasets/"+folder+"/Figs_for_spectra/"+filename)
            person_data.append(signals) # carry each intensity for a person

        all_participants.append(person_data)
        person_data = []

all_people = np.array(all_participants)
np.save("raw_signal", all_people)
"""

"""
# Store the alpha values
# Comment next line if you don't have the data stored in a file
all_people = np.load("raw_signal.npy", allow_pickle=True)   
for person in all_people: # every person
    #print("new person", person.shape)
    alpha = []
    for intensity in person.T: # fore every intensity(0.1 ... 1.0)
        #print("el raw", intensity.shape)
        coff = signal.firwin(intensity.shape[0], alpha_cut, pass_zero=False, fs=250)
        new_values = np.zeros_like(intensity)
        #print(new_values.shape, intensity.shape)
        for i in range(intensity.shape[1]): # alpha cut
            
            new_values[:,i] = np.convolve(intensity[:,i], coff, 'same')
        alpha.append(new_values)
    data_alpha.append(alpha)
data_alpha = np.array(data_alpha)
np.save("alpha_signal", data_alpha)

        # calculate coefficient values, Alpha
        alpha_values = []
        for i in range(new_values.shape[1]-1):
            print(new_values.shape[1])
            for j in range(i+1, new_values.shape[1]):
                p_coff, _ = stats.pearsonr(new_values[:,i], new_values[:,j])
                alpha_values.append(p_coff)

        co_values.append(alpha_values)
        print(len(co_values))
        alphas.append(np.average(alpha_values))
    all_alphas.append(alphas)
    alphas = []
    #print(len(all_alphas[-1])) 

#print(len(co_values))
#print(len(co_values[0]))

np.save("mydata", all_alphas)
"""

all_alphas = np.load("avg_alphas.npy", allow_pickle=True)
alpha_norm = 2.*(all_alphas - np.min(all_alphas))/np.ptp(all_alphas)-1

inten = np.linspace(0.1,1, 10)
for i in range(0, 50, 10):
    plt.plot(inten, alpha_norm[i:i+10])

plt.xlabel("intensity")
plt.ylabel("alpha")
plt.show()




