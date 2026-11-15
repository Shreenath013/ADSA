MAX = 5
queue = [0] * MAX

front = -1
rear = -1

# Enqueue operation
def enqueue(value):
    global front, rear

    if rear == MAX - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0

        rear = rear + 1
        queue[rear] = value

        print(value, "inserted into queue")

# Dequeue operation
def dequeue():
    global front, rear

    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        value = queue[front]

        print("Deleted element:", value)

        front = front + 1

        if front > rear:
            front = -1
            rear = -1

# Front operation
def get_front():
    if front == -1:
        print("Queue is empty")
    else:
        print("Front element:", queue[front])

# Rear operation
def get_rear():
    if rear == -1:
        print("Queue is empty")
    else:
        print("Rear element:", queue[rear])

# Display operation
def display():
    if front == -1:
        print("Queue is empty")
    else:
        print("Queue elements:")

        for i in range(front, rear + 1):
            print(queue[i], end=" ")

        print()

# Main program
while True:

    print("\n--- QUEUE OPERATIONS ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rear")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        enqueue(value)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        get_front()
    elif choice == 4:
        get_rear()
    elif choice == 5:
        display()
    elif choice == 6:
        print("Program terminated.")
        break
    else:
        print("Invalid choice")