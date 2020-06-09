"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
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
