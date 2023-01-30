# create Node for linked list
class Node:

    # initializer for the node class
    def __init__(self, data):

        self.data = data
        self.next = None


# create a Linked_List class
class Linked_List:
    def __init__(self):
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        node1 = Node(80)
        self.head = node1

        node2 = Node(9)
        node1.next = node2

        node3 = Node(14)
        node2.next = node3

        node4 = Node(144)
        node3.next = node4

    def isSorted(self):

        # set current node to head node
        current = self.head
        # set a minimum value for the previous node
        prev_node = -234324

        # continue till end of linked list
        while current != None:
            # stop the loop if current is greater than prev_node
            if (current.data < prev_node):
                # return False if the list is not sorted in ascending order
                return False

            # assign the data of current node to prev_node
            prev_node = current.data

            # move current to succedding node
            current = current.next

        # return true if we reach end of the linked list, meaning the list is sorted in ascending order
        return True


linked_list = Linked_List()

# create linked list
linked_list.create_linked_list()

# check if the linked list is sorted
if linked_list.isSorted():
    print("Linked List is sorted")

else:
    print("Linked List is not sorted")
