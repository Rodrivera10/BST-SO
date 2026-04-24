from .node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if not self.root:
            self.root = node
            return
        
        current = self.root
        while True:
            if key < current.key:
                if not current.left:
                    current.left = node
                    node.parent = current
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    node.parent = current
                    return
                current = current.right

    def search(self, key):
        current = self.root
        steps = 0

        while current:
            steps += 1
            if key == current.key:
                return current, steps
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None, steps