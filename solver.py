from util import *
from node import *
from bfs import *
from dfs import *
from dls import *
from astar import *

def dls_solver(maze, limit):
    dls = DLS(maze, limit)
    return dls.solve()

def iterative_dfs_solver(maze):
    depth = 0
    while True:
        path = dls_solver(maze, depth)
        if path:
            return path
        depth += 1
    return []

def dfs_solver(maze):
    dfs = DFS(maze)
    return dfs.solve()

def bfs_solver(maze):
    bfs = BFS(maze)
    return bfs.solve()

def astar_heuristic(maze, cell):
    astar = AStar(maze)
    return astar.astar_heuristic(cell)

def astar_solver(maze):
    astar = AStar(maze)
    return astar.solve()
