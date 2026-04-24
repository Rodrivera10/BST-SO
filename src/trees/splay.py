from .node import Node

class SplayTree:
    def __init__(self):
        self.root = None

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x.parent.left == x:
                    self.rotate_right(x.parent)
                else:
                    self.rotate_left(x.parent)
            else:
                if x.parent.left == x and x.parent.parent.left == x.parent:
                    self.rotate_right(x.parent.parent)
                    self.rotate_right(x.parent)
                elif x.parent.right == x and x.parent.parent.right == x.parent:
                    self.rotate_left(x.parent.parent)
                    self.rotate_left(x.parent)
                else:
                    if x.parent.left == x:
                        self.rotate_right(x.parent)
                        self.rotate_left(x.parent)
                    else:
                        self.rotate_left(x.parent)
                        self.rotate_right(x.parent)

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        while x:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if not y:
            self.root = node
        elif key < y.key:
            y.left = node
        else:
            y.right = node

        self.splay(node)

    def search(self, key):
        current = self.root
        steps = 0

        while current:
            steps += 1
            if key == current.key:
                self.splay(current)
                return current, steps
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None, steps