import random
import numpy as np
import matplotlib.pyplot as plt

# mixture model 
# https://www.programcreek.com/python/?CodeExample=generate+data
def generate_data(num_samples, means, variances, weights):
    num_components = len(weights)
    samples_per_component = np.random.multinomial(num_samples, weights) # https://omz-software.com/pythonista/numpy/reference/generated/numpy.random.multinomial.html
    data = []
    for i in range(num_components):
        mean = means[i]
        variance = variances[i]
        samples = np.random.normal(loc=mean, scale=np.sqrt(variance), size=samples_per_component[i])
        data.extend(samples)  #https://www.freecodecamp.org/news/python-list-append-vs-python-list-extend/
    return np.array(data)

# mixture values
mix_means = [2, 7, 12]
mix_variances = [1, 1, 1]
mix_weights = [0.3, 0.5, 0.2]

np.random.seed(0)
data = generate_data(1000, mix_means, mix_variances, mix_weights)

# Plotting the data from random seed
plt.hist(data, bins=30)
plt.show()
