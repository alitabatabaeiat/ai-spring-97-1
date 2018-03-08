from node import *

def delete_first_element(l):
    if len(l) == 1:
        l = []
    else:
        l = l[1:]
    return l

def delete_last_element(l):
    if len(l) == 1:
        l = []
    else:
        l = l[:-1]
    return l

def add_neighbors_to_frontier(frontier, explored, neighbors, node):
    i = 0
    for n in neighbors:
        if n not in explored:
            append_permission = True
            if frontier:
                for f in frontier:
                    if n == f.cell:
                        append_permission = False
                        break
            if append_permission:
                i += 1
                frontier.append(Node(state = n, parent = node, path_cost = node.path_cost + 1))
    return i
