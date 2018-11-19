#------------------Import-----------------#
import re
#------------------Import-----------------#

# Notes:
# -?[0-9]+ --> for -ve and positive numbers, \d+ --> for positive numbers
# \s* --> for spaces if any

#street_name_format = '\"\s*([a-zA-Z]\s*)+\s*\"'
street_name_format = '\".+\"'
coor_format = '\(\s*-?[0-9]+\s*,\s*-?[0-9]+\s*\)'

#add format - a "Street Name" coordinates
add_format = '\s*[a]\s*' + street_name_format + '\s*('+coor_format +'\s*){2,}\s*$'
add_compile = re.compile(add_format)

#change format - c "Street Name" coordinates  
change_format = '\s*[c]\s*' + street_name_format + '\s*('+coor_format +'\s*){2,}\s*$' 
change_compile = re.compile(change_format)

#remove format - r "Street name" 
remove_format = '\s*[r]\s*' + street_name_format + '\s*$' 
remove_compile = re.compile(remove_format)

#vertexandedge format  - g
graph_format = '\s*[g]\s*$' 
graph_compile = re.compile(graph_format)


def reg_exp(input_command):
    add_match=add_compile.match(input_command)
    change_match=change_compile.match(input_command)
    remove_match=remove_compile.match(input_command)
    graph_match=graph_compile.match(input_command)
    return add_match,change_match,remove_match,graph_match