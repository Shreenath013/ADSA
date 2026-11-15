class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Insertion
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


# Recursive Search
def search_recursive(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search_recursive(root.left, key)
    return search_recursive(root.right, key)


# Iterative Search
def search_iterative(root, key):
    while root:
        if root.data == key:
            return root
        root = root.left if key < root.data else root.right
    return None


# Deletion
def delete(root, key):
    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")

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


# Main
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

root = None
for x in arr:
    root = insert(root, x)

print("\nInorder: ", end="")
inorder(root)

print("\nPreorder: ", end="")
preorder(root)

print("\nPostorder: ", end="")
postorder(root)

key = int(input("\n\nEnter element to search: "))

print("Recursive Search:", "Found" if search_recursive(root, key) else "Not Found")
print("Iterative Search:", "Found" if search_iterative(root, key) else "Not Found")

key = int(input("\nEnter element to delete: "))
root = delete(root, key)

print("After deletion (Inorder): ", end="")
inorder(root)