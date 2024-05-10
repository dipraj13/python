import heapq

class Node:
    def __init__(self,state , g_score=float('inf'),h_score=float('inf'),parent=None):
        self.state = state
        self.g_score = g_score
        self.h_score = h_score
        self.parent = parent
        
    def __lt__(self,other):
        return (self.g_score + self.h_score) < (other.g_score + other.h_score)
    
def astar(graph,start,goal,h):
    open_list = []
    closed_list = set()
    head = Node(start,0,h(start))
    heapq.heappush(open_list,head)
    
    while open_list:
        curr = heapq.heappop(open_list)
        
        if curr.state == goal:
            return curr
        
        closed_list.add(curr.state)
        
        for neighbor, dist in graph[curr.state].items():
            temp = curr.g_score + dist
        
            neb_node = Node(neighbor)
            
            if neb_node not in open_list or temp < neb_node.g_score:
                neb_node.g_score = temp
                neb_node.h_score = h(neighbor)
                neb_node.parent = curr
                heapq.heappush(open_list,neb_node)
    return None

def path(graph,h):
    ans = astar(graph,'A','G',h)
    arr = []
    while True:
        if ans.parent == None:
            arr.append(ans.state)
            break
        arr.append(ans.state)
        ans = ans.parent
    return arr[::-1]


def h(node):
    heuristics = {
    'A' : 3,
    'B' : 4,
    'D' : 1,
    'C' : 3,
    'E' : 2,
    'F' : 1,
    'G' : 0
     }
    return heuristics[node]

graph = {
    'A': {'B': 3, 'D': 2, 'E': 2},
    'B': {'A': 3, 'D': 3, 'C': 1},
    'D': {'A': 2, 'B': 3, 'C': 2, 'G': 1},
    'C': {'B': 1, 'D': 2},
    'E': {'A': 2, 'F': 1},
    'F': {'E': 1, 'G': 1},
    'G': {'D': 1, 'F': 1}
}

print(path(graph,h))
