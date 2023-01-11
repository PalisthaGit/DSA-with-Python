# create Node for linked list
class Node:

    # initializer for the node class
    def __init__(self, data):

        # intialize the data field with the data in argument
        self.data = data

        # intialize the next field to None
        self.next = None


# create a Linked_List class
class Linked_List:
    def __init__(self):
        #intitalize the head field to None
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        # create first node
        node1 = Node(80)
        # set head field to the first node
        self.head = node1

        # create second node
        node2 = Node(9)
        #link first and second nodes
        node1.next = node2

        # create third node
        node3 = Node(14)
        #connect second and third node
        node2.next = node3

    # method to traverse through the linked list
    def traverse_list(self):
        # get a reference to the head of the list
        current = self.head

        # loop through the list until we reach the end
        while current is not None:
            
            # print the value of current node
            print(current.data)

            #move to the next node
            current = current.next

# count elements in linked list
def count_elements(current):
    # initialize a variable to store the count
    count = 0
    # iterate through the linked list while the current pointer is not None
    while current is not None:
        # increment the count for each iteration
        count += 1
        # move to the next element in the linked list
        current = current.next
    # return the final count of elements in the linked list
    return count

#create object of linked list
linked_list = Linked_List()


# create linked list
linked_list.create_linked_list()
# print count
print(count_elements(linked_list.head))


