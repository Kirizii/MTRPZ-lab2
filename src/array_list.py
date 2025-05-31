class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def append(self, element):
        self.data.append(element)

    def insert(self, element, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds")
        self.data.insert(index, element)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data.pop(index)

    def deleteAll(self, element):
        self.data = [x for x in self.data if x != element]

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

    def clone(self):
        cloned = ArrayList()
        cloned.data = self.data.copy()
        return cloned

    def reverse(self):
        self.data.reverse()

    def findFirst(self, element):
        try:
            return self.data.index(element)
        except ValueError:
            return -1

    def findLast(self, element):
        try:
            return len(self.data) - 1 - self.data[::-1].index(element)
        except ValueError:
            return -1

    def clear(self):
        self.data.clear()

    def extend(self, elements):
        self.data.extend(elements.data)