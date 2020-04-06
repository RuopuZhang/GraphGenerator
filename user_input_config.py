"""
created by Ruopu Zhang, Jan 2020.
The program will take csv files as input, output images for generating the report
Three things need to changes for each report: csv file directory, image file output location, and number of pages/tables for different type of pages
"""

import os
import sys
from Veh_Speed_Distribution import *
from detail_page import *
from conflicts_page import *
from Veh_Speed_Profiles_by_Intersection_Approach import *
from fnmatch import fnmatch



####csv folder lcoation####
csv_folder_location = '/home/rico/Desktop/Rico test/'

####image folder location
image_folder_location = '/home/rico/Desktop/image-test'


##subfolders###
for entry in os.listdir(csv_folder_location):
    if os.path.isdir(os.path.join(csv_folder_location, entry)):
    	if 'CYC' in entry:
    		cyc_conflict_data = csv_folder_location+entry
    	if 'VEH' in entry:
    		veh_conflict_data = csv_folder_location+entry
    	if 'PED' in entry:
    		ped_conflict_data = csv_folder_location+entry
    	if 'SPEED' in entry:
    		speed_profile_data = csv_folder_location+entry




###detail page ###
def detail_page(conflict_data,image_folder_location,page_type):
	#image file location
	DetailPage_Bar_Image_Directory = '{}/{}_detail_bar'.format(image_folder_location, page_type)
	DetailPage_Scatter_Image_Directory = '{}/{}_detail_scatter'.format(image_folder_location, page_type)
	DetailPage_Table_Image_Directory = '{}/{}_detail_table'.format(image_folder_location, page_type)

	detail_pattern_bar = "temp_plot_data*.csv"
	detail_pattern_scatter = "plot_data*.csv"
	detail_pattern_table = "tabular*.csv"

	pattern_bar_list=[]
	pattern_scatter_list=[]
	pattern_table_list=[]

	for path, subdirs, files in os.walk(conflict_data):
	    for name in files:
	        if fnmatch(name, detail_pattern_bar):
	        	pattern_bar_list.append(os.path.join(path, name))
	        if fnmatch(name, detail_pattern_scatter):
	        	pattern_scatter_list.append(os.path.join(path, name))	
	        if fnmatch(name, detail_pattern_table):
	        	pattern_table_list.append(os.path.join(path, name))
	if page_type == 'veh':
		Veh_detail_page(
			pattern_bar_list, pattern_scatter_list, pattern_table_list,
			DetailPage_Bar_Image_Directory,
			DetailPage_Scatter_Image_Directory,
			DetailPage_Table_Image_Directory
			)
	if page_type == 'cyc':
		Cyc_detail_page(
			pattern_bar_list, pattern_scatter_list, pattern_table_list,
			DetailPage_Bar_Image_Directory,
			DetailPage_Scatter_Image_Directory,
			DetailPage_Table_Image_Directory
			)
	if page_type == 'ped':
		Ped_detail_page(
			pattern_bar_list, pattern_scatter_list, pattern_table_list,
			DetailPage_Bar_Image_Directory,
			DetailPage_Scatter_Image_Directory,
			DetailPage_Table_Image_Directory
			)


### conflict page ###
def conflict_page(conflict_data,image_folder_location,page_type):
	#image file location
	DetailPage_Bar_Image_Directory = '{}/summary_{}_conflict_bar'.format(image_folder_location, page_type)
	DetailPage_Table_Image_Directory = '{}/summary_{}_conflict_table'.format(image_folder_location, page_type)

	detail_pattern_bar = "plot_data.csv"
	detail_pattern_table = "tab_data*.csv"

	pattern_bar_list=[]
	pattern_table_list=[]

	for path, subdirs, files in os.walk(conflict_data):
	    for name in files:
	        if fnmatch(name, detail_pattern_bar):
	        	pattern_bar_list.append(os.path.join(path, name))	
	        if fnmatch(name, detail_pattern_table):
	        	pattern_table_list.append(os.path.join(path, name))
	if page_type == 'veh':
		Veh_Conflicts(
			pattern_bar_list, pattern_table_list,
			DetailPage_Bar_Image_Directory,
			DetailPage_Table_Image_Directory
			)
	if page_type == 'cyc':
		Cyc_Conflicts(
			pattern_bar_list, pattern_table_list,
			DetailPage_Bar_Image_Directory,
			DetailPage_Table_Image_Directory
			)
	if page_type == 'ped':
		Ped_Conflicts(
			pattern_bar_list, pattern_table_list,
			DetailPage_Bar_Image_Directory,
			DetailPage_Table_Image_Directory
			)


### veh speed distributio n###
def speed_dist_page(speed_profile_data,image_folder_location):
	#image file location
    VehSpeedDistPage_Bar_Image_Directory = '{}/summary_veh_speed_bar'.format(image_folder_location)
    VehSpeedDistPage_Table_Image_Directory = '{}/summary_veh_speed_table'.format(image_folder_location)

    detail_pattern_bar = "Speed_Summary_Summary_plot_data.csv"
    detail_pattern_table = "Speed_Summary_Summary_tabular_data.csv"
    pattern_bar_dir=''
    pattern_table_dir=''

    for path, subdirs, files in os.walk(speed_profile_data):
	    for name in files:
	        if fnmatch(name, detail_pattern_bar):
	        	pattern_bar_dir = os.path.join(path, name)
	        if fnmatch(name, detail_pattern_table):
	        	pattern_table_dir = os.path.join(path, name)
    Veh_Speed_Dist(pattern_bar_dir, pattern_table_dir, VehSpeedDistPage_Bar_Image_Directory, VehSpeedDistPage_Table_Image_Directory)


###Vehicles Speed Profiles by Intersection Approach page###
def speed_profile_page(speed_profile_data,image_folder_location):
	#image file location
    VehSpeedByIntAppr_Table_Image_Directory = '{}/veh_speed_profile_table'.format(image_folder_location)
    VehSpeedByIntAppr_Scatter_Image_Directory = '{}/veh_speed_profile_scatter'.format(image_folder_location)
    VehSpeedByIntAppr_Bar_Image_Directory = '{}/veh_speed_profile_bar'.format(image_folder_location)

    detail_pattern_table = "tab_data*.csv"
    detail_pattern_scatter = "plot_data*.csv"
    detail_pattern_bar = "plot_data*.csv"
	
    pattern_table_list = []
    pattern_scatter_list = []
    pattern_bar_list = []
	

    for path, subdirs, files in os.walk(speed_profile_data):
	    for name in files:
	        if fnmatch(name, detail_pattern_bar):
	        	pattern_bar_list.append(os.path.join(path, name))	
	        if fnmatch(name, detail_pattern_table):
	        	pattern_table_list.append(os.path.join(path, name))
	        if fnmatch(name, detail_pattern_scatter):
	        	pattern_scatter_list.append(os.path.join(path, name))

    Veh_speed_Profiles_by_Intersection_App(
		pattern_table_list, pattern_scatter_list, pattern_bar_list,
		VehSpeedByIntAppr_Table_Image_Directory,
		VehSpeedByIntAppr_Scatter_Image_Directory,
		VehSpeedByIntAppr_Bar_Image_Directory
		)


# ######end of Vehicles Speed Profiles by Intersection Approach page#########

#execute
detail_page(veh_conflict_data,image_folder_location, 'veh')
# detail_page(cyc_conflict_data,image_folder_location, 'cyc')
# detail_page(ped_conflict_data,image_folder_location, 'ped')

# conflict_page(veh_conflict_data,image_folder_location,'veh')
# conflict_page(cyc_conflict_data,image_folder_location,'cyc')
# conflict_page(ped_conflict_data,image_folder_location,'ped')

# speed_dist_page(speed_profile_data, image_folder_location)

# speed_profile_page(speed_profile_data,image_folder_location)



