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


    # insert node in linked list
    def insert_node(self, index, x):

        if index < 1 or index > self.count_elements():
            return

        if index == 1:
            # create a new node
            new_node = Node(x)

            # make it point to head node
            new_node.next = self.head

            # make head point to new node
            self.head = new_node
        
        else:
            # Adding a new node with value 'x' at index 'index' in the linked list
            new_node = Node(x)

            # Start at the head of the list
            current = self.head

            # Traverse the list to the position before the desired index
            for i in range(0, index-1):
                current = current.next

            # Set the new node's next pointer to the current node's next pointer
            new_node.next = current.next

            # Set the current node's next pointer to the new node
            current.next = new_node
    
    
    def delete_node(self, index):
        # take pointer for the previous node
        prev_node = None
        deleted_data = -1

        # check if the given index is valid or not
        if index < 1 or index > self.count_elements():
            return -1

        # delete the first node
        if index == 1:
            # make prev_node point to the first node
            prev_node = self.head
            # store the data of first node to deleted_data
            deleted_data = self.head.data

            # move head pointer to the next node
            self.head = self.head.next

            # delete the node we want to delete
            del prev_node

            return deleted_data

        else:
            # if the node is not the first node
            current = self.head
            for i in range(index - 1):
                # move prev_node to current
                prev_node = current
                current = current.next

            # remove the current node logically from the linked list
            prev_node.next = current.next
            # take the data of current
            deleted_data = current.data
            #delete current
            del current
            # return the deleted data
            return deleted_data


# create object of linked list
linked_list = Linked_List()



# create linked list
linked_list.create_linked_list()

#delete
linked_list.delete_node(2)
# print linked list
linked_list.traverse_list()