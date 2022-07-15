import numpy as np 
import scipy 

from scipy import signal 
from scipy.fft import fft, fftfreq 



def fft(X, fs, axis = 0):
		"""
		:param  x:  	array-like - Input Array 
		:param fs: 		int - Input Sampling Frequency 
		:param axis: 	int, optional - Axis over which to compute FFT, default = 0.  
		:return: 		Dictionary - frequency and fft amplitude values.  
		"""

		N = np.array(x).shape[0] 
		T = 1.0 / fs 

		# Compute fft 
		yf = (fft(input_array, axis = axis)) 
		# Skip C0 coefficient
		yf_trim = 2.0/N * np.abs(yf[1:(N//2), :])
		# Compute the Phase
		yf_phase = np.angle(yf[0:N//2, :])
		# Frequency range 
		xf = fftfreq(N, T)[1:N//2] 
		fft_ = {
				'frequency': xf, 
				'fft_phase': yf_trim
			}
		return fft_