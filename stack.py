MAX = 5

stack = [0] * MAX
top = -1

# Push operation
def push(value):
    global top

    if top == MAX - 1:
        print("Stack Overflow")
    else:
        top = top + 1
        stack[top] = value
        print(value, "pushed into stack")

# Pop operation
def pop():
    global top

    if top == -1:
        print("Stack Underflow")
    else:
        value = stack[top]
        top = top - 1
        print("Popped element:", value)

# Peek operation
def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print("Top element:", stack[top])

# Display operation
def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(top, -1, -1):
            print(stack[i])

while True:

    print("\n--- STACK OPERATIONS ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        push(value)
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice")