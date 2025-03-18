from collections import defaultdict
def solution(edges):
    answer = []
    a, b, c, d = 0, 0, 0, 0
    total_graph = 0
    
    edge_in = defaultdict(list)
    edge_out = defaultdict(list)
    
    for i,o in edges:
        edge_in[o].append(i)
        edge_in[i] = edge_in[i]
        edge_out[i].append(o)
        
    for i in edge_out:
        if len(edge_out[i]) >=2 and len(edge_in[i]) == 0:
            a = i
            total_graph = len(edge_out[i])
            for j in edge_out[i]:
                edge_in[j].remove(i)
    del edge_in[a]
    
    for i in edge_in:
        if len(edge_in[i]) == 0:
            c+= 1
        elif len(edge_in[i]) == 2:
            d+= 1
        else:
            continue
    
    return [a, total_graph-c-d, c, d]