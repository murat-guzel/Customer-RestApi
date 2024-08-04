class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next

# Create a linked list with one element
head = Node(1)

# Intentionally set head to None, simulating a "null pointer" scenario
head = None

# Attempt to print the list will raise an exception because head is None
try:
    print_list(head)
except AttributeError as e:
    print(f"Caught an exception: {e}")
