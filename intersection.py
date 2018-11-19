#------------------Import-----------------#
import sys
import re
#------------------Import-----------------#

def intersection(a1,b1,a2,b2):
    temp_1=[a1,b1,a2,b2]
    temp_2=set(temp_1)
    if (len(temp_2)==2):
        return "equal"
    elif (len(temp_2)==3):
        cr=(0.0,0.0)
        for element in temp_1:
            if(temp_1.count(element)==2):
                cr=element
        temp_2.remove(cr)
        vertex_list=list(temp_2)
        
        flag = 0
        if(a1[0] == b1[0] == a2[0] == b2[0]):
            flag = 1
        elif(a1[0] != b1[0] and a2[0] != b2[0]):
            p = (a1[1] - b1[1])/(a1[0] - b1[0])
            q = (a2[1] - b2[1])/(a2[0] - b2[0])
            if(p==q):
                flag = 1

        if(flag==1):
            if((cr[0]>vertex_list[0][1] and cr[0]>vertex_list[1][1])
               or (cr[0]<vertex_list[0][1] and cr[0]<vertex_list[1][1])):
                return "equal"
        else:
            ret_X = cr[0]
            ret_Y = cr[1]
            return (ret_X,ret_Y)
            
    else:
        if(a1[0] == b1[0] and a2[0] == b2[0] and b1[0]!=a2[0]):
            return 0
        elif(a1[0] == b1[0] == a2[0] == b2[0]):
            if(a1[1]<a2[1]<b1[1] or b1[1]<a2[1]<a1[1] or a1[1]<b2[1]<b1[1] or b1[1]<b2[1]<a1[1]):
                return "equal"
            else:
                return 0
        elif(a1[0] == b1[0]):
            ret_X = a1[0]
            q = (a2[1] - b2[1])/(a2[0] - b2[0])
            n = a2[1] - (a2[1] - b2[1])/(a2[0] - b2[0]) * a2[0]
            ret_Y = q * ret_X + n             
        elif(a2[0] == b2[0]):        
            ret_X = a2[0]
            p = (a1[1] - b1[1])/(a1[0] - b1[0])
            m = a1[1] - (a1[1] - b1[1])/(a1[0] - b1[0]) * a1[0]
            ret_Y = p * ret_X + m
        else:
            p = (a1[1] - b1[1])/(a1[0] - b1[0])
            m = a1[1] - (a1[1] - b1[1])/(a1[0] - b1[0]) * a1[0]
            q = (a2[1] - b2[1])/(a2[0] - b2[0])
            n = a2[1] - (a2[1] - b2[1])/(a2[0] - b2[0]) * a2[0]
            if(p - q == 0):
                if((a2[1]==p*a2[0]+m and a1[1]<a2[1]<b1[1])
                    or (a2[1]==p*a2[0]+m and b1[1]<a2[1]<a1[1])
                    or (a2[1]==p*a2[0]+m and a1[1]<b2[1]<b1[1])
                    or (a2[1]==p*a2[0]+m and b1[1]<b2[1]<a1[1])):
                    return "equal"
                else:
                    return 0
            else:
                ret_X = (n - m)/(p - q)
                ret_Y = (p * n - q * m)/(p - q)
                

        if( (ret_X > a1[0] and ret_X > b1[0])
            or (ret_X < a1[0] and ret_X < b1[0])
            or (ret_X > a2[0] and ret_X > b2[0])
            or (ret_X < a2[0] and ret_X < b2[0])
            or (ret_Y > a1[1] and ret_Y > b1[1])
            or (ret_Y < a1[1] and ret_Y < b1[1])
            or (ret_Y > a2[1] and ret_Y > b2[1])
            or (ret_Y < a2[1] and ret_Y < b2[1])):
            return 0
        else:
            return (ret_X,ret_Y)