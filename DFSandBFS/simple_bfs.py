# bfs_search performs a breadth-first search on a given graph and returns the path
def bfs_search(graph, start):
    visited = set()
    nodeQueue = [start]
    while len(nodeQueue) > 0:
        vertex = nodeQueue.pop(0) # this is a queue so we pop first item
        if vertex not in visited:
            visited.add(vertex)
            nodeQueue.extend(graph[vertex] - visited)
    return visited

# shortest_path uses bfs to find the shortest path 
def shortest_path(graph, start, goal):
    nodeQueue = [(start, [start])]
    while len(nodeQueue) > 0:
        (vertex, path) = nodeQueue.pop(0)
        for nextNode in graph[vertex] - set(path):
            if nextNode == goal:
                return path + [nextNode]
            else:
                nodeQueue.append((nextNode, path + [nextNode]))

# test functions
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print("Graph: ", graph)
result1 = bfs_search(graph, 'A')
result2 = shortest_path(graph, 'A', 'F')
print("BFS Search for 'A': ", result1)
print("BFS shortest path from 'A' to 'F': ", result2)