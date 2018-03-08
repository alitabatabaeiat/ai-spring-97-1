class Node:
    def __init__(self, state, parent, action, path_cost):
        self.cell = state
        self.parent_cell = parent
        self.action = action
        self.path_cost = path_cost
