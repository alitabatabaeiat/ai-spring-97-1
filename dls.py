from dfs import *
from util import *

class DLS(DFS):
    def __init__(self, maze, limit):
        super().__init__(maze)
        self.limit = limit

    def solve(self):
        if self.limit == 0:
            if self.maze.start == self.maze.goal:
                return [self.maze.start]
            return []
        return super().solve()

    def get_neighbors(self):
        if self.node.parent is None: # start node
            return self.maze.get_neighbors(self.node.cell)
        elif self.node.parent.path_cost < self.limit - 1:
            return self.maze.get_neighbors(self.node.cell)
        return []
