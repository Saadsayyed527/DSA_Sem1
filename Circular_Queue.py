class Node:
    """Node class for the circular queue"""
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    """Circular Queue implementation using Linked List"""
    def __init__(self):
        self.tail = None  # Tail pointer for the circular queue
        self.size = 0     # To track the number of elements in the queue

    def is_empty(self):
        """Check if the queue is empty"""
        return self.tail is None

    def enqueue(self, data):
        """Add an element to the rear of the queue"""
        new_node = Node(data)
        if self.is_empty():
            # If the queue is empty, point the new node to itself
            new_node.next = new_node
            self.tail = new_node
        else:
            # Insert the new node at the rear and maintain the circular link
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the front element of the queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        head = self.tail.next  # Front element
        if self.tail == head:
            # Only one element in the queue
            self.tail = None
        else:
            # Remove the front element and update the tail's next pointer
            self.tail.next = head.next
        self.size -= 1
        return head.data

    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.tail.next.data

    def get_size(self):
        """Return the size of the queue"""
        return self.size

    def print_queue(self):
        """Print all elements of the circular queue"""
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.tail.next
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.tail.next:  # Stop when we return to the front
                break
        print("(back to front)")

# Example usage
if __name__ == "__main__":
    cq = CircularQueue()

    # Enqueue elements
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)

    # Print the queue
    print("Circular Queue elements:")
    cq.print_queue()

    # Front element
    print("Front element:", cq.peek())

    # Dequeue elements
    print("Dequeued element:", cq.dequeue())
    print("Dequeued element:", cq.dequeue())

    # Print the queue after dequeues
    print("Circular Queue after dequeues:")
    cq.print_queue()

    # Size of the queue
    print("Size of Circular Queue:", cq.get_size())
