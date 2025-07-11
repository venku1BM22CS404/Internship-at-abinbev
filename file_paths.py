# file_paths.py
import os
from datetime import datetime

run_time = datetime.now()
run_time_naive = run_time.replace(tzinfo=None)
run_date = run_time_naive.date()

month_folder = f"{run_date.month:02d}. {run_date.strftime('%B')} {run_date.year}/"
date_str = run_date.strftime('%d_%m_%Y ')

# Input data storage location
data_filepath = f'./Input_Data/{month_folder}{date_str[:-1]}/{run_time.strftime("%Y_%m_%d_%H_%M_%S")} input data/'
if not os.path.exists(data_filepath):
    os.makedirs(data_filepath)

# Static file storage location
static_filepath = './Static_data/'

# Preprocessed data location
preprocessed_path = f'./PRE_PROCESSED_DATA/{month_folder}{date_str}preprocessed data/{run_time.strftime("%Y_%m_%d_%H_%M_%S")} preprocessed data/'
if not os.path.exists(preprocessed_path):
    os.makedirs(preprocessed_path)

# Results storage location
result_path = f'./RESULTS/{month_folder}{date_str}results/'
if not os.path.exists(result_path):
    os.makedirs(result_path)

result_path = f'{result_path}{run_date.strftime("%Y_%m_%d")}_'

#save the variables to a file
with open('location_variables.txt', 'w') as f:
    f.write('data_filepath = "' + data_filepath + '" \n')
    f.write('static_filepath = "' + static_filepath + '" \n')
    f.write('preprocessed_path = "' + preprocessed_path + '" \n')
    f.write('result_path = "' + result_path + '" \n')
    f.write('run_date = "' + run_date.strftime("%Y-%m-%d %H:%M:%S") + '" \n')
    f.write('run_time_naive = "' + run_time_naive.strftime("%Y-%m-%d %H:%M:%S") + '" \n')
    f.write('run_time = "' + run_time.strftime("%Y-%m-%d %H:%M:%S") + '" \n')