from singly_linked_list import LinkedList

class StackFromArray:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):

        if self.size > 0:
            self.size -= 1
            return self.storage.pop()

class StackFromLinkedList:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size


    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):

        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

class Stack(StackFromArray):
    def __init__(self):
        super().__init__()