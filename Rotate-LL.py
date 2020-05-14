'''
What clarifying questions would you ask?
    • What data do the nodes hold?
    • Are the nodes data sorted?
    • Can I expect that K is > number of nodes? If so, what would you like me to return?
    • Can I expect to always be given in a linked list? Or can I expect a None value?

What reasonable assumptions could you state?
    • The nodes data holds integers
    • You could expect the K to sometimes be > than the number of nodes, if so return None
    • Return the modified linked list

What are 2-3 ways you can simplify the problem?
    • Think about the data structures you’ll need
    • Break down the edge cases 

Brainstorm 2-3 ways to approach the problem.
    • Start with Brute force approach
    • Use a queue/stack to store temp data

Choose one idea and write pseudocode for it.
    * start with brute force approach

'''
from linkedlist import LinkedList
import queue

def rotate_linked_list(ll, k):
    # return None if K > len(ll)
    if k > ll.length():
        return None

    # put first k items in a Queue
    counter = 0
    curr_node = ll.head

    q = queue.Queue()
    while curr_node.next is not None and counter != k:
        q.put(curr_node.data)
        curr_node = curr_node.next
        counter += 1
    
    # append all items in q
    while q.empty() == False:
        temp = q.get()
        ll.append(temp)

    # delete first k items in ll
    for _ in range(k):
        ll.pop_front()

    return ll.items()
    

linked_list = LinkedList([1,2,3,4,5,6])
example2_linked_list = LinkedList(["A","B","C","D","E","F"])
test = rotate_linked_list(linked_list, 2)
test2 = rotate_linked_list(example2_linked_list, 4)
print(test)
print(example2_linked_list)