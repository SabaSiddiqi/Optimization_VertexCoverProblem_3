#------------------Import-----------------#
import sys
import re
#------------------Import-----------------#

#------------------Import Functions/Modules-----------------#
from intersection import intersection
#------------------Import Functions/Modules-----------------#


def vertexandedge(out):

    Vertex={}
    Edge=[]
	
    streets=out['S']
    street={}
    for street_idx in streets:
        street[street_idx]=streets[street_idx][:]

    Edge_set=set()
    Vertex_set=set()
    compute=[]

    for street_key_1 in street:
        for street_key_2 in street:
            if(street_key_1 != street_key_2 and  set([street_key_1,street_key_2]) not in compute ):
                compute.append(set([street_key_1,street_key_2]))
                p=0
                q=0
                while(p<len(street[street_key_1])-1):
                    while(q<len(street[street_key_2])-1):
                        intersect = intersection(street[street_key_1][p],street[street_key_1][p+1],street[street_key_2][q],street[street_key_2][q+1])
                        if(intersect != 0 and intersect!="equal"):
                            Vertex_set.update([street[street_key_1][p],street[street_key_1][p+1],street[street_key_2][q],street[street_key_2][q+1],intersect])
                            if(intersect not in street[street_key_1] and intersect not in street[street_key_2]):
                                Edge_set.update([(street[street_key_1][p],intersect),(intersect,street[street_key_1][p+1]),(street[street_key_2][q],intersect),(intersect,street[street_key_2][q+1])])
                                if((street[street_key_1][p],street[street_key_1][p+1]) in Edge_set):
                                    Edge_set.remove((street[street_key_1][p],street[street_key_1][p+1]))
                                if((street[street_key_2][q],street[street_key_2][q+1]) in Edge_set):
                                    Edge_set.remove((street[street_key_2][q],street[street_key_2][q+1]))
                                street[street_key_1].insert(p+1,intersect)
                                street[street_key_2].insert(q+1,intersect)
                                q=q+1
                            elif(intersect in street[street_key_1] and intersect not in street[street_key_2]):
                                Edge_set.update([(street[street_key_2][q],intersect),(intersect,street[street_key_2][q+1])])
                                if((street[street_key_2][q],street[street_key_2][q+1]) in Edge_set):
                                    Edge_set.remove((street[street_key_2][q],street[street_key_2][q+1]))
                                street[street_key_2].insert(q+1,intersect)
                                q=q+1
                            elif(intersect in street[street_key_2] and intersect not in street[street_key_1]):
                                Edge_set.update([(street[street_key_1][p],intersect),(intersect,street[street_key_1][p+1])])
                                if((street[street_key_1][p],street[street_key_1][p+1]) in Edge_set):
                                    Edge_set.remove((street[street_key_1][p],street[street_key_1][p+1]))
                                street[street_key_1].insert(p+1,intersect)
                                q=q+1
                            elif(intersect in street[street_key_1] and intersect in street[street_key_2]):                                
                                Edge_set.update([(street[street_key_1][p],street[street_key_1][p+1]),(street[street_key_2][q],street[street_key_2][q+1])])
                        q=q+1
                    q=0
                    p=p+1

    Vertex_data_1 = list(Vertex_set)
    cnt=0    
    for Vertex_mem in Vertex_data_1:
        cnt=cnt+1
        Vertex[cnt]=Vertex_mem

    Edge_data = list(Edge_set)
    Edge=[]
    for Edge_mem in Edge_data:
        for Vertex_idx in Vertex:
            if(Edge_mem[0]==Vertex[Vertex_idx]):
                a1=Vertex_idx
            if(Edge_mem[1]==Vertex[Vertex_idx]):
                a2=Vertex_idx
        Edge.append((a1,a2))
    
    out['V']=Vertex
    out['E']=Edge

    return out