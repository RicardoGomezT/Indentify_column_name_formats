import pandas as pd

file_format = 'parquet' #'txt', 'csv', 'parquet'
path_csv = 'input/'
path_txt = 'input/'
path_parquet = 'input/userdata1.parquet'

def txt_identify_column():
    print("[INFO] Identify on txt")

def cvs_identify_column():
    print("[INFO] Identify on csv")

def parquet_identify_column():
    print("[INFO] Identify on parquet")
    dataset_parquet = pd.read_parquet(path_parquet, engine='pyarrow')
    print("[INFO]\n", dataset_parquet)

def error():
	print('[INFO] Error, unsupported file format')

switch_format = {
	'txt': txt_identify_column,
	'csv': cvs_identify_column,
	'parquet': parquet_identify_column
}

switch_format.get(file_format, error)()

print ("\n\n[INFO] End proccessing")