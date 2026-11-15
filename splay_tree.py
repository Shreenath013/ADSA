class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right

        if y is None:
            return

        x.right = y.left

        if y.left is not None:
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

    def right_rotate(self, x):
        y = x.left

        if y is None:
            return

        x.left = y.right

        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, x):
        while x.parent is not None:

            if x.parent.parent is None:
                if x == x.parent.left:
                    self.right_rotate(x.parent)
                else:
                    self.left_rotate(x.parent)

            elif (x == x.parent.left and
                  x.parent == x.parent.parent.left):
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)

            elif (x == x.parent.right and
                  x.parent == x.parent.parent.right):
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)

            elif (x == x.parent.right and
                  x.parent == x.parent.parent.left):
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)

            else:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print(data, "inserted successfully.")
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current

            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                self.splay(current)
                print("Duplicate values are not allowed.")
                return

        new_node = Node(data)
        new_node.parent = parent

        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self.splay(new_node)
        print(data, "inserted successfully.")

    def search(self, data):
        current = self.root
        last = None

        while current is not None:
            last = current

            if data == current.data:
                self.splay(current)
                print(data, "found and moved to the root.")
                return current

            elif data < current.data:
                current = current.left
            else:
                current = current.right

        if last is not None:
            self.splay(last)

        print(data, "not found.")
        return None

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def join(self, left_tree, right_tree):
        if left_tree is None:
            self.root = right_tree
            if right_tree is not None:
                right_tree.parent = None
            return

        self.root = left_tree
        left_tree.parent = None

        maximum = left_tree
        while maximum.right is not None:
            maximum = maximum.right

        self.splay(maximum)
        self.root.right = right_tree

        if right_tree is not None:
            right_tree.parent = self.root

    def delete(self, data):
        node = self.search(data)

        if node is None:
            print("Deletion failed: value not found.")
            return

        left_tree = node.left
        right_tree = node.right

        if left_tree is not None:
            left_tree.parent = None

        if right_tree is not None:
            right_tree.parent = None

        node.left = None
        node.right = None
        node.parent = None

        self.join(left_tree, right_tree)
        print(data, "deleted successfully.")

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def display(self):
        if self.root is None:
            print("Tree is empty.")
            return

        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        h = height(self.root)
        width = 4 * (2 ** h)
        canvas = [[" "] * width for _ in range(2 * h - 1)]

        def draw(node, row, col, gap):
            if node is None:
                return

            label = str(node.data)
            start = col - len(label) // 2

            for i, ch in enumerate(label):
                if 0 <= start + i < width:
                    canvas[row][start + i] = ch

            if row + 2 >= len(canvas):
                return

            if node.left is not None:
                child_col = col - gap
                if child_col >= 0:
                    branch_col = (col + child_col) // 2
                    canvas[row + 1][branch_col] = "/"
                    draw(node.left, row + 2, child_col,
                         max(1, gap // 2))

            if node.right is not None:
                child_col = col + gap
                if child_col < width:
                    branch_col = (col + child_col) // 2
                    canvas[row + 1][branch_col] = "\\"
                    draw(node.right, row + 2, child_col,
                         max(1, gap // 2))

        draw(self.root, 0, width // 2, width // 4)

        print("\nTree structure:")
        for row in canvas:
            line = "".join(row).rstrip()
            if line.strip():
                print(line)


if __name__ == "__main__":
    tree = SplayTree()

    while True:
        print("\n===== SPLAY TREE MENU =====")
        print("1. Insert node")
        print("2. Search node")
        print("3. Delete node")
        print("4. Inorder traversal")
        print("5. Display tree")
        print("6. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            try:
                value = int(input("Enter value: "))
                tree.insert(value)
            except ValueError:
                print("Please enter a valid integer.")

        elif ch == 2:
            try:
                value = int(input("Enter value: "))
                tree.search(value)
            except ValueError:
                print("Please enter a valid integer.")

        elif ch == 3:
            try:
                value = int(input("Enter value: "))
                tree.delete(value)
            except ValueError:
                print("Please enter a valid integer.")

        elif ch == 4:
            if tree.root is None:
                print("Tree is empty.")
            else:
                print("Inorder traversal:")
                tree.inorder(tree.root)
                print()

        elif ch == 5:
            tree.display()

        elif ch == 6:
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")