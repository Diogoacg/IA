# Import necessary libraries
from collections import deque

#----------------------------------------Funcionalidade 1----------------------------------------
# Gerar os circuitos de entrega, caso existam, que cubram um determinado território. 
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph:  # Verifique se a chave existe no dicionário
            for next in set([neighbor[0] for neighbor in graph[vertex]]) - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))



def all_paths_to_goal(graph, goal):
    all_paths = []
    for start in graph.keys():
        paths = list(dfs_paths(graph, start, goal))
        if paths:
            all_paths.extend(paths)
    return all_paths


