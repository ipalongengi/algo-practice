class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def insert(self, value):
        if self.root is None:
            self.set_root(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, current_node, value):
        if value < current_node.get_data(): 
            if current_node.left_child:
                self.insert_node(current_node.left_child, value)
            else:
                current_node.left_child = Node(value)
        else:
            if current_node.right_child:
                self.insert_node(current_node.right_child, value)
            else:
                current_node.right_child = Node(value)

    def insert_iter(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while current is not None:
                if value < current.get_data():
                    if current.left_child:
                        current = current.left_child
                    else:
                        current.left_child = Node(value)
                        return
                else:
                    if current.right_child:
                        current = current.right_child
                    else:
                        current.right_child = Node(value)
                        return

    def find(self, value):
        if self.root is None:
            raise ValueError("The BST is empty")
        else:
            return self.find_node(self.root, value)

    def find_node(self, current_node, value):
        if current_node is None:
            raise ValueError("The value does not exist in the BST")

        if value == current_node.get_data():
            return current_node
        elif value < current_node.get_data():
            self.find_node(current_node.left_child, value)
        else:
            self.find_node(current_node.right_child, value)

    def find_iter(self, value):
        if self.root is None:
            raise ValueError("The BST is empty")
        else:
            current = self.root
            while current is not None:
                if value == current.get_data():
                    return current
                elif value < current.get_data():
                    current = current.left_child
                else:
                    current = current.right_child

            if current is None:
                raise ValueError("The value is not found in the BST")

    def delete(self, value):
        if self.root is None:
            raise ValueError("The BST is empty")
        else:
            self.delete_node(self.root, value)
    
    def delete_node(self, current_node, value):
        if current_node is None:
            raise ValueError("The value does not exist in the BST")

        if value == current_node.data:
            # There are three cases to consider:
            # 1 - The current_node is a leaf
            # 2 - The current_node has only one child
            # 3 - The current_node has two children
            pass
        elif value < current_node.data:
            self.delete_node(current_node.left_child, value)
        else:
            self.delete_node(current_node.right_child, value)


# Print the nodes of the BST following the In Order Traversal Rule
def inOrderTraversal(node):
    if node:
        inOrderTraversal(node.left_child)
        print(node.data)
        inOrderTraversal(node.right_child)

