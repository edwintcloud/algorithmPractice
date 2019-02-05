# dfs_search_recursive performs a depth-first search on a given graph recursively
def dfs_search_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nextNode in graph[start] - visited:
        dfs_search_recursive(graph, nextNode, visited)
    return visited

# dfs_search performs a depth-first search on a given graph without using recursion
def dfs_search(graph, start, visited=None):
    visited = set()
    nodeStack = []
    nodeStack.append(start)
    while len(nodeStack) > 0:
        vertex = nodeStack.pop()
        if vertex not in visited:
            visited.add(vertex)
            nodeStack.extend(graph[vertex] - visited)
    return visited

# dfs_paths performs recursive dfs search to find all posible paths from start to goal
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for nextNode in graph[start] - set(path):
        yield from dfs_paths(graph, nextNode, goal, path + [nextNode])

# test functions
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print("Graph: ", graph)
result1 = dfs_search_recursive(graph, 'C')
result2 = dfs_search(graph, 'C')
result3 = list(dfs_paths(graph, 'A', 'F'))
print("Recursive DFS Search for 'C': ", result1)
print("DFS Search for 'C': ", result2)
print("DFS paths from 'A' to 'F': ", result3)