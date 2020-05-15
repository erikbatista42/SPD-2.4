from linkedlist import LinkedList

'''
Given a singly-linked list, find the middle value in the list.

Example: If the given linked list is A → B → C → D → E, return C.
Assumptions: The length (n) is odd so the linked list has a definite middle.

'''
def ll_middle_val(ll):
    # check if ll is empty
    if ll.length() == 0:
        return None
    # get middle index
    middle = ll.length() // 2
    counter = 0
    curr_node = ll.head

    # iterate middle(int) number of times and return the node's data
    while curr_node.next is not None and counter != middle:
        counter += 1
        curr_node = curr_node.next

    return curr_node.data


linked_list = LinkedList(["A","B","C","D","E"])
print(ll_middle_val(linked_list))


