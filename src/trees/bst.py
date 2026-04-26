from .node import Node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key == current.key:
                return
            elif key < current.key:
                if not current.left:
                    new_node = Node(key)
                    new_node.parent = current
                    current.left = new_node
                    return
                current = current.left
            else:
                if not current.right:
                    new_node = Node(key)
                    new_node.parent = current
                    current.right = new_node
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
