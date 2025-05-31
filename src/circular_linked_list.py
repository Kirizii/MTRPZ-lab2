class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        if not self.head:
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert(self, element, index):
        if index < 0 or index > self.length():
            raise IndexError("Index out of bounds")
        new_node = Node(element)
        if index == 0:
            if not self.head:
                self.head = new_node
                new_node.next = self.head
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                new_node.next = self.head
                self.head = new_node
                last.next = self.head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Index out of bounds")
        if index == 0:
            data = self.head.data
            if self.head.next == self.head:
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = self.head.next
                last.next = self.head
            return data
        current = self.head
        for _ in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        return data
