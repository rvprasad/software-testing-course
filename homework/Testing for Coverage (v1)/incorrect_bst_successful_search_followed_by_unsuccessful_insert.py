import copy


class Node(object):
    "Represents a node in a BST"
    
    def __init__(self, key, left, right):
        """Initializes a Node instance
        
        Args:
            key: a comparable value stored in the node
            left: child of the node
            right: child of the node
        """
        self._key = key
        self._left = left
        self._right = right
    
    @staticmethod
    def make_copy(node):
        "Returns a shallow copy of this node"
        return Node(node._key, node._left, node._right) # can be copy.copy(self)
    
    @property
    def key(self):
        "Returns the key of this node"
        return self._key
    
    @property
    def left(self):
        "Returns the left child of this node"
        return copy.copy(self._left)  # should be return self._left
    
    @property    
    def right(self):
        "Returns the left child of this node"
        return copy.copy(self._right)  # should be return self._right
    
    # required to make the documentation of properties consistent with
    # their implementations
    #
    # def __eq__(self, other):
    #     if isinstance(other, Node):
    #         tmp1 = (not self.left and not other.left) or \
    #             self.left.key == other.left.key
    #         tmp2 = (not self.right and not other.right) or \
    #             self.right.key == other.right.key
    #         return tmp1 and tmp2 and self.key == other.key
        
        
class BST(object):
    "Represents a homogeneous BST that stores comparable values"
    
    def __init__(self):
        "Initializes a BST instance"
        self._root = None

    @staticmethod
    def __search(node, value):
        """Helper method to find a value in this node or its children
        
        Args:
            node: to be searched for the value
            value: to find
        
        Return:
            True if the value is present in the given node or its children
            False otherwise
        """
        if node:
            if node.key == value:
                return True
            else:
                if value < node.key:
                    return BST.__search(node._left, value)
                else:
                    return BST.__search(node._right, value)
        else:
            return False
            
    def search(self, value):
        """Find the value in this tree
        
        Args:
            value: to find in this tree
            
        Return:
            True if value is present in this tree
            False otherwise
        """
        return BST.__search(self._root, value)
        
    def insert(self, value):
        """Insert the value in this tree
        
        Args:
            value: to insert into this tree
            
        Return:
            True if value was inserted into this tree
            False if value was already present in this tree
        """
        if self._root:
            node = self._root
            child = self._root
            parent = None
            while node and child:
                if node.key == value:
                    child = None
                else:
                    parent = node
                    if value < node.key:
                        node = node._left
                    else:
                        node = node._right
            if child:
                child = Node(value, None, None)
                if value < parent.key:
                    parent._left = child
                else:
                    parent._right = child
            return True
        else:
            self._root = Node(value, None, None)
            return True
        
    def delete(self, value):
        """Delete the value from this tree
        
        Args:
            value: to be deleted from this tree
            
        Return:
            True if value was deleted from this tree
            False if value was not present in this tree
        """
        node = self._root
        parent = None
        while node and node.key != value:
            parent = node;
            if value < node.key:
                node = node._left
            else:
                node = node._right
        
        if not node:
            return False
        
        if not node._left:
            if node == self._root:
                self._root = self._root.right
            else:
                if value <= parent.key:
                    parent._left = node._right
                else:
                    parent._right = node._right
        elif not node._right:
            if node == self._root:
                self._root = self._root.left
            else:
                if value <= parent.key:
                    parent._left = node._left
                else:
                    parent._right = node._left
        else:
            node1 = node._left
            parent1 = node
            while node1._right:
                parent1 = node1
                node1 = node1._right
            if node == self._root:
                if parent1 == self._root:
                    self._root._key = node1.key
                    self._root._left = node1._left
                else:
                    parent1._right = node1._left
                    self._root._key = node1.key
            else:
                node._key = node1.key
                if parent1 == node:
                    parent1._left = node1._left
                else:
                    parent1._right = node1._left
        return True

    @property
    def root(self):
        "Returns a copy of the root node in this BST"
        if self._root:
            return Node.make_copy(self._root)
        else:
            return None

