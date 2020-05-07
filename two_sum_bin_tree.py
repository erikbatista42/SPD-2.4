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
        # caculate total
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



# -------

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge two arrays
        merged_nums = self.merge(nums1, nums2)
        mid_index = len(merged_nums) //2
        # find the middle of the arrays, if its odd, go to the index at length //2 and get the value at that index
        if len(merged_nums) % 2 == 1:
            return merged_nums[mid_index]
        # if its even, go to the index at length //2 and get the value at that index and at that index - 1 and then divide those values by 2
        return (merged_nums[mid_index] + merged_nums[mid_index - 1])/2
        
    # merge function from merge sort       
    def merge(self, nums_1, nums_2): # O(n + m)
        result = []
        index_1 = 0
        index_2 = 0
        
        while index_1 < len(nums_1) and index_2 < len(nums_2):
            if nums_1[index_1] < nums_2[index_2]:
                result.append(nums_1[index_1])
                index_1 += 1
            else:
                result.append(nums_2[index_2])
                index_2 += 1
        if index_1 < len(nums_1):
            result.extend(nums_1[index_1:])
        else:
            result.extend(nums_2[index_2:])