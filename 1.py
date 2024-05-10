def mst(graph,start):
    if start not in graph.keys():
        return None
    n = len(graph)
    
    mst = []
    visited = []
    visited.append(start)
    
    while len(visited) != n:
        parent , min_node, min_dist = min_key(graph,visited)
        mst.append([parent , min_node, min_dist])
        visited.append(min_node)
        
    return mst

def min_key(graph,visited):
    import math
    min_node = None
    min_dist = math.inf
    for i in visited:
        for node,dist in graph[i].items():
            if dist < min_dist and node not in visited:
                parent = i 
                min_dist = dist
                min_node = node
    return parent,min_node,min_dist

def min_cost(mst):
    count = 0
    for i in mst:
        count += i[2]
    
    return count
        
    

graph = {
    'A': {'B': 4, 'C': 8},
    'B': {'A': 4, 'D': 7, 'E': 5},
    'C': {'A': 8, 'E': 1},
    'D': {'B': 7, 'E': 9, 'F': 14},
    'E': {'B': 5, 'C': 1, 'D': 9, 'F': 10},
    'F': {'D': 14, 'E': 10}
}

mst1 = mst(graph, 'A')
a = min_cost(mst1)
print(mst1)
print('min cost : ', a)
