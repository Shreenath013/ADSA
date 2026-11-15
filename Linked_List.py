class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input("Enter number of elements you want in the linked list: "))

head = None
temp = None

for i in range(n):

    element = int(input(f"Enter the Element {i + 1}: "))

    new_node = Node(element)

    if head is None:
        head = new_node
        temp = new_node
    else:
        temp.next = new_node
        temp = new_node

# Traversal
print("\nLinked List elements:")

temp = head

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

# Insertion
pos = int(input("\n\nEnter the position where you want to insert the element: "))

value = int(input("Enter the value you want to insert: "))

new_node = Node(value)


# Insertion at beginning
if pos == 1:

    new_node.next = head
    head = new_node

else:

    temp = head

    # Move to the node before the required position
    for i in range(1, pos - 1):
        temp = temp.next

    new_node.next = temp.next
    temp.next = new_node

n = n + 1


# Traversal after insertion
print("\n\nAfter insertion:")

temp = head

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

# Deletion
pos = int(input("\n\nEnter the position of the element you want to delete: "))

# Deletion of first node
if pos == 1:

    head = head.next

else:

    temp = head

    # Move to the node before the node to be deleted
    for i in range(1, pos - 1):
        temp = temp.next

    temp.next = temp.next.next

n = n - 1

# Traversal after deletion
print("\n\nAfter deletion:")

temp = head

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

# Searching
key = int(input("\n\nEnter the element you want to search: "))

found = False
position = 1

temp = head

while temp is not None:

    if temp.data == key:

        print("\n\nElement", key, "found at position", position)

        found = True
        break

    temp = temp.next
    position = position + 1

if found == False:
    print("\n\nElement not found")