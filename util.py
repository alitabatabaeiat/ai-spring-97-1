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
            print(n)
            if frontier:
                for i in frontier:
                    if n != i.cell:
                        frontier.append(Node(state = n, parent = node.cell, path_cost = node.path_cost + 1))
            else:
                frontier.append(Node(state = n, parent = node.cell, path_cost = node.path_cost + 1))
    return
