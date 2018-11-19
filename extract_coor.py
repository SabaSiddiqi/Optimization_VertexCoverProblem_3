#------------------Import-----------------#
import re
#------------------Import-----------------#

# Notes:
# -?[0-9]+ --> for -ve and positive numbers, \d+ --> for positive numbers
# \s* --> for spaces if any

coor_format = '\(\s*-?[0-9]+\s*,\s*-?[0-9]+\s*\)'
tuple_coor=[]
coor=[]

def extract_coor(input_command):
    #initiate to store coordinates
    tuple_coor=[]
    #extract coordinates form input
    for coor in re.findall(coor_format,input_command):
        #find numbers in coordinates and convert to int
        y=[float(x) for x in re.findall('-?[0-9]+',coor)]
        #convert each pair of numbers to tuple
        tuple_coor.append(tuple(y))
        
    return tuple_coor