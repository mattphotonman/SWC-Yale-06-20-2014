"""
Main script for fitting a sine wave.
"""
import fitting_sine_wave as fsw
from scipy import optimize

x, y = fsw.generate_data(1.,1.,0.01)
Amp_fit, freq_fit = fsw.fit_data(x, y, optimize.fmin,
                                 init_guess = np.array([0.9,0.9]))
fsw.plot_data(x, y, Amp_fit, freq_fit, filename = 'plot_result')
