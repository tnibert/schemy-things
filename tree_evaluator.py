import re

class BinaryTree:
    """
    This is just a silly way of representing a tree as a flat array.
    """
    def __init__(self, root, size):
        self.arr = [None] * size
        self.arr[0] = root
        
    def parent_idx(self, i):
        return (i-1)/2

    def left_idx(self, i):
        return 2*i+1

    def right_idx(self, i):
        return 2*i+2
       
    def set_left_child(self, i, x):
        idx = self.left_idx(i)
        self.arr[idx] = x
        return idx

    def set_right_child(self, i, x):
        idx = self.right_idx(i)
        self.arr[idx] = x
        return idx
            
    def get_left_child(self, i):
        idx = self.left_idx(i)
        return idx, self.arr[idx]

    def get_right_child(self, i):
        idx = self.right_idx(i)
        return idx, self.arr[idx]

    def traverse(self, i):
        val = self.arr[i]
        if val is None:
            return
        yield from self.traverse(self.left_idx(i))
        yield from self.traverse(self.right_idx(i))
        yield val


operations = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b
}

class Evaluator:
    """
    wip
    """
    def __init__(self):
        self.tree = BinaryTree(1, 100)

    def evaluate(self, expression):
        tokens = [i for i in re.split(r'(\d+|\W+)', expression) if i]
        print(tokens)

if __name__ == '__main__':
    t = BinaryTree('+', 100)
    i1 = t.set_left_child(0, '-')
    t.set_left_child(i1, 4)
    t.set_right_child(i1, 5)
    i2 = t.set_right_child(0, '*')
    t.set_left_child(i2, 6)
    t.set_right_child(i2, 7)
    for val in t.traverse(0):
        print(val)

    e = Evaluator()
    e.evaluate("2+3+4")
