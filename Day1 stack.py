class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the top-most item from the stack."""
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """Returns the top-most item from the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """Returns True if the stack is empty, otherwise False."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)

# Create a new stack
my_stack = Stack()

# Add items to the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Check the size of the stack
print(my_stack.size())  # Output: 3

# Check the top item of the stack
print(my_stack.peek())  # Output: 30

# Remove the top item from the stack
my_stack.pop()

# Check the top item of the stack again
print(my_stack.peek())  # Output: 20
