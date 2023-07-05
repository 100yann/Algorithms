class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        
        curr = self.root
        while curr:
            if curr.value == new_node.value:
                return False
            if new_node.value < curr.value:
                if curr.left is None:
                    curr.left = new_node
                    return True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    return True
                curr = curr.right

    def contains(self, value):
        curr = self.root
        while curr:
            if value < curr.value:
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                return True
        return False
                

            
bst = BinarySearchTree()
print(bst.root)
bst.insert(2)
bst.insert(1)
bst.insert(3)
print(bst.contains(2))