class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev_node = None
        self.next_node = None

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev_node

    def get_next(self):
        return self.next_node

    def set_prev(self, node):
        self.prev_node = node

    def set_next(self, node):
        self.next_node = node


class DoubleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def size(self):
        """
        Return the size of the linked list
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def insert(self, data):
        """
        Create a new node containing the data and 
        insert it at the front of the linked list

        Keyword Argument
        data -- the value to be inserted into the linked list
        """
        current = self.head
        new_node = Node(data)

        if current:
            current.set_prev(new_node)
            new_node.set_next(current)

        self.head = new_node

    def delete(self, data):
        """
        Delete the first instance of a node with data as its value.
        If the data is not found in the linked list, a ValueError exception
        is raised.

        Keyword Argument:
        data -- the value to be deleted from the linked list
        """
        current = self.head

        while current:
            if current.get_data() == data:
                # The data is found at the head of the DLL
                if current.get_prev() is None:
                    current.get_next().set_prev(None)
                    self.head = current.get_next()
                
                # The data is found at the tail of the DLL
                elif current.get_next() is None:
                    current.get_prev().set_next(None)

                else:
                    current.get_prev().set_next(current.get_next())
                    current.get_next().set_prev(current.get_prev())
                return
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data is not found!")

    def search(self, data):
        """
        Search for the first instance of data in the linked list and return 
        the Node object if the data is found or raise a ValueError exception
        otherwise.

        Keyword Argument:
        data -- the value to be deleted from the linked list
        """
        current = self.head

        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data is not found!")


def printLinkedList(node):
    current = node.head

    while current:
        print(current.get_data())
        current = current.get_next()

