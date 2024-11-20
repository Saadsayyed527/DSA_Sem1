# Doubly Linked List
# Methods:
#     print
#     insert
#     delete
#     count
#     min
#     max
#     search

class Node:
    """Class to represent a node in the doubly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    """Class to represent the doubly linked list"""
    
    def __init__(self):
        self.head = None

    def add(self, data):
        """Add a new node with the given data to the end of the list"""
        
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        
        # Traverse to the last node
        last = self.head
        while last.next:
            last = last.next
        # Link the last node to the new node
        last.next = new_node
        new_node.prev = last

    def printing(self):
        """Print the elements of the list"""
        
        temp = self.head
        if not temp:
            print("The list is empty.")
            return
        while temp:
            # Go to the last and just print the data of every node
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def delete(self):
        """Delete the first node from the list and return its value"""
        
        if self.head is None:
            print("List is empty, nothing to delete!")
            return None
        popped_value = self.head.data
        if self.head.next:
            # Move the head pointer to the next node
            self.head = self.head.next
            self.head.prev = None  # Update the new head's previous pointer to None
        else:
            # If the list has only one node, make the head None
            self.head = None
        return popped_value

    def count(self):
        """Return the count of nodes in the list"""
        
        current = self.head
        count = 0
        # Traverse to the last node while counting
        while current:
            count += 1
            current = current.next
        return count

    def search(self, key):
        """Search for a node with the given value"""
        
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def find_min(self):
        """Find and return the minimum value in the list"""
        
        if self.head is None:
            print("List is empty, no minimum value.")
            return None
        
        min_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        
        return min_value

    def find_max(self):
        """Find and return the maximum value in the list"""
        
        if self.head is None:
            print("List is empty, no maximum value.")
            return None
        
        max_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Example usage:
if __name__ == "__main__":
    # Create an instance of DoublyLinkedList
    dll = DoublyLinkedList()

    # Add elements to the list
    dll.add(10)
    dll.add(20)
    dll.add(5)
    dll.add(40)

    # Print the list
    print("Doubly Linked List:")
    dll.printing()

    # Count elements in the list
    print("\nCount of nodes:", dll.count())

    # Search for elements
    search_value = 20
    print(f"\nSearching for {search_value}: {'Found' if dll.search(search_value) else 'Not Found'}")

    search_value = 50
    print(f"Searching for {search_value}: {'Found' if dll.search(search_value) else 'Not Found'}")

    # Find the minimum value
    print(f"\nMinimum value in the list: {dll.find_min()}")

    # Find the maximum value
    print(f"Maximum value in the list: {dll.find_max()}")

    # Delete the first element
    popped_value = dll.delete()
    print(f"\nDeleted value: {popped_value}")

    # Print the list after deletion
    print("\nDoubly Linked List after deletion:")
    dll.printing()

    # Count elements after deletion
    print("\nCount of nodes after deletion:", dll.count())
