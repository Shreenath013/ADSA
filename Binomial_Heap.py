class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


class BinomialHeap:
    def __init__(self):
        self.head = None

    def merge(self, h1, h2):
        dummy = Node(0)
        tail = dummy

        while h1 and h2:
            if h1.degree <= h2.degree:
                tail.sibling, h1 = h1, h1.sibling
            else:
                tail.sibling, h2 = h2, h2.sibling
            tail = tail.sibling

        tail.sibling = h1 or h2
        return dummy.sibling

    def link(self, y, z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def union(self, other):
        self.head = self.merge(self.head, other.head)
        other.head = None

        if not self.head:
            return

        prev = None
        curr = self.head
        nxt = curr.sibling

        while nxt:
            if (curr.degree != nxt.degree or
                (nxt.sibling and nxt.sibling.degree == curr.degree)):
                prev, curr = curr, nxt
            elif curr.key <= nxt.key:
                curr.sibling = nxt.sibling
                self.link(nxt, curr)
            else:
                if prev:
                    prev.sibling = nxt
                else:
                    self.head = nxt
                self.link(curr, nxt)
                curr = nxt

            nxt = curr.sibling

    def insert(self, key):
        temp = BinomialHeap()
        temp.head = Node(key)
        self.union(temp)

    def extract_min(self):
        if not self.head:
            print("Heap is empty")
            return

        prev_min = None
        minimum = self.head
        prev = None
        curr = self.head

        while curr:
            if curr.key < minimum.key:
                minimum = curr
                prev_min = prev
            prev = curr
            curr = curr.sibling

        if prev_min:
            prev_min.sibling = minimum.sibling
        else:
            self.head = minimum.sibling

        child = minimum.child
        rev = None

        while child:
            nxt = child.sibling
            child.sibling = rev
            child.parent = None
            rev = child
            child = nxt

        temp = BinomialHeap()
        temp.head = rev
        self.union(temp)

        print("Extracted minimum:", minimum.key)

    def display(self):
        def show(node):
            while node:
                print(node.key, end=" ")
                show(node.child)
                node = node.sibling

        print("Heap elements:", end=" ")
        show(self.head)
        print()


heap = BinomialHeap()

while True:
    print("\n1. Insert")
    print("2. Union with another heap")
    print("3. Extract-Min")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        heap.insert(int(input("Enter value: ")))

    elif ch == 2:
        other = BinomialHeap()
        n = int(input("Number of elements in second heap: "))

        for _ in range(n):
            other.insert(int(input("Enter value: ")))

        heap.union(other)
        print("Heaps united successfully")

    elif ch == 3:
        heap.extract_min()

    elif ch == 4:
        heap.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice")