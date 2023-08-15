import pandas as pd
import sys

input_file = sys.argv[1]
database_file = sys.argv[2]
output_file = sys.argv[3]
# read csv file : database
database = pd.read_csv(database_file,sep='\t')
# rename columns in database
database.rename(columns={database.columns[1]: 'REF'},inplace=True)
database.rename(columns={database.columns[2]: 'ALT'},inplace=True)
database.rename(columns={database.columns[6]: 'CHROM'},inplace=True)
database.rename(columns={database.columns[7]: 'POS'},inplace=True)
database.rename(columns={database.columns[8]: 'SYMBOL'},inplace=True)
#read csv file : input
input = pd.read_csv(input_file,sep='\t')

# list of common columns to use for merge ['REF','ALT','CHROM','POS','SYMBOL']
df = pd.merge(database, input, on = ['REF','ALT','CHROM','POS','SYMBOL'])

# export results
df.to_csv(output_file)
