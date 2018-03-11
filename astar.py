from search import *
from util import *

class AStar(Search):
    def solve(self):
        self.add_start_to_frontier()
        while True:
            if not self.frontier:
                break
            index = self.pick_from_frontier()
            self.frontier = delete_element(self.frontier, index)
            if self.goal_test(): # reach the Goal
                self.add_to_explored()
                self.found = True
                break
            self.add_to_explored()
            self.add_neighbors_to_frontier()

        return self.get_path()

    def add_start_to_frontier(self):
        heuristic = self.astar_heuristic(self.maze.start)
        n = Node(cell = self.maze.start, parent = None, path_cost = 0, h = heuristic)
        self.frontier.append(n)
        return

    def add_neighbors_to_frontier(self):
        i = 0
        for n in self.get_neighbors():
            if not (self.is_explored(n) or self.is_frontier(n)):
                i += 1
                heuristic = self.astar_heuristic(n)
                mNode = Node(cell = n, parent = self.node, path_cost = self.node.path_cost + 1, h = heuristic)
                self.frontier.append(mNode)
        return i

    def pick_from_frontier(self):
        self.node = self.frontier[0]
        i, index = 0, 0
        for f in self.frontier:
            print(f)
            if f.fn < self.node.fn:
                self.node = f
                index = i
            i += 1
        return index

    def astar_heuristic(self, cell):
        dx = abs(cell[0] - self.maze.goal[0])
        dy = abs(cell[1] - self.maze.goal[1])
        return dx + dy
