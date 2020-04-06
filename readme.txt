Generate image for all graphs from csv files, created by Ruopu Zhang

library required:
plotly
pandas 0.24.2: pip3 install pandas==0.24.2
orca: https://plot.ly/python/static-image-export/

To run the program:
python user_input_config.py

Two varibles need to be changed for each report :
1. csv folder location (file input)
2. image file save location (file out put)


In user_input_config.py, threr are 4 main pages, including:
1. veh speed distribution page
2. veh/cyc/ped conflicts page
3. veh Speed Profiles by Intersection Approach page
4. veh/cyc/ped detail page


comment out the rest of the code if you want to test specific pages


