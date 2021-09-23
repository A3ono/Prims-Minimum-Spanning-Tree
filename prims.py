//Alexandra Medina

import Weighted_Graph as wg
import prims_functions as pf

def Prims(textfile):
    G = wg.Weighted_Graph(textfile)
    E = G.edge_set()
    V = G.vertex.set()
    
    graph = []
    for e in E:
        edge = [e[0], e[1], G.edge_dict() [e]]
        graph.append(edge)
        
    MST = pf.findMinimalGraph(len(V), graph)
    
    print
    for each in MST:
        print (each)
        
