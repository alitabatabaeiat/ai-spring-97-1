from search import *
from util import *

class BFS(Search):
    def solve(self):
        self.add_start_to_frontier()
        while True:
            if not self.frontier:
                break
            self.node = self.frontier[0]
            self.frontier = delete_element(self.frontier, 0)
            if self.goal_test(): # reach the Goal
                self.add_to_explored()
                self.found = True
                break
            self.add_to_explored()
            self.add_neighbors_to_frontier()

        return self.get_path()
