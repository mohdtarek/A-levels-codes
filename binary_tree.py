# Binary Tree

class Node:
    # Initializing the binary tree to create nodes. Left and right children are none by default
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # Function to insert a node
    def insert(self, value):
        # self.key is nothing but the root.
        if self.key is None:
            # by default the first value to be inserted will be the root node unless it's modified in the program
            self.key = value
            return

        # To ignore duplicates
        if self.key == value:
            pass

        elif value < self.key:  # Check the rules of binary tree
            if self.left:  # Evaluated to either true (present) or false (not present)
                self.left.insert(value)
            else:  # Otherwise a left child node will be created for the original root node
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    # Function to search in the tree
    def search(self, value):
        if value == self.key:
            print("Node is found")
            return
        if value < self.key:
            if self.left:
                # This will be the parameter to be passed to the function and then compared with the value
                self.left.search(value)
            else:
                print("Node is not present in the tree")
        else:
            if self.right:
                self.right.search(value)
            else:
                print("Node is not present in the tree")


root = Node(10)  # we can also set the root node manually
data = [6, 3, 1, 6, 98, 3, 7]
for nodes in data:
    root.insert(nodes)  # accessing the function insert() from class/TYPE Node

#--------------------------------------------------------------------------#
# The representation of the nodes in data will be as follows::::           #
#                                                                          #
#                                 10                                       #
#                                /  \                                      #
#                               6   98                                     #
#                             / \                                          #
#                            3   7                                         #
#                           /                                              #
#                          1                                               #
#--------------------------------------------------------------------------#

# Below code is just an illustarion for the code runner to see how the function works.
try:
    while True:
        opt = int(input("""
Choose an option:
1. Search for a node
2. exit    
> """))
        if opt == 1:
            node = int(input("Enter the node you are looking for: "))
            root.search(node)
        elif opt == 2:
            exit()
        # else:
        #     pass
except:
    print("Error")