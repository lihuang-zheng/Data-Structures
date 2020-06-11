from singly_linked_list import LinkedList
from stack import Stack


class QueueFromArray:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if (self.size > 0):
            first_in_line = self.storage[0]

            self.storage = self.storage[1:]
            self.size -= 1

            return first_in_line


class QueueFromLinkedList:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_end(value)
        self.size += 1

    def dequeue(self):
        if (self.size > 0):
            self.size -= 1
            return self.storage.remove_from_head()


class QueueFromStack:
    def __init__(self):
        self.size = 0
        self.storage = Stack()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        next_stack = Stack()
        next_stack.push(value)

        self.storage.push(next_stack)
        pass

    def dequeue(self):
        all_other_items = self.storage.pop()
        first_in_line = self.storage.pop()

        self.size -= 1

        self.storage = all_other_items

        return first_in_line


class Queue(QueueFromLinkedList):
    def __init__(self):
        super().__init__()
