import numpy as np
from scipy.stats import norm

__author__ = 'Michal Kononenko'


def calculate_t1_noisy(tau, t1, noise):
    return 1 - np.exp(-tau/t1) + noise


def create_noise_process(array_to_make_noise, amplitude=1,
                         stdev=1, mean=0):
    dist = norm(loc=mean, standard_deviation=stdev)

    return amplitude * dist.rvs(len(array_to_make_noise))



