#! /usr/bin/env python

import argparse
import pandas as pd
from multiprocessing import Process


def parse_args():
    """ Define input file arguments. """
    parser = argparse.ArgumentParser(description='Extract left-turn speed data CSV files from Excel')
    parser.add_argument('veh_conflict_data', type=str, help='Excel file with all veh conflicts data')
    return parser.parse_args()

#define function to extract certain ranges from excel sheet and create a .csv file containing this range
def range_2_csv(df, data_range, output_filename):
	start_row, end_row, col_range = data_range	
	start_row = max(0, start_row - 1)
	end_row = max(0, end_row - 1)
	nrows = end_row - start_row
	df = pd.read_excel(spreadsheet, sheet_name=sheet_name, usecols=col_range, skiprows=start_row, nrows=nrows)
	df.to_csv(output_filename, index=False)

def plot_range_to_csv(df, output_csv, start_col=15, end_col=27):
	""" Extract data from given columns where first column is not empty.
	
	Args:
		df (DataFrame): The excel sheet from read_excel
		start_col (int): First column of range
		end_col (int): Last column of range
		output_csv (str): CSV file to write data
	"""
	non_empty_rows = df.ix[:, 0].notna()
	data = df[non_empty_rows].ix[:, start_col:end_col]
	data.to_csv(output_csv, index=False)
	
def tabular_range_to_csv(df, output_csv, start_row=10, end_row=14, start_col=71, end_col=77):
    """ Extract data from given range specified by start/end rows and
    columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_row (int): First row of range
            end_row (int): Last row of range
            start_col (int): First column of range
            end_col (int): Last column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, start_col:end_col]
    data.to_csv(output_csv, index=False, header=None)

def temporal_range_to_csv(df, output_csv, start_row=0, end_row=24, start_col=38, end_col=43):
    """ Extract data from given columns where first column is not empty.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_col (int): First column of range
            end_col (int): Last column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, start_col:end_col]
    data.to_csv(output_csv, index=False)

def extract_conflict_data(xlsx, conflict):
    df = pd.read_excel(xlsx, sheet_name=conflict)
    temporal_range_to_csv(df, conflict + '_temporal_plot_data' + '.csv')	
    tabular_range_to_csv(df, conflict + '_tabular_data' + '.csv')
    plot_range_to_csv(df, conflict + '_plot_data' + '.csv')

if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()

    # List of input files
    files = [args.veh_conflict_data]

    # List of tabs names present in each input file containing conflict data
    all_types = [['nbl_vs_sbt','ebl_vs_wbt','sbl_vs_nbt', 'wbl_vs_ebt','nbt_vs_ebt','sbt_vs_ebt','sbt_vs_wbt', 'nbt_vs_wbt', 'nbl_vs_ebt','ebl_vs_sbt','sbl_vs_wbt','wbl_vs_nbt']] 
        
    # Create one process for each conflict configuration
    processes = []
    for xlsx, conflict_types in zip(files, all_types):
        for conflict in conflict_types:
            name = '%s %s' % (xlsx, conflict)
            print('Launching process for', name)
            p = Process(target=extract_conflict_data, args=(xlsx, conflict), name=name)
            p.start()
            processes.append(p)

    # Wait for processes to terminate
    for p in processes:
        print('Waiting for', p.name)
        p.join()
