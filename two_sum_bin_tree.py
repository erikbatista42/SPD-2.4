# Given a binary search tree containing integers and a target integer, 
# come up with an efficient way to locate two nodes in the tree whose sum is 
# equal to the target value.

from binarytree import BinaryTreeNode, BinarySearchTree

def two_sum_bin_tree(tree, target):
    # * Check for edge cases
    if target == None or tree.size == 0:
        return None

    # perform in order operation, add each number it visits to an array
    numbers = tree.items_in_order()
    # start, end vars
    start = 0
    end = len(numbers) -1

    while start < end:
        # calculate total
        curr_total = numbers[start] + numbers[end]

        if curr_total == target:
            return [numbers[start], numbers[end]]
        elif curr_total > target:
            end -=1 
        else:
            # increase total 
            start += 1
    return [] # Doesn't exist
    

tree_one = BinarySearchTree([10, 7, 14, 5, 8, 6, 11, 12])
tree_two = BinarySearchTree([7, 14, 5, 8, 6])
tree_three = BinarySearchTree([10, 7, 14, 5, 8, 6, 11, 12])

test_one = two_sum_bin_tree(tree_one, 21)
test_two = two_sum_bin_tree(tree_one, 14)
test_three = two_sum_bin_tree(tree_one, 0)

print(test_three)
