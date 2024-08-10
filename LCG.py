import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pseudo_random_generator(mult = 17253, mod = (2**31) - 1, seed = 123456789, size = 1):
    U = np.zeros(size)
    x = (seed*mult + 1) % mod
    U[0] = x/mod
    for i in range(1,size):
        x = (x*mult + 1) % mod
        U[i] = x/mod
    return U

def pseudo_uniform(low = 0, high = 1, seed = 123456789, size = 1):
    return low + (high - low)*pseudo_random_generator(seed = seed, size = size)

def plot(Low = 100, high = 600):
    Show = pseudo_uniform(low = Low, high= high, size = 10000)
    plt.hist(Show, bins= 20, edgecolor = 'k')
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.xlim(Low, high)
    plt.show()

# for i in range (25):
#     print(pseudo_uniform(1,12, size=100))

