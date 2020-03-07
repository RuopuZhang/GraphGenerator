#! /usr/bin/env python
# updated Jan 2020 by Ruopu, each cell will generate a csv file now
import argparse
import pandas as pd
from multiprocessing import Process
import os

def parse_args():
    """ Define input file arguments. """
    parser = argparse.ArgumentParser(description='Extract veh conflicts data summary CSV files from Excel')
    parser.add_argument('title_pages', type=str, help='Excel file with all speed profile and veh/cyc/ped conflicts pages titles')
    #parser.add_argument('ebl', type=str, help='Excel file with east-left speed data')
    #parser.add_argument('sbl', type=str, help='Excel file with south-left speed data')
    #parser.add_argument('wbl', type=str, help='Excel file with west-left speed data')
    return parser.parse_args()


def speed_title_range_to_csv(df, output_csv, col_number, start_row=70, end_row=70):
    """ Extract data from given range specified by start/end rows and
    columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_row (int): First row of range
            end_row (int): Last row of range
            col_number (int): current column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, col_number:col_number+1]
    data.to_csv(output_csv, index=False, header=None)

def veh_title_range_to_csv(df, output_csv, col_number, start_row=72, end_row=72):#12
    """ Extract data from given range specified by start/end rows and
    columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_row (int): First row of range
            end_row (int): Last row of range
            col_number (int): current column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, col_number:col_number+1]
    data.to_csv(output_csv, index=False, header=None)

def cyc_title_range_to_csv(df, output_csv, col_number, start_row=74, end_row=74): #16
    """ Extract data from given range specified by start/end rows and
    columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_row (int): First row of range
            end_row (int): Last row of range
            col_number (int): current column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, col_number:col_number+1]
    data.to_csv(output_csv, index=False, header=None)

def ped_title_range_to_csv(df, output_csv, col_number, start_row=76, end_row=76): #16
    """ Extract data from given range specified by start/end rows and
    columns.

    Args:
            df (DataFrame): The excel sheet from read_excel
            start_row (int): First row of range
            end_row (int): Last row of range
            col_number (int): current column of range
            output_csv (str): CSV file to write data
    """
    data = df.ix[start_row:end_row, col_number:col_number+1]
    data.to_csv(output_csv, index=False, header=None)


def extract_conflict_data(xlsx, conflict):
    df = pd.read_excel(xlsx, sheet_name=conflict)
    for i in range(0,4):
        speed_title_range_to_csv(df,'Speed_Profiles_page_Titles{}.csv'.format(i+1),i)
    for j in range(0,12):    
        veh_title_range_to_csv(df, 'Detail_Conflict_page_Titles{}.csv'.format(j+1),j)
    for k in range(0,16):
        cyc_title_range_to_csv(df, 'Cyclist_page_titles{}.csv'.format(k+1),k)
        ped_title_range_to_csv(df, 'Pedestrian_page_titles{}.csv'.format(k+1),k)	


if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()

    # List of input files
    files = [args.title_pages]

    # List of tabs names present in each input file containing conflict data
    all_types = [['Site_1']]  
                # ['EBL_Speed'],
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
