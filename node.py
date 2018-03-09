class Node:
    def __init__(self, state = None, parent = None, path_cost = None, fn = None):
        self.cell = state
        self.parent = parent
        self.path_cost = path_cost
        self.fn = fn

    def __str__(self):
        val = 'cell = (%d, %d)\n' % self.cell
        if self.parent is not None:
            val += 'parent_cell = (%d, %d)\n' % self.parent.cell
        else:
            val += 'No parent\n'
        val += 'path_cost = %d\n' % (self.path_cost)
        if self.fn is not None:
            val += 'f(n) = %d\n' %(self.fn)
        return val

    def getPath(self):
        path = []
        cur_node = self
        while cur_node is not None:
            path.append(cur_node.cell)
            cur_node = cur_node.parent
        return list(reversed(path))
