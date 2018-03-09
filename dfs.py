from search import *
from util import *

class DFS(Search):
    def solve(self):
        self.add_start_to_frontier()
        while True:
            if not self.frontier:
                break
            self.node = self.frontier[-1]
            self.frontier = delete_element(self.frontier, -1)
            if self.goal_test(): # reach the Goal
                self.add_to_explored()
                self.found = True
                break
            num = self.add_neighbors_to_frontier()
            self.update_explored(num)

        return self.get_path()

    def get_path(self):
        if self.found:
            return self.explored
        return []

    def update_explored(self, num):
        if num > 0:
            self.explored.append(self.node.cell) # list of explored cells on a current path from start
        elif num == 0:
            self.go_up_on_tree()

    def go_up_on_tree(self):
        while self.explored and self.frontier:
            if self.explored[-1] == self.frontier[-1].parent.cell:
                break
            self.explored = delete_element(self.explored, -1)
