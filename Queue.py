#  there are 2 ways creating queue 
#  1 with list 
#  2 with LL 
 
#  1 with list 
 
 # Queue Data Structure
# Methods:
#     enqueue (insert)
#     dequeue (delete)
#     print (display all elements)
#     count (number of elements in the queue)
#     min (minimum value)
#     max (maximum value)
#     search (find an element)

class Queue:
    """Class to represent a queue data structure"""

    def __init__(self):
        self.queue = []  # Using a list to represent the queue

    def enqueue(self, data):
        """Insert an element at the end of the queue"""
        self.queue.append(data)

    def dequeue(self):
        """Remove and return the element from the front of the queue"""
        if not self.queue:
            print("Queue is empty, nothing to dequeue!")
            return None
        return self.queue.pop(0)

    def print_queue(self):
        """Print all elements in the queue"""
        if not self.queue:
            print("The queue is empty.")
            return
        print(" -> ".join(map(str, self.queue)))

    def count(self):
        """Return the number of elements in the queue"""
        return len(self.queue)

    def search(self, key):
        """Search for an element in the queue"""
        return key in self.queue

    def find_min(self):
        """Find and return the minimum value in the queue"""
        if not self.queue:
            print("Queue is empty, no minimum value.")
            return None
        return min(self.queue)

    def find_max(self):
        """Find and return the maximum value in the queue"""
        if not self.queue:
            print("Queue is empty, no maximum value.")
            return None
        return max(self.queue)


# Example usage:
if __name__ == "__main__":
    # Create an instance of Queue
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(5)
    q.enqueue(40)

    # Print the queue
    print("Queue:")
    q.print_queue()

    # Count elements in the queue
    print("\nCount of elements:", q.count())

    # Search for elements
    search_value = 20
    print(f"\nSearching for {search_value}: {'Found' if q.search(search_value) else 'Not Found'}")

    search_value = 50
    print(f"Searching for {search_value}: {'Found' if q.search(search_value) else 'Not Found'}")

    # Find the minimum value
    print(f"\nMinimum value in the queue: {q.find_min()}")

    # Find the maximum value
    print(f"Maximum value in the queue: {q.find_max()}")

    # Dequeue an element
    dequeued_value = q.dequeue()
    print(f"\nDequeued value: {dequeued_value}")

    # Print the queue after dequeuing
    print("\nQueue after dequeue:")
    q.print_queue()

    # Count elements after dequeuing
    print("\nCount of elements after dequeue:", q.count())


# with ll 


# Queue Data Structure using Linked List
# Methods:
#     enqueue (insert at the end)
#     dequeue (delete from the front)
#     print (display all elements)
#     count (number of elements in the queue)
#     min (minimum value)
#     max (maximum value)
#     search (find an element)

class Node:
    """Class to represent a node in the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class Queue:
    """Class to represent a queue using a linked list"""
    
    def __init__(self):
        self.front = None  # Pointer to the front of the queue
        self.rear = None   # Pointer to the rear of the queue
        self.size = 0      # Number of elements in the queue

    def enqueue(self, data):
        """Insert an element at the end of the queue"""
        new_node = Node(data)
        if self.rear is None:
            # If the queue is empty, set both front and rear to the new node
            self.front = self.rear = new_node
        else:
            # Link the current rear to the new node and update the rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the element from the front of the queue"""
        if self.front is None:
            print("Queue is empty, nothing to dequeue!")
            return None
        # Get the data from the front node and move the front pointer to the next node
        dequeued_value = self.front.data
        self.front = self.front.next
        # If the queue becomes empty, reset the rear pointer as well
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_value

    def print_queue(self):
        """Print all elements in the queue"""
        if self.front is None:
            print("The queue is empty.")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def count(self):
        """Return the number of elements in the queue"""
        return self.size

    def search(self, key):
        """Search for an element in the queue"""
        temp = self.front
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def find_min(self):
        """Find and return the minimum value in the queue"""
        if self.front is None:
            print("Queue is empty, no minimum value.")
            return None
        temp = self.front
        min_value = temp.data
        while temp:
            if temp.data < min_value:
                min_value = temp.data
            temp = temp.next
        return min_value

    def find_max(self):
        """Find and return the maximum value in the queue"""
        if self.front is None:
            print("Queue is empty, no maximum value.")
            return None
        temp = self.front
        max_value = temp.data
        while temp:
            if temp.data > max_value:
                max_value = temp.data
            temp = temp.next
        return max_value


# Example usage:
if __name__ == "__main__":
    # Create an instance of Queue
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(5)
    q.enqueue(40)

    # Print the queue
    print("Queue:")
    q.print_queue()

    # Count elements in the queue
    print("\nCount of elements:", q.count())

    # Search for elements
    search_value = 20
    print(f"\nSearching for {search_value}: {'Found' if q.search(search_value) else 'Not Found'}")

    search_value = 50
    print(f"Searching for {search_value}: {'Found' if q.search(search_value) else 'Not Found'}")

    # Find the minimum value
    print(f"\nMinimum value in the queue: {q.find_min()}")

    # Find the maximum value
    print(f"Maximum value in the queue: {q.find_max()}")

    # Dequeue an element
    dequeued_value = q.dequeue()
    print(f"\nDequeued value: {dequeued_value}")

    # Print the queue after dequeuing
    print("\nQueue after dequeue:")
    q.print_queue()

    # Count elements after dequeuing
    print("\nCount of elements after dequeue:", q.count())

