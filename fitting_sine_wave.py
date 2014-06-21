"""
Tools for fitting a sine wave.
They are not very reliable though so don't
use this for science!
Well do, but figure out a better optimization
method.
"""
import numpy as np
import pylab as plb

def generate_data(Amp, freq, noise_amp):
    """
    Generates data x, y where

    y = Amp * sin(freq * x) + noise_amp * randn()
    """
    x = np.arange(0.,80.,0.01)
    y = Amp * np.sin(freq * x)
    y += noise_amp * np.random.randn(len(y))
    return x, y

def plot_data(x, y, Amp, freq, filename):
    """
    Plot the actual data point x, y, along with
    the fit curve Amp * sin(freq * x).
    """
    plb.plot(x, y, 'b', linestyle = ':')
    y_fit = Amp * np.sin(freq * x)
    plb.plot(x, y_fit, 'r')
    plb.savefig(filename)

def fit_data(x, y, fmin_method, init_guess = np.array([0.,0.])):
    """
    Fits data x, y to a sin wave using the fit
    method fmin_method.  Returns the fitted
    amplitude and frequency.

    This is usually unstable so you should plot
    to check if it worked.
    """
    def objective_func(A):
        return sum((y - A[0] * np.sin(A[1] * x))**2)
    return fmin_method(objective_func, init_guess)
