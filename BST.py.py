# Binary Search Tree (BST)
# Methods:
#     insert
#     print (in-order traversal)
#     delete
#     count
#     min
#     max
#     search

class Node:
    """Class to represent a node in the binary search tree"""
    
    def __init__(self, data):
        self.data = data
        self.left = None   # Pointer to the left child
        self.right = None  # Pointer to the right child


class BinarySearchTree:
    """Class to represent the binary search tree"""
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a new node with the given data into the tree"""
        
        def _insert_recursive(current, data):
            if current is None:
                return Node(data)
            if data < current.data:
                current.left = _insert_recursive(current.left, data)
            else:
                current.right = _insert_recursive(current.right, data)
            return current
        
        self.root = _insert_recursive(self.root, data)

    def print_in_order(self):
        """Print the elements of the tree in in-order traversal"""
        
        def _in_order_traversal(current):
            if current is not None:
                _in_order_traversal(current.left)
                print(current.data, end=" ")
                _in_order_traversal(current.right)
        
        if self.root is None:
            print("The tree is empty.")
        else:
            _in_order_traversal(self.root)
            print()

    def delete(self, data):
        """Delete a node with the given value from the tree"""
        
        def _delete_recursive(current, data):
            if current is None:
                return current
            
            if data < current.data:
                current.left = _delete_recursive(current.left, data)
            elif data > current.data:
                current.right = _delete_recursive(current.right, data)
            else:
                # Node with only one child or no child
                if current.left is None:
                    return current.right
                elif current.right is None:
                    return current.left
                
                # Node with two children: Get the inorder successor (smallest in the right subtree)
                temp = self._find_min_node(current.right)
                current.data = temp.data
                # Delete the inorder successor
                current.right = _delete_recursive(current.right, temp.data)
            
            return current
        
        self.root = _delete_recursive(self.root, data)

    def count(self):
        """Return the count of nodes in the tree"""
        
        def _count_recursive(current):
            if current is None:
                return 0
            return 1 + _count_recursive(current.left) + _count_recursive(current.right)
        
        return _count_recursive(self.root)

    def search(self, key):
        """Search for a node with the given value"""
        
        def _search_recursive(current, key):
            if current is None:
                return False
            if current.data == key:
                return True
            if key < current.data:
                return _search_recursive(current.left, key)
            return _search_recursive(current.right, key)
        
        return _search_recursive(self.root, key)

    def find_min(self):
        """Find and return the minimum value in the tree"""
        
        if self.root is None:
            print("Tree is empty, no minimum value.")
            return None
        min_node = self._find_min_node(self.root)
        return min_node.data

    def find_max(self):
        """Find and return the maximum value in the tree"""
        
        if self.root is None:
            print("Tree is empty, no maximum value.")
            return None
        max_node = self._find_max_node(self.root)
        return max_node.data

    def _find_min_node(self, current):
        """Helper method to find the node with the minimum value"""
        
        while current.left is not None:
            current = current.left
        return current

    def _find_max_node(self, current):
        """Helper method to find the node with the maximum value"""
        
        while current.right is not None:
            current = current.right
        return current


# Example usage:
if __name__ == "__main__":
    # Create an instance of BinarySearchTree
    bst = BinarySearchTree()

    # Insert elements into the BST
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    bst.insert(5)
    bst.insert(15)
    bst.insert(25)
    bst.insert(35)

    # Print the BST in in-order traversal
    print("BST in-order traversal:")
    bst.print_in_order()

    # Count the number of nodes
    print("\nCount of nodes:", bst.count())

    # Search for elements
    search_value = 15
    print(f"\nSearching for {search_value}: {'Found' if bst.search(search_value) else 'Not Found'}")

    search_value = 50
    print(f"Searching for {search_value}: {'Found' if bst.search(search_value) else 'Not Found'}")

    # Find the minimum value
    print(f"\nMinimum value in the BST: {bst.find_min()}")

    # Find the maximum value
    print(f"Maximum value in the BST: {bst.find_max()}")

    # Delete a node
    delete_value = 20
    print(f"\nDeleting value: {delete_value}")
    bst.delete(delete_value)

    # Print the BST after deletion
    print("\nBST in-order traversal after deletion:")
    bst.print_in_order()

    # Count the nodes after deletion
    print("\nCount of nodes after deletion:", bst.count())
