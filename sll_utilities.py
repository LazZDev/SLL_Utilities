# Define a class for individual nodes in the linked list
class Node:
    def __init__(self, val):
        self.val = val  # Store the value of the node
        self.next = None  # Initialize the 'next' pointer to None


# Define a class for the linked list itself
class List:
    def __init__(self):
        self.head = (
            None  # Initialize the 'head' pointer to None, indicating an empty list
        )

    # Method to check if the linked list contains a node with a given value
    def contains(self, val):
        runner = self.head  # Start from the head of the linked list
        while runner:
            if runner.val == val:
                return True  # If a node with the given value is found, return True
            runner = runner.next
        return False  # Return False if the value is not found in the linked list

    # Method to calculate the length (number of nodes) in the linked list
    def length(self):
        runner = self.head  # Start from the head of the linked list
        length = 0  # Initialize a counter for the length
        while runner:
            length += 1  # Increment the length counter for each node encountered
            runner = runner.next
        return length

    # Method to create a string representation of the linked list
    def display(self):
        runner = self.head  # Start from the head of the linked list
        str_repr = ""  # Initialize an empty string to store the representation
        while runner:
            str_repr += f"{runner.val} -->"  # Append the value of the current node to the string
            runner = runner.next
        return str_repr
