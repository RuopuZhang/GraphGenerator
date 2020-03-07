#! /usr/bin/env python

import argparse
import pandas as pd
from multiprocessing import Process


def parse_args():
    """ Define input file arguments. """
    parser = argparse.ArgumentParser(description='Extract left-turn speed data CSV files from Excel')
    parser.add_argument('speed_data', type=str, help='Excel file with all left turn speed summary data')
    #parser.add_argument('ebl', type=str, help='Excel file with east-left speed data')
    #parser.add_argument('sbl', type=str, help='Excel file with south-left speed data')
    #parser.add_argument('wbl', type=str, help='Excel file with west-left speed data')
    return parser.parse_args()


def plot_range_to_csv(df, output_csv, start_row=0, end_row=101,start_col=10, end_col=18):
    """ Extract data from given columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_col (int): First column of range
            end_col (int): Last column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, start_col:end_col]
    data.to_csv(output_csv, index=False)


def tabular_range_to_csv(df, output_csv, start_row=0, end_row=5, start_col=32, end_col=34):
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

def plot_range_to_csv1(df, output_csv, start_row=9, end_row=13,start_col=13, end_col=18):
    """ Extract data from given columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_col (int): First column of range
            end_col (int): Last column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, start_col:end_col]
    data.to_csv(output_csv, index=False,header=None)


def tabular_range_to_csv1(df, output_csv, start_row=9, end_row=13, start_col=5, end_col=12):
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
    tabular_range_to_csv(df, conflict + '_tabular_data' + '.csv')
    plot_range_to_csv(df, conflict + '_plot_data' + '.csv')
    tabular_range_to_csv1(df, conflict + '_Summary_tabular_data' + '.csv')
    plot_range_to_csv1(df, conflict + '_Summary_plot_data' + '.csv')
    #title_range_to_csv(df,'Speed_Profiles_page_Titles' + '.csv')

if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()

    # List of input files
    files = [args.speed_data]

    # List of tabs names present in each input file containing conflict data
    all_types = [['EBL_Speed','WBL_Speed', 'NBL_Speed', 'SBL_Speed','Speed_Summary']] 
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
