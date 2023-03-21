class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the front-most item from the queue."""
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        """Returns the front-most item from the queue without removing it."""
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        """Returns True if the queue is empty, otherwise False."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)

        

# Create a new queue
my_queue = Queue()

# Add items to the queue
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Check the size of the queue
print(my_queue.size())  # Output: 3

# Check the front item of the queue
print(my_queue.front())  # Output: 10

# Remove the front item from the queue
my_queue.dequeue()

# Check the front item of the queue again
print(my_queue.front())  # Output: 20
