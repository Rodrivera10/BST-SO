from .node import Node

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    # ---------------- ROTACIONES ---------------- #

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    # ---------------- INSERCIÓN ---------------- #

    def insert(self, key):
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL
        node.parent = None
        node.color = "RED"

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    # ---------------- FIX RB ---------------- #

    def _fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right  # tío

                if u.color == "RED":
                    # Caso 1
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Caso 2
                        k = k.parent
                        self.left_rotate(k)

                    # Caso 3
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left  # tío

                if u.color == "RED":
                    # Caso 1
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Caso 2
                        k = k.parent
                        self.right_rotate(k)

                    # Caso 3
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = "BLACK"

    # ---------------- SEARCH  ---------------- #

    def search(self, key):
        current = self.root
        steps = 0

        while current != self.NIL:
            steps += 1

            if key == current.key:
                return current, steps

            if key < current.key:
                current = current.left
            else:
                current = current.right

        return None, steps