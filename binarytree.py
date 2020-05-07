#!python

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        if self.left is not None or self.right is not None: return True
        return False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best case running time: O(1) - there is only the root node.
        worst case running time: O(n) - when you have to touch all the nodes."""
        left_height = right_height = 0
        # Check if left child has a value and if so calculate its height
        if self.left is not None:
            # calculate height
            left_height = 1 + self.left.height()
        # Check if right child has a value and if so calculate its height
        if self.right is not None:
            # calculate height
            right_height = 1 + self.right.height()
        # Return one more than the greater of the left height and right height
        return max(left_height, right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best case running time: O(1) if tree is really small like a couple of nodes that we need to traverse to find height
        worst case running time: because it depends how many nodes they are in to traverse"""
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(1) - if we find the node we're looking for at the root
        Worst case running time: O(log n) - if we have to traverse all the nodes to find the item we're looking for"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(1) - if we find the node we're looking for at the root
        Worst case running time: O(log n) - if we have to perform bin search to see if the item is in there"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        # return node.data if node.data is not None else None # <- ternary operator
        if node is not None:
            return node.data
        else: return None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(1)  If parent is found quickly when traversing
        Worst case running time: O(log n) because we have to find the parent. So n is the number of time we have to search to find parent"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            new_node = BinaryTreeNode(item)
            self.root = new_node
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_iterative(item)
        # TODO: Check if the given item should be inserted left of parent node
        if parent.data > item:
            # Create a new node and set the parent's left child
            new_node = BinaryTreeNode(item)
            parent.left = new_node
        # TODO: Check if the given item should be inserted right of parent node
        elif parent.data < item:
            # Create a new node and set the parent's right child
            new_node = BinaryTreeNode(item)
            parent.right = new_node
        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(1) under what conditions? - if the node we find is very early like the first few nodes
        Worst case running time: O(n) under what conditions? - because we have to traverse the nodes/ tree to find the node"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(1) under what conditions? - if the node we find is very early like the first few nodes
        Worst case running time: O(n) under what conditions? - because we have to traverse the nodes/ tree to find the node"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif item == node.data:
            return node # Return the found node
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node=node.left)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node=node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(1) under what conditions? - item we're looking for is at root
        Worst case running time: O(log n) under what conditions? - doing bin search to find the item and keeping track of previous item """
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # heck if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            if node.left is not None:
                node = node.left
            return self._find_parent_node_recursive(item, node, parent=node)  # Hint: Remember to update the parent parameter
        # TODO: Check if the given item is greater than the node's data
        elif node.right is not None:
            # TODO: Recursively descend to the node's right child, if it exists
            node = node.right
            return self._find_parent_node_recursive(item, node, parent=node)  # Hint: Remember to update the parent parameter

    def delete(self, item):
        pass
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Why and under what conditions? - visiting every node
        Memory usage: O(n) Why and under what conditions? - visiting every node"""
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        visit(node.data)
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        pass
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Why and under what conditions? - visiting every node
        Memory usage: O(n) Why and under what conditions? - visiting every node"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Why and under what conditions? - visiting every node
        Memory usage: O(n) Why and under what conditions? - visiting every node"""
        visit(node.data)
        if node.left:
            self._traverse_pre_order_recursive(node.left, visit)
        if node.right:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        pass
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Why and under what conditions? - visiting every node
        Memory usage: O(n) Why and under what conditions? - visiting every node"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Why and under what conditions? - visiting every node
        Memory usage: O(n) Why and under what conditions? - visiting every node"""
        if node.left:
            self._traverse_post_order_recursive(node.left, visit)
        if node.right:
            self._traverse_post_order_recursive(node.right, visit)
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        pass
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Why and under what conditions? - visiting every node
        Memory usage: O(n) Why and under what conditions? - visiting every node"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Why and under what conditions? - visiting every node
        Memory usage: O(n) Why and under what conditions? - visiting every node"""
        q = []
        q.append(start_node)
        while len(q) != 0:
            node = q.pop()
            visit(node.data)
            if node.left:
                q.insert(0, node.left) # en-q
            if node.right:
                q.insert(0, node.right) # en-q


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
