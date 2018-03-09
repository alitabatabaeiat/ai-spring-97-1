from util import *
from node import *
import copy

# depth-limited dfs
def dls_solver(maze, limit):
    if limit == 0:
        if maze.start == maze.goal:
            return [maze.start]
        return []

    frontier = []
    explored = []
    start = Node(cell = maze.start, parent = None, path_cost = 0);
    frontier.append(start)
    found = False
    node = Node()
    while True:
        if not frontier:
            break
        node = frontier[-1]
        frontier = delete_element(frontier, -1)
        if node.cell == maze.goal: # reach the Goal
            explored.append(node.cell)
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
        elif num == 0:
            while explored and frontier:
                if explored[-1] == frontier[-1].parent.cell:
                    break
                explored = delete_element(explored, -1)

    if found:
        return explored
    return []


def iterative_dfs_solver(maze):
    depth = 0
    while True:
        path = dls_solver(maze, depth)
        if path:
            return path
        depth += 1
    return []


def dfs_solver(maze):
    frontier = []
    explored = []
    start = Node(cell = maze.start, parent = None, path_cost = 0);
    frontier.append(start)
    found = False
    node = Node()
    while True:
        if not frontier:
            break
        node = frontier[-1]
        frontier = delete_element(frontier, -1)
        if node.cell == maze.goal: # reach the Goal
            explored.append(node.cell)
            found = True
            break
        neighbors = maze.get_neighbors(node.cell) # list of cells
        num = add_neighbors_to_frontier(frontier, explored, neighbors, node)
        if num > 0:
            explored.append(node.cell) # list of explored cells on a current path from start
        elif num == 0:
            while explored and frontier:
                if explored[-1] == frontier[-1].parent.cell:
                    break
                explored = delete_element(explored, -1)
    if found:
        return explored
    return []


def bfs_solver(maze):
    frontier = []
    explored = []
    start = Node(cell = maze.start, parent = None, path_cost = 0);
    frontier.append(start)
    found = False
    node = Node()
    while True:
        if not frontier:
            break
        node = frontier[0]
        frontier = delete_element(frontier, 0)
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
    dx = abs(cell[0] - maze.goal[0])
    dy = abs(cell[1] - maze.goal[1])
    return dx + dy


def astar_solver(maze):
    frontier = []
    explored = []
    start = Node(cell = maze.start, parent = None, path_cost = 0, h = astar_heuristic(maze, maze.start));
    frontier.append(start)
    found = False
    node = Node()
    while True:
        if not frontier:
            break
        (node, index) = pick_from_frontier(frontier)
        frontier = delete_element(frontier, index)
        if node.cell == maze.goal: # reach the Goal
            found = True
            break
        explored.append(node.cell) # list of explored cells
        neighbors = maze.get_neighbors(node.cell) # list of cells
        add_neighbors_to_frontier(frontier, explored, neighbors, node, maze, astar_heuristic)

    if found:
        return node.getPath()
    return []
