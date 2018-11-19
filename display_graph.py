#------------------Import-----------------#
import sys
import re
#------------------Import-----------------#

def display(output):

    Vertex=output['V']
    Edge=output['E']

    Vertex_copy = Vertex.copy()
    Edge_copy = []
    cnt =0
    for Vertex_idx in Vertex:
        Vertex_copy[Vertex_idx]=cnt;
        cnt=cnt+1

    for Edge_mem in Edge:
        Edge_copy.append((Vertex_copy[Edge_mem[0]],Vertex_copy[Edge_mem[1]]))
    
    print ('V '+str(len(Vertex)))
    sys.stdout.write("E {")
    for num in range(len(Edge_copy)):
        if(num<len(Edge_copy)-1):
            sys.stdout.write("<"+str(Edge_copy[num][0])+","+str(Edge_copy[num][1])+">,")
        else:
            sys.stdout.write("<"+str(Edge_copy[num][0])+","+str(Edge_copy[num][1])+">")
    print ("}")

    sys.stdout.flush()
    