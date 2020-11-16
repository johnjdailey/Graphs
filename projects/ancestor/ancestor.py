
#ancestor.py



from collections import deque


def createGraph(ancestors):
    graph = {}
    for edge in ancestors:
        child, parent = edge[1], edge[0]
    
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = {parent}
    return graph
    

def earliest_ancestor(ancestors, starting_node):
    if len(ancestors) == 0:
        return ''
    graph = createGraph(ancestors) 
    queue = deque()
    queue.append(starting_node)
    visited = set()
    
    if starting_node not in graph:
        return -1
    while len(queue) > 0:
        curr = queue.popleft()
        if curr not in visited:
            visited.add(curr)
            print(curr)

            for neighbor in graph[curr]:
                if neighbor in graph:
                    queue.append(neighbor)
    
    return neighbor
