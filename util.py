from node import *

def delete_first_element(frontier):
    if len(frontier) == 1:
        frontier = []
    else:
        frontier = frontier[1:]
    return frontier

def add_neighbors_to_frontier(frontier, explored, neighbors, node):
    for n in neighbors:
        if n not in explored:
            append_permission = True
            if frontier:
                for f in frontier:
                    if n == f.cell:
                        append_permission = False
                        break
            if append_permission:
                frontier.append(Node(state = n, parent = node, path_cost = node.path_cost + 1))
    return
