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
        # intitalize the head field to None
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        # create first node
        node1 = Node(80)
        # set head field to the first node
        self.head = node1

        # create second node
        node2 = Node(9)
        # link first and second nodes
        node1.next = node2

        # create third node
        node3 = Node(14)
        # connect second and third node
        node2.next = node3

        # create third node
        node4 = Node(144)
        # connect second and third node
        node3.next = node4

        # create third node
        node5 = Node(14444444444)
        # connect second and third node
        node4.next = node5

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
    
    # count elements in linked list
    def count_elements(self):
        # initialize a variable to store the count
        count = 0
        current = self.head
        # iterate through the linked list while the current pointer is not None
        while current is not None:
            # increment the count for each iteration
            count += 1
            # move to the next element in the linked list
            current = current.next
        # return the final count of elements in the linked list
        return count
    
    def find_max(self):
        # create a variable to store current node
        current = self.head
        # create a variable to store the max value
        max = 0

        # iterate through the linked list
        for i in range(0, self.count_elements()):
            # compare the data of the current node to the max value
            if current.data > max:
                # update the max value if the current node's data is greater
                max = current.data

            # move to the next node
            current = current.next
        # return the max value
        return max

# create object of linked list
linked_list = Linked_List()

# create linked list
linked_list.create_linked_list()

#print max
max = linked_list.find_max()
print(max)