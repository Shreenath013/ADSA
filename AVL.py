class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 1

def height(r):
    return r.height if r else 0

def bf(r):
    return height(r.left) - height(r.right) if r else 0

def right_rotate(y):
    x = y.left
    t = x.right
    x.right = y
    y.left = t
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def left_rotate(x):
    y = x.right
    t = y.left
    y.left = x
    x.right = t
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(root, x):
    if not root:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    elif x > root.data:
        root.right = insert(root.right, x)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = bf(root)

    if b > 1 and x < root.left.data:
        return right_rotate(root)              # LL
    if b < -1 and x > root.right.data:
        return left_rotate(root)               # RR
    if b > 1 and x > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)              # LR
    if b < -1 and x < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)               # RL
    return root

def delete(root, x):
    if not root:
        return None
    if x < root.data:
        root.left = delete(root.left, x)
    elif x > root.data:
        root.right = delete(root.right, x)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        t = root.right
        while t.left:
            t = t.left
        root.data = t.data
        root.right = delete(root.right, t.data)

    root.height = 1 + max(height(root.left), height(root.right))
    b = bf(root)

    if b > 1 and bf(root.left) >= 0:
        return right_rotate(root)              # LL
    if b > 1 and bf(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)              # LR
    if b < -1 and bf(root.right) <= 0:
        return left_rotate(root)               # RR
    if b < -1 and bf(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)               # RL
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(f"{root.data}(BF:{bf(root)})", end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

root = None
while True:
    print("\n1.Insert  2.Delete  3.Inorder")
    print("4.Preorder  5.Postorder  6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        root = insert(root, x)
    elif ch == 2:
        x = int(input("Delete value: "))
        root = delete(root, x)
    elif ch == 3:
        inorder(root)
        print()
    elif ch == 4:
        preorder(root)
        print()
    elif ch == 5:
        postorder(root)
        print()
    elif ch == 6:
        break
    else:
        print("Invalid choice")
