# Set of classes and functions to convert binary values to float32.np vals

import numpy as np 
import pandas as pd 
from decimal import Decimal

# Binary to int 16 
uint16_t_vec = lambda x: [int(i, 16) for i in x]

# Unsigned integer to signed integer 
int16_t_vec = lambda x: [-(i&0x8000) | (i&0x7fff) for i in x]



# Binary to int 16 
uint16_t_scalar = lambda x: int(x, 16) 

# Unsigned integer to signed integer 
int16_t_scalar = lambda x: -(x&0x8000) | (x&0x7fff)

#convert .txt to pandas df 

def from_txt_to_csv(loaded_txt, label, log_num): 
	
	x,y = [] , []
	cond, logs_num, ts = [], [], []
	ts_counter = 0
	for line in range(0, len(loaded_txt)): 

		#x_temp = loaded_txt[line][3:7]
		#y_temp = loaded_txt[line][10:14]
		logs_temp = str(log_num)   
		logs_float = float(logs_temp)
		
		x_temp = (int16_t_scalar(uint16_t_scalar(loaded_txt[line][3:7])))
		y_temp = (int16_t_scalar(uint16_t_scalar(loaded_txt[line][10:14])))

		x = np.append(x, x_temp)
		y = np.append(y, y_temp) 
		cond = np.append(cond, label)
		  

		logs_num = np.append(logs_num, logs_float)
		ts = np.append(ts, ts_counter)

		ts_counter += 0.01
		
	out = {'x':x,
			'y':y, 
			'cond':cond, 
			'logger': logs_num, 
			'ts': ts}

	return pd.DataFrame.from_dict(out)

# generate looger numbers based on the format you want 
def logger(file_num, format):

	"""
	:params num_files: 	Total number of files to read
	:params format:		Foramt of the files to read
	:yields logger:		proper names to read the line

	"""

	if file_num < 10: 
		return "LOG000" + str(file_num) + format
	 
	return "LOG00" + str(file_num) + format


def read_txt(path, label, log_num, format = '.TXT'):
	
	logger_path = logger(log_num, format)  
	read_path = path + logger_path  
	print(read_path)
	with open(read_path) as f:
		lines = f.readlines()
		return from_txt_to_csv(lines, label, log_num)

 

#convert df to .csv format

def from_df_to_csv(df, path, log_num, foramt = '.csv'):
	print(log_num)
	log = logger(file_num = int(log_num), format = foramt)
	df.to_csv(path+log, header = True, index = False)


# Use load (.dat) to df
def read_dat(path, num_file = 1):
    if num_file == 1:
        return pd.DataFrame(np.loadtxt(path,  unpack = True).T , columns=['Ts', 'N.A', 'Velocity', 'CH0', 'CH1'])
    return [np.loadtxt(f,  unpack = True) for f in glob.glob(path + "*.dat")]
    