# definition for singly-linked list
class Node:
    def __init__(self, data):
        """ initialize a new node with the given data """
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """ initialize a new linked list with no elements """
        self.head = None

    def append(self, data):
        """ append an element to the end of the linked list """
        # create a new node with the given data
        new_node = Node(data)

        # if the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # traverse to the end of the linked list
        current = self.head
        while current.next:
            current = current.next

        # append the new node to the end of the linked list
        current.next = new_node

    def traverse(self):
        """ traverse through the linked list and print each element """
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # method to concatenate two linked lists
    def concat(self, list2):

        # traverse till the end of first list
        current = self.head
        while current.next is not None:
            current = current.next

        # connect the last node of the first linked list with the head of the second linked list
        current.next = list2.head


# create a linked list
linked_list1 = LinkedList()

# append elements to the linked list
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)

# create a linked list
linked_list2 = LinkedList()

# append elements to the linked list
linked_list2.append(5)
linked_list2.append(6)
linked_list2.append(7)
linked_list2.append(8)

# concat linkedlist
linked_list1.concat(linked_list2)

# traverse through the linked list and print each element
linked_list1.traverse()
