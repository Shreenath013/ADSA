
class Node:
    def __init__(self, data, color="RED"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, "BLACK")
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self.NIL:
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

        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def insert(self, data):
        z = Node(data)
        z.left = self.NIL
        z.right = self.NIL

        parent = self.NIL
        current = self.root

        while current != self.NIL:
            parent = current

            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                print("Duplicate values are not allowed.")
                return

        z.parent = parent

        if parent == self.NIL:
            self.root = z
        elif data < parent.data:
            parent.left = z
        else:
            parent.right = z

        self.insert_fixup(z)
        print(data, "inserted successfully.")

    def insert_fixup(self, z):
        while z.parent.color == "RED":

            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right

                if uncle.color == "RED":
                    z.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent

                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)

            else:
                uncle = z.parent.parent.left

                if uncle.color == "RED":
                    z.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent

                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)

        self.root.color = "BLACK"

    def search(self, data):
        current = self.root

        while current != self.NIL:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return None

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def delete(self, data):
        z = self.search(data)

        if z is None:
            print(data, "not found in the tree.")
            return

        y = z
        original_color = y.color

        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)

        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)

        else:
            y = self.minimum(z.right)
            original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if original_color == "BLACK":
            self.delete_fixup(x)

        print(data, "deleted successfully.")

    def delete_fixup(self, x):
        while x != self.root and x.color == "BLACK":

            if x == x.parent.left:
                sibling = x.parent.right

                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    sibling = x.parent.right

                if (sibling.left.color == "BLACK"
                        and sibling.right.color == "BLACK"):
                    if sibling != self.NIL:
                        sibling.color = "RED"
                    x = x.parent

                else:
                    if sibling.right.color == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self.right_rotate(sibling)
                        sibling = x.parent.right

                    sibling.color = x.parent.color
                    x.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                sibling = x.parent.left

                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    sibling = x.parent.left

                if (sibling.right.color == "BLACK"
                        and sibling.left.color == "BLACK"):
                    if sibling != self.NIL:
                        sibling.color = "RED"
                    x = x.parent

                else:
                    if sibling.left.color == "BLACK":
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self.left_rotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = "BLACK"

    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(f"{node.data}({node.color})", end=" ")
            self.inorder(node.right)
    
    def display(self):
        if self.root == self.NIL:
            print("Tree is empty.")
            return

        def get_height(node):
            if node == self.NIL:
                return 0
            return 1 + max(
                get_height(node.left),
                get_height(node.right)
            )

        height = get_height(self.root)
        width = (2 ** height) * 6
        canvas = [[" "] * width for _ in range(2 * height - 1)]

        def draw(node, row, col, gap):
            if node == self.NIL:
                return

            label = f"{node.data}({node.color})"
            start = max(0, col - len(label) // 2)

            for i, ch in enumerate(label):
                if start + i < width:
                    canvas[row][start + i] = ch

            if row + 2 >= len(canvas):
                return

            if node.left != self.NIL:
                left_col = col - gap
                if left_col >= 0:
                    canvas[row + 1][(col + left_col) // 2] = "/"
                    draw(node.left, row + 2, left_col, max(1, gap // 2))

            if node.right != self.NIL:
                right_col = col + gap
                if right_col < width:
                    canvas[row + 1][(col + right_col) // 2] = "\\"
                    draw(node.right, row + 2, right_col, max(1, gap // 2))

        draw(self.root, 0, width // 2, width // 4)

        for row in canvas:
            line = "".join(row).rstrip()
            if line.strip():
                print(line)


if __name__ == "__main__":
    tree = RedBlackTree()

    while True:
        print("\n===== RED-BLACK TREE =====")
        print("1. Insert node")
        print("2. Delete node")
        print("3. Search node")
        print("4. Inorder traversal")
        print("5. Display tree")
        print("6. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            try:
                value = int(input("Enter value: "))
                tree.insert(value)
            except ValueError:
                print("Enter a valid integer.")

        elif ch == 2:
            try:
                value = int(input("Enter value: "))
                tree.delete(value)
            except ValueError:
                print("Enter a valid integer.")

        elif ch == 3:
            try:
                value = int(input("Enter value: "))
                result = tree.search(value)

                if result:
                    print(f"{value} found. Color: {result.color}")
                else:
                    print(value, "not found.")

            except ValueError:
                print("Enter a valid integer.")

        elif ch == 4:
            if tree.root == tree.NIL:
                print("Tree is empty.")
            else:
                print("Inorder traversal:")
                tree.inorder(tree.root)
                print()

        elif ch == 5:
            if tree.root == tree.NIL:
                print("Tree is empty.")
            else:
                print("Tree structure:")
                tree.display()

        elif ch == 6:
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")