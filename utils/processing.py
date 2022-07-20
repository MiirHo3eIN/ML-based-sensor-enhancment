import numpy as np 
import scipy 

from scipy import signal 
from scipy.fft import fft, fftfreq 



def fft_(X, fs, axis = 0, vec = False):
		"""
		:param  x:  	array-like - Input Array 
		:param fs: 		int - Input Sampling Frequency 
		:param axis: 	int, optional - Axis over which to compute FFT, default = 0.  
		:param vec:		True if the input is (MxN matrix), False if the input is (1xN) matrix
		:return: 		Dictionary - frequency and fft amplitude values.  
		"""

		N = np.array(X).shape[0] 
		T = 1.0 / fs 

		# Compute fft 
		yf = (fft(X, axis = axis)) 
		# Skip C0 coefficient
		if vec == False: 
			yf_trim = 2.0/N * np.abs(yf[1:(N//2)])
			# Compute the Phase
			yf_phase = np.angle(yf[0:N//2])

		elif vec == True:	
			yf_trim = 2.0/N * np.abs(yf[1:(N//2), :])
			# Compute the Phase
			yf_phase = np.angle(yf[0:N//2, :])
		# Frequency range 
		xf = fftfreq(N, T)[1:N//2] 
		fft_ = {
				'frequency': xf, 
				'fft_': yf_trim
			}
		return fft_

def mean_center(df, loc = []):
	for ax in loc: 
		df[ax] = df[ax].values - np.mean(df[ax].values)

def g_conversion(df): 
	conv = 1/(2**15) 
	df['x'] = df.x.values*conv
	df['y'] = df.y.values*conv
