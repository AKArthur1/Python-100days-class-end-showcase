### Project 02 - Webscrapper to CSV 01 - Red Camera Tech Specs ###
from os import write

import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
import lxml


CSV_COMPARISON_TITLE = 'Red Camera Comparison'

### functions into separate files

    # build tool to run at first to generate each product/"camera" tech info weblinks and format them into lists
    # csv creation file
    # api requests file that pulls from main code file website execution
    # csv writing and data processing
    # csv product comparison csv collection breaking out every row into it's own csv that updates everytime it's run to stay current on products
    # modern data scientist common functions/calculations to be run to showcase data. ex make list from interviews and youtube day in my life and google lists on most common
    # modern Data viz library that passes through matplot etc and outputs a cleaner data vis window
            #should this be webapp or pop up window?

# keep this main file clean and clear


### BLANK ### ---------------------------------------------------------------------------------------------

response_home_link = requests.get('https://www.red.com/')
red_camera_webpage = response_home_link.text
# print(home_link_response.text)

soup_home_link = BeautifulSoup(red_camera_webpage, 'html.parser')
# print(soup_home_link.title)
camera_list_tag = soup_home_link.find(name='ul', class_ ='header-nav__submenu')
# print(camera_list_tag.prettify())


CAM_LIST = []
for x in camera_list_tag:
    textname = x.text
    CAM_LIST.append(textname)
print(CAM_LIST)

# tech_specs_categories = [for categories in soup_techspecs_link.find_all(name='BLANK', class_='BLANK')]

### Create Camera List .txt file ### ---------------------------------------------------------------------------------------------
with open('Red_Camera_Names.txt', mode='w') as CamList:
    CamList.write(str(CAM_LIST))
### Create Camera List .txt file ### ---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
### Reset CSV to blank ### ---------------------------------------------------------------------------------------------
with open('comparison_RED_CAMERAS.csv', mode='w') as clear_file:
    clear_file.flush()
    clear_file.close()
### Reset CSV to blank ### ---------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
### Add Comparison_CSV Title ### ---------------------------------------------------------------------------------------------
with open('comparison_RED_CAMERAS.csv', mode='a') as add_title:
    add_title.write(CSV_COMPARISON_TITLE)
### Add Comparison_CSV Title ### ---------------------------------------------------------------------------------------------

# FINAL_DICTIONARY = {index: value for index, value in enumerate(CAM_LIST: CAM_LIST)}
# FINAL_DICTIONARY = {}

from collections import defaultdict

out = defaultdict(dict)

# with open('file.txt', mode='w') as FINAL_DICTIONARY:
#     # for line in f:
#     for line in FINAL_DICTIONARY:
#         # typ,name,price = line.split(';')
#         out[CAM_LIST][CAM_LIST] = 0

dict(out)
print(str(out))


with open('comparison_RED_CAMERAS.csv', mode='a', newline='') as FinalConstructor:
    final = csv.writer(FinalConstructor)
    final.writerow('')
    final.writerow(CAM_LIST)







#
# FINAL_CONSTRUCTOR = pd.DataFrame(CAM_LIST)
# print(FINAL_CONSTRUCTOR)
# print(CAM_LIST)
# with open('comparison_RED_CAMERAS.csv', mode='a') as constructor:
#     constructor.write(str(FINAL_CONSTRUCTOR))



# df_CAM_LIST.to_csv('comparison_RED_CAMERAS.csv',mode='a')










#
# test_camera_table = pd.read_csv('test_camera_table.csv')
# print(test_camera_table['camera_name'])
#
#
#
# # opening and reading html
# with open('camera_test_Techspec.html') as camera_test_HTML:
#     Camera_test_contents = camera_test_HTML.read()
#
# soup = BeautifulSoup(Camera_test_contents, 'html.parser')
#
# print(soup.title.string)
# print(soup.prettify())
# print(soup.h2)
#
#
#
#
#
