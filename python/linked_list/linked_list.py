# LINKED LIST IMPLEMENTATION

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """ Get the data stored in the Node."""
        return self.data

    def get_next_node(self):
        """ Get the next node."""
        return self.next_node

    def set_next_node(self, new_next_node):
        """ Set the next node for the Node."""
        self.next_node = new_next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """
        Create a new Node and insert it at the front of the linked list

        Keyword Argument:
        data -- the value to be inserted to be inserted to the linked list
        """
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def size(self):
        """
        Return the size of the linked list
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next_node()

        return count

    def search(self, data):
        """
        Search the data inside the linked list and return the first Node 
        where it is found. Otherwise, a ValueError exception is raised 

        Keyword Argument:
        data -- the value to be searched in the linked list`
        """
        current = self.head

        while current:
            if current.get_data() == data:
                return current 
            else:
                current = current.get_next_node()

        if current is None:
            raise ValueError("Data not in the list")

    def delete(self, data):
        """
        Delete the first Node that contains data from the linked list

        Keyword Atgument:
        data -- the value to be deleted from the linked list
        """
        current = self.head
        previous = None

        while current:
            if current.get_data() == data:
                if previous is None:
                    self.head = current.get_next_node()
                else:
                    previous.set_next_node(current.get_next_node())
            else:
                current = current.get_next_node()

        if current is None:
            raise ValueError("Data not in the list")


def printLinkedList(node):
    current = node.head
    while current:
        print(current.get_data())
        current = current.get_next_node()

