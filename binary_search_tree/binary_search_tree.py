"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BinarySearchTree class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BinarySearchTree class.
"""
from queue import QueueFromArray as Queue
from stack import StackFromLinkedList as Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if value < self.value:

            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
            
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    def contains(self, target):
        if self.value == target:
            return True
        
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        
        else:
            if self.right:
                return self.right.contains(target)

        return False


    def get_max(self):
        current_node = self

        while current_node.right:
            current_node = current_node.right
        
        return current_node.value


    def for_each(self, fn):
        
        fn(self.value)
                
        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        
        print(node.value)

        if self.right:
            self.right.in_order_print(self.right)
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while len(queue) > 0:
            next_in_line = queue.dequeue()
            print(next_in_line.value)

            if next_in_line.left:
                queue.enqueue(next_in_line.left)
            
            if next_in_line.right:
                queue.enqueue(next_in_line.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while len(stack) > 0:
            last_added = stack.pop()
            print(last_added.value)

            if last_added.right:
                stack.push(last_added.right)
              
            if last_added.left:
                stack.push(last_added.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            self.pre_order_dft(node.left)

        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)

        if node.right:
            self.post_order_dft(node.right)

        print(node.value)