#! /usr/bin/env python

import argparse
import pandas as pd
from multiprocessing import Process


def parse_args():
    """ Define input file arguments. """
    parser = argparse.ArgumentParser(description='Extract left-turn speed data CSV files from Excel')
    parser.add_argument('veh_conflict_data', type=str, help='Excel file with all veh conflicts data')
    #parser.add_argument('ebl', type=str, help='Excel file with east-left speed data')
    #parser.add_argument('sbl', type=str, help='Excel file with south-left speed data')
    #parser.add_argument('wbl', type=str, help='Excel file with west-left speed data')
    return parser.parse_args()

#define function to extract certain ranges from excel sheet and create a .csv file containing this range
def range_2_csv(df, data_range, output_filename):
	start_row, end_row, col_range = data_range	
	start_row = max(0, start_row - 1)
	end_row = max(0, end_row - 1)
	nrows = end_row - start_row
	df = pd.read_excel(spreadsheet, sheet_name=sheet_name, usecols=col_range, skiprows=start_row, nrows=nrows)
	df.to_csv(output_filename, index=False)


def plot_range_to_csv1(df, output_csv, start_row=15, end_row=27,start_col=38, end_col=43):
    """ Extract data from given columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_col (int): First column of range
            end_col (int): Last column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, start_col:end_col]
    data.to_csv(output_csv, index=False,header=None)


def tabular_range_to_csv1(df, output_csv, start_row=15, end_row=19, start_col=4, end_col=22):
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

def extract_conflict_data(xlsx, conflict):
    df = pd.read_excel(xlsx, sheet_name=conflict)
    
    tabular_range_to_csv1(df,conflict + '_tabular_data' + '.csv')
    plot_range_to_csv1(df, conflict + '_plot_data' + '.csv')
    
    

    #title_range_to_csv(df,'Speed_Profiles_page_Titles' + '.csv')

if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()

    # List of input files
    files = [args.veh_conflict_data]

    # List of tabs names present in each input file containing conflict data
    all_types = [['Results_Summary']] 
                #['Speed_Profiles_page_Titles']]
                 #['SBL_Speed'],
                 #['WBL_Speed']]  

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
