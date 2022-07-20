# This Script Converting TXT (binary values) to CSV (Integer) files

import utils_adder

import numpy as np 
import pandas as pd 



import data_convertor, processing 





def main(): 
	
	print("Starting the Main functuion")
	berkly_tab = pd.read_csv('../data/data_berkley.csv')
	print(berkly_tab.head())

	
	for i in range(0, len(berkly_tab.path)):
    	print(f'Converting {berkly_tab.names[i]}\n')
	    
	    src_path = berkly_tab.path[i]
	    logs = berkly_tab.logs_num[i]
	    tag = berkly_tab.label[i]
	    
	    for j in range(0,logs+1):
	        logger = j
	        l_df = data_convertor.read_txt(path=src_path, label= tag, log_num = logger)
	        data_convertor.from_df_to_csv(l_df, src_path, logger)

	    print(f'{berkly_tab.names[i]} Converted Successfully!\n')


if __name__ == "__main__":
	
	print("*************************************************************")
	print("****************** TXT to CSV LOGGER ************************")
	print("*************************************************************") 
	

	main()