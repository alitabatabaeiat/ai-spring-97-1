from util import *
from node import *
import copy

# depth-limited dfs
def dls_solver(maze, limit):
    return []


def iterative_dfs_solver(maze):
    return []


def dfs_solver(maze):
    return []


def bfs_solver(maze):
    frontier = []
    explored = []
    start = Node(state = maze.start, parent = None, path_cost = 0);
    frontier.append(start)
    found = False
    node = Node()
    while True:
        if not frontier:
            break
        node = frontier[0]
        frontier = delete_first_element(frontier)
        if node.cell == maze.goal:# reach the Goal
            found = True
            break
        explored.append(node.cell) # list of cells
        neighbors = maze.get_neighbors(node.cell) # list of cells
        add_neighbors_to_frontier(frontier, explored, neighbors, node)

    if found:
        return node.getPath()
    return []


def astar_heuristic(maze, cell):
    return 0


def astar_solver(maze):
    return []
