# Set of classes and functions to convert binary values to float32.np vals

import numpy as np 
import pandas as pd 


# Binary to int 16 
uint16_t = lambda x: [int(i, 16) for i in x]

# Unsigned integer to signed integer 
int16_t = lambda x: [-(i&0x8000) | (i&0x7fff) for i in x]




#convert .txt to .csv 

def from_txt_to_csv(): 
	x,y = [] 

	for line in range(0, len(lines)): 

		x_temp = lines[line][3:7]
		y_temp = lines[line][10:14]

		x = np.append(x, x_temp)
		y = np.append(y, y_temp) 

		