#!/usr/bin/python

#------------------Import-----------------#
import sys
import re
#------------------Import-----------------#

#------------------Import Functions/Modules-----------------#
from vertexandedge import vertexandedge
from intersection import intersection
from display_graph import display
#------------------Import Functions/Modules-----------------#


def add_street(out,street_name,street_line):
    s_out=out['S']
    s_out[street_name]=[]
    for i in range(0,len(street_line)-1,2):
        s_out[street_name].append((float(street_line[i]),float(street_line[i+1])))
    out['S']=s_out
    return out

def remove_street(out,street_name):
    s_del=out['S']        
    del s_del[street_name]
    return out

out={'V':{},'E':[],'S':{}}

while(1):
    street=out['S']
    try:
        input_command = raw_input()
    except EOFError:
        break
        
    cmd = re.match(r'^\s*(\w)\s*"(.*)"(.*)$', input_command)
    cmdg = re.match(r'^\s*(g)\s*$', input_command)
    if cmd:
        command = cmd.group(1)
        street_input = re.match(r'[acrg]$',command)
        if not street_input:
            continue
        
        if(command=='a' or command=='c' or command=='r'):
            street_name = re.match(r'^\s*$',cmd.group(2))
            if street_name:
                continue
            if(command=='a' and (cmd.group(2) in street.keys())):
                continue
            if(command=='c' and (cmd.group(2) not in street.keys())):
                continue
            if(command=='r' and (cmd.group(2) not in street.keys())):
                continue
                        
        if(command=='a' or command=='c'):
            street_line = re.match(r'(\s*\(\s*-?\d+\s*,\s*-?\d+\s*\)\s*)*$',cmd.group(3))
            if street_line:
                temp = re.compile(r'-?\d+')
                street_line_list = temp.findall(cmd.group(3))
                if(len(street_line_list)==0):
                    continue
                if(len(street_line_list)==2):
                    continue

            else:
                continue
            
        if(command=='r'):
            street_line = re.match(r'^\s*$',cmd.group(3))
            if not street_line:
                continue
                
        
        if(command=='a'):
            out=add_street(out,cmd.group(2),street_line_list)
            out=vertexandedge(out)
        elif(command=='c'):
            out=remove_street(out,cmd.group(2))
            out=add_street(out,cmd.group(2),street_line_list)
            out=vertexandedge(out)
        elif(command=='r'):
            out=remove_street(out,cmd.group(2))
            out=vertexandedge(out)
    elif cmdg:
        display(out)
    else:
        sys.stderr.write("")