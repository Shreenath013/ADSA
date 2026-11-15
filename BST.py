
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    elif x > root.data:
        root.right = insert(root.right, x)
    return root

def search_rec(root, x):
    if root is None or root.data == x:
        return root
    if x < root.data:
        return search_rec(root.left, x)
    return search_rec(root.right, x)

def search_iter(root, x):
    while root:
        if root.data == x:
            return root
        root = root.left if x < root.data else root.right
    return None

def delete(root, x):
    if root is None:
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
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
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
    print("\n1.Insert  2.Recursive Search  3.Iterative Search")
    print("4.Delete  5.Inorder  6.Preorder  7.Postorder  8.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        root = insert(root, x)
    elif ch == 2:
        x = int(input("Search value: "))
        print("Found" if search_rec(root, x) else "Not Found")
    elif ch == 3:
        x = int(input("Search value: "))
        print("Found" if search_iter(root, x) else "Not Found")
    elif ch == 4:
        x = int(input("Delete value: "))
        root = delete(root, x)
    elif ch == 5:
        inorder(root)
        print()
    elif ch == 6:
        preorder(root)
        print()
    elif ch == 7:
        postorder(root)
        print()
    elif ch == 8:
        break
    else:
        print("Invalid choice")
