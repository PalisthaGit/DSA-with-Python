# create Node for linked list
class Node:

    # initializer for the node class
    def __init__(self, data):
        # data of the node
        self.data = data
        # next node in the linked list
        self.next = None


# create a Linked_List class
class Linked_List:
    def __init__(self):
        # head of the linked list
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        # create 4 nodes with values 8, 8, 8 and 144
        node1 = Node(8)
        self.head = node1

        node2 = Node(8)
        node1.next = node2

        node3 = Node(8)
        node2.next = node3

        node4 = Node(144)
        node3.next = node4

    # remove duplicate from the linked list
    def remove_duplicate(self):
        # set current node to the head
        current = self.head
        # set next_node to the node after current
        next_node = current.next

        # loop through the linked list
        while next_node != None:
            # if data of current node is not equal to data of next_node
            if current.data != next_node.data:
                # move current to the next node
                current = next_node
                # set next_node to the node after current
                next_node = next_node.next

            # if data of current node is equal to data of next_node
            else:
                # set next node of current node to the node after next_node
                current.next = next_node.next
                # delete next_node
                del next_node
                # set next_node to the node after current node
                next_node = current.next

    # method to traverse through the linked list
    def traverse_list(self):
        # get a reference to the head of the list
        current = self.head

        # loop through the list until we reach the end
        while current is not None:

            # print the value of current node
            print(current.data)

            # move to the next node
            current = current.next


# create an instance of the linked list
linked_list = Linked_List()

# create linked list
linked_list.create_linked_list()

# remove duplicate from the linked list
linked_list.remove_duplicate()

# print linked list
linked_list.traverse_list()
