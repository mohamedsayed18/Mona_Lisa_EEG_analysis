"""
Draw the maximum co-efficient value matrix 

TODO: [Done]find the max RMD value, and get coefficient matrix for this value
"""

import numpy as np
import os
from scipy import signal
from scipy import stats
import matplotlib.pyplot as plt

# Global arrays
wav_out = []
def co_matrix(data):
    """
    I will made the diagonal zeros for calculation
    """
    count = 0
    #cm = np.identity(34)
    cm = np.zeros((31,31))
    for i in range(31-1):
        for j in range(i+1, 31):
            cm[i, j] = data[count]
            cm[j, i] = data[count]
            count+=1
    #print(count)
    return cm

def wave_let(filter_data, raw_data):
    """
    parameters:
    filter_data: One channel of the filtered data
    raw_data: One channel of the raw data

    return:
    the value of the whole channel
    """
    total = 0 
    for i in range(raw_data.shape[0]):
        total += raw_data[i] * morlet(filter_data[i])
    #print(f)
    return np.sqrt(filter_data.astype(np.complex)) * total

def morlet(value):
    return (1/np.power(np.pi, 1/4)) * (np.exp((2*np.pi*value)*1j)) 

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
        #print(value)
        return np.average(value)


if __name__ == "__main__":
    
    """    
    # Read data
    raw_data = np.load("raw_signal.npy", allow_pickle=True)
    filtered_data = np.load("beta_signal.npy", allow_pickle=True)
    #y = wave_let(filtered_data[0,1], raw_data[0,1])
    #x = morlet(filtered_data[0,1][0,0])
    #print(y)

    for person in range(5):
        for intensity in range(10):
            raw = raw_data[person, intensity]
            fil = filtered_data[person, intensity]
            wav_data = np.empty_like(raw, dtype=np.complex)
            for col in range(raw.shape[1]):
                wav_data[:,col] = wave_let(fil[:,col], raw[:,col])
            wav_out.append(wav_data)

    all_waves = np.array(wav_out)
    np.save("wavlet_beta_data", all_waves)
"""


    wavelet_data = np.load("wavlet_beta_data.npy", allow_pickle=True)
    #print(wavelet_data[0].shape)

    # calculate the rmd value
    rec_value = []
    for intense in wavelet_data:
        rec_value.append(RMD(intense))

    np.save("RMD_beta_value", rec_value)
 
    rmd_data = np.load("RMD_beta_value.npy", allow_pickle=True)
    
    #print(rmd_data.shape)
    #print(all_rmd[0].shape)
    """
    max_index = np.argmax(rmd_data)
    #print(max_index)
    #print(rmd_data[max_index])

    # find max for each person
    rmd_data = np.load("RMD_value.npy", allow_pickle=True)
    all_rmd = np.load("all_RMD_value.npy", allow_pickle=True)
    for i in range(0, 50, 10):
        max_index = np.argmax(rmd_data[i:i+10])
        print("H", max_index, max_index+i)
        person = co_matrix(all_rmd[max_index+i])
        place = np.argmax(person)//31, np.argmax(person)%31
        print(place)


"""
# plot 
    inten = np.linspace(0.1,1, 10)
    for i in range(0,50,10):
        person = "person", str(i/10+1)
        plt.plot(inten, rmd_data[i:i+10], label=person)

    plt.xlabel("intensity")
    plt.ylabel("RMD")
    plt.title("RMD for each_person")
    plt.show()
