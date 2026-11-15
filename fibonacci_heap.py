class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = self.child = None
        self.left = self.right = self
        self.mark = False


class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.n = 0

    def insert(self, key):
        x = Node(key)
        if self.min is None:
            self.min = x
        else:
            x.left, x.right = self.min.left, self.min
            self.min.left.right = x
            self.min.left = x
            if x.key < self.min.key:
                self.min = x
        self.n += 1

    def union(self, other):
        if other.min is None:
            return
        if self.min is None:
            self.min, self.n = other.min, other.n
            other.min, other.n = None, 0
            return

        a, b = self.min.right, other.min.left
        self.min.right = other.min
        other.min.left = self.min
        a.left, b.right = b, a

        if other.min.key < self.min.key:
            self.min = other.min

        self.n += other.n
        other.min, other.n = None, 0

    def link(self, y, x):
        y.left.right, y.right.left = y.right, y.left
        y.parent = x
        y.mark = False

        if x.child is None:
            x.child = y
            y.left = y.right = y
        else:
            c = x.child
            y.left, y.right = c.left, c
            c.left.right = y
            c.left = y

        x.degree += 1

    def extract_min(self):
        z = self.min
        if z is None:
            print("Heap is empty")
            return

        if z.child:
            children = []
            x = z.child
            while True:
                children.append(x)
                x = x.right
                if x == z.child:
                    break

            for x in children:
                x.left.right = x.right
                x.right.left = x.left
                x.parent = None

                x.left, x.right = self.min.left, self.min
                self.min.left.right = x
                self.min.left = x

        z.left.right = z.right
        z.right.left = z.left
        self.n -= 1

        if z == z.right:
            self.min = None
        else:
            self.min = z.right
            self.consolidate()

        print("Extracted minimum:", z.key)

    def consolidate(self):
        roots = []
        x = self.min
        while True:
            roots.append(x)
            x = x.right
            if x == self.min:
                break

        A = {}
        for x in roots:
            d = x.degree
            while d in A:
                y = A.pop(d)
                if y.key < x.key:
                    x, y = y, x
                self.link(y, x)
                d += 1
            A[d] = x

        self.min = None
        for x in A.values():
            x.left = x.right = x
            if self.min is None:
                self.min = x
            else:
                x.left, x.right = self.min.left, self.min
                self.min.left.right = x
                self.min.left = x
                if x.key < self.min.key:
                    self.min = x

    def cut(self, x, y):
        if x.right == x:
            y.child = None
        else:
            x.left.right = x.right
            x.right.left = x.left
            if y.child == x:
                y.child = x.right

        y.degree -= 1
        x.parent = None
        x.mark = False

        x.left, x.right = self.min.left, self.min
        self.min.left.right = x
        self.min.left = x

    def cascading_cut(self, y):
        z = y.parent
        if z:
            if not y.mark:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def decrease_key(self, old, new):
        x = self.find(self.min, old)
        if x is None:
            print("Element not found")
            return
        if new > x.key:
            print("New key must be smaller")
            return

        x.key = new
        y = x.parent
        if y and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)

        if self.min is None or x.key < self.min.key:
            self.min = x

    def find(self, start, key):
        if start is None:
            return None

        roots = []
        x = start
        while True:
            roots.append(x)
            x = x.right
            if x == start:
                break

        for x in roots:
            if x.key == key:
                return x
            found = self.find(x.child, key)
            if found:
                return found
        return None

    def display(self):
        def show(start):
            if start is None:
                return
            x = start
            while True:
                print(x.key, end=" ")
                show(x.child)
                x = x.right
                if x == start:
                    break

        print("Heap elements:", end=" ")
        show(self.min)
        print()


heap = FibonacciHeap()

while True:
    print("\n1. Insert")
    print("2. Union")
    print("3. Extract-Min")
    print("4. Decrease-Key")
    print("5. Display")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        heap.insert(int(input("Enter value: ")))

    elif ch == 2:
        other = FibonacciHeap()
        n = int(input("Number of elements in second heap: "))
        for _ in range(n):
            other.insert(int(input("Enter value: ")))
        heap.union(other)
        print("Heaps united successfully")

    elif ch == 3:
        heap.extract_min()

    elif ch == 4:
        old = int(input("Enter existing value: "))
        new = int(input("Enter smaller value: "))
        heap.decrease_key(old, new)

    elif ch == 5:
        heap.display()

    elif ch == 6:
        break

    else:
        print("Invalid choice")