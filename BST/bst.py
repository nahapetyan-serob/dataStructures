class BST:
    class Node:
        def __init__(self, val=0):
            self.val = val
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __search(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        if node.val < val:
            return self.__search(node.right, val)
        else:
            return self.__search(node.left, val)

    def search(self, val):
        return self.__search(self.root, val)

    def __inorder_traverse(self, node):
        if not node:
            return
        self.__inorder_traverse(node.left)
        print(node.val)
        self.__inorder_traverse(node.right)

    def inorder_traverse(self):
        self.__inorder_traverse(self.root)

    def __preorder_traverse(self, node):
        if not node:
            return
        print(node.val)
        self.__preorder_traverse(node.left)
        self.__preorder_traverse(node.right)

    def preorder_traverse(self):
        self.__preorder_traverse(self.root)

    def __postorder_traverse(self, node):
        if not node:
            return
        print(node.val)
        self.__postorder_traverse(node.left)
        self.__postorder_traverse(node.right)

    def postorder_traverse(self):
        self.__postorder_traverse(self.root)

    def __get_min(self, node):
        if not node:
            return "Can't find minimum starting from None"
        if not node.left:
            return node
        else:
            return self.__get_min(node.left)

    def get_min(self):
        return self.__get_min(self.root)

    def __get_max(self, node):
        if not node:
            return "Can't find maximum starting from None"
        if not node.right:
            return node
        else:
            return self.__get_min(node.right)

    def get_max(self):
        return self.__get_max(self.root)

    def __get_height(self, node):
        if not node:
            return -1
        left = self.__get_height(node.left)
        right = self.__get_height(node.right)
        return max(left, right) + 1

    def get_height(self):
        return self.__get_height(self.root)

    def __insert(self, node, val):
        if not node:
            return self.Node(val)
        if node.val > val:
            node.left = self.__insert(node.left, val)
        else:
            node.right = self.__insert(node.right, val)
        return node
    def insert(self, val):
        self.root = self.__insert(self.root, val)

    def get_successor(self, node):
        if not node:
            return None
        if node.right:
            return self.__get_min(node.right)
        successor = None
        ancestor = self.root
        while ancestor != node:
            if node.val <= ancestor.val:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor

    def get_predecessor(self, node):
        if not node:
            return None
        if node.left:
            return self.__get_max(node.left)
        predecessor = None
        ancestor = self.root
        while ancestor != node:
            if node.val >= ancestor.val:
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left
        return predecessor

    def delete(self, val):
        self.root = self.__help_delete(self.root, val)

    def __help_delete(self, node, val):
        if not node:
            return None
        if node.val < val:
            node.right = self.__help_delete(node.right, val)
        elif node.val > val:
            node.left = self.__help_delete(node.left, val)
        else:
            if not node.left:
                return node.right

            elif not node.right:
                return node.left

            else:
                successor = self.__get_min(node.right)
                node.val = successor.val
                node.right = self.__help_delete(node.right, successor.val)

        return node





bst = BST()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(5)
bst.insert(15)
bst.insert(25)
bst.insert(40)
bst.insert(1)
bst.insert(7)
bst.insert(12)
bst.insert(17)
bst.insert(21)
bst.insert(28)
bst.insert(35)
bst.insert(50)
bst.inorder_traverse()
bst.delete(40)
print('New')
bst.inorder_traverse()
