// Alexandra Medina

print (" ")
print ("Prim's MST Algorithm Graph: ")
print (" ")

import Weighted_Graph as wg
G=wg.Weighted_Graph("sample.txt")
G.draw_graph()

E = G.edge_set()           
V = G.vertex_set()

print (" ")
print ("Prim's MST Algorithm Iterations: ")
print (" ")

def cost(e):                   
    return G.edge_dict()[e]

V_T = {0}
E_T = []
T = (V_T, E_T)

def valid_edges(T):
    connected_edges = []
    for e in E: 
        for v in T[0]:
            if v in e and e not in T[1]:
           
                connected_edges.append(e)
    valid_edges = []
    for e in connected_edges:
        if e[0] not in T[0] or e[1] not in T[0]: 
            valid_edges.append(e)
    return valid_edges

def min_edge_append(T):
    valid = valid_edges(T) 
    min_edge = valid[0] 
    for i in range(len(valid)):
        if cost(valid[i]) < cost(min_edge):
            min_edge = valid[i]

    new_edges = []
    new_edges.append(min_edge)
    for e in T[1]:
        new_edges.append(e)

    new_vertices = {min_edge[0], min_edge[1]}

    return (new_vertices.union(T[0]), new_edges)

def Prims(T):  
    x=0
    while T[0] != V: 
        x+=1
        T = min_edge_append(T)
        print ("Iteration "+str(x))
        print (T)
        print (" ")
    cost_total = 0
    for e in T[1]:
        cost_total += cost(e)
    return (T, 'with a minimum total cost of', cost_total)
    
print("The Prims algorithm for this graph with all the vertices used, vertex sets and total cost",Prims(T))
