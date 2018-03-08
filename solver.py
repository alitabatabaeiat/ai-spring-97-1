from util import *
from node import *
import copy

# depth-limited dfs
def dls_solver(maze, limit):
    if limit == 0:
        return []

    frontier = []
    explored = []
    start = Node(state = maze.start, parent = None, path_cost = 0);
    frontier.append(start)
    found = False
    node = Node()
    while True:
        if not frontier:
            break
        node = frontier[-1]
        frontier = delete_last_element(frontier)
        if node.cell == maze.goal: # reach the Goal
            found = True
            break

        neighbors = []
        if node.parent is None: # start node
            neighbors = maze.get_neighbors(node.cell) # list of cells
        elif node.parent.path_cost < limit - 1:
            neighbors = maze.get_neighbors(node.cell) # list of cells

        num = add_neighbors_to_frontier(frontier, explored, neighbors, node)
        if num > 0:
            explored.append(node.cell) # list of explored cells on a current path from start
        elif num == 0 and explored and frontier:
            if explored[-1] != frontier[-1].parent.cell:
                explored = delete_last_element(explored)

    if found:
        return node.getPath()
    return []


def iterative_dfs_solver(maze):
    return []


def dfs_solver(maze):
    frontier = []
    explored = []
    start = Node(state = maze.start, parent = None, path_cost = 0);
    frontier.append(start)
    found = False
    node = Node()
    while True:
        if not frontier:
            break
        node = frontier[-1]
        frontier = delete_last_element(frontier)
        if node.cell == maze.goal: # reach the Goal
            found = True
            break
        neighbors = maze.get_neighbors(node.cell) # list of cells
        num = add_neighbors_to_frontier(frontier, explored, neighbors, node)
        if num > 0:
            explored.append(node.cell) # list of explored cells on a current path from start
        elif num == 0 and explored and frontier:
            if explored[-1] != frontier[-1].parent.cell:
                explored = delete_last_element(explored)

    if found:
        return node.getPath()
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
        if node.cell == maze.goal: # reach the Goal
            found = True
            break
        explored.append(node.cell) # list of explored cells
        neighbors = maze.get_neighbors(node.cell) # list of cells
        add_neighbors_to_frontier(frontier, explored, neighbors, node)

    if found:
        return node.getPath()
    return []


def astar_heuristic(maze, cell):
    return 0


def astar_solver(maze):
    return []
