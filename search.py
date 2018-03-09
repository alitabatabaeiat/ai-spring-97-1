from node import *

class Search:
    def __init__(self, maze):
        self.frontier = []
        self.explored = []
        self.found = False
        self.node = None
        self.maze = maze

    def add_start_to_frontier(self):
        n = Node(cell = self.maze.start, parent = None, path_cost = 0)
        self.frontier.append(n)
        return

    def goal_test(self):
        return self.maze.goal == self.node.cell

    def get_path(self):
        if self.found:
            return self.node.getPath()
        return []

    def is_explored(self, n):
        return n in self.explored

    def is_frontier(self, n):
        if self.frontier:
            for f in self.frontier:
                return n == f.cell

    def get_neighbors(self):
        return self.maze.get_neighbors(self.node.cell)

    def add_neighbors_to_frontier(self):
        i = 0
        for n in self.get_neighbors():
            if not (self.is_explored(n) or self.is_frontier(n)):
                i += 1
                mNode = Node(cell = n, parent = self.node, path_cost = self.node.path_cost + 1)
                self.frontier.append(mNode)
        return i

    def add_to_explored(self):
        self.explored.append(self.node.cell)
        return
