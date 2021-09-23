//Alexandra Medina

import Weighted_Graph as wg
import Prims_Prof_Functions as pf

G=wg.Weighted_Graph("Text.txt")
G.draw_graph()

def Prims(textfile, start_vertex = 0, cost = False):
    
    E = G.edge_set()
    V = G.vertex_set()          

    while T[0] != G.vertex_set():
        update_tree(G, T)
        
    return T

