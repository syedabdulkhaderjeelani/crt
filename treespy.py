class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
    def inorder_traversal(self,Node):
        if Node:
            self.inorder_traversal(Node.left)
            print("inorder_traversal=",Node.data)
            self.inorder_traversal(Node.right)
    def preorder_traversal(self,Node):
        if Node:
            print("preorder_traversal=",Node.data)
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)
    def postorder_traversal(self,Node):
        if Node:
            self.postorder_traversal(Node.left)
            self.postorder_traversal(Node.right)
            print("postorder_traversal=",Node.data)
    def sum_of_Nodes(self,Node):
        if Node is None:
            return 0
        return Node.data + self.sum_of_Nodes(Node.left)+self.sum_of_Nodes(Node.right)


    def height(self,Node):
        if Node is None:
            return 0
        else:
            return 1+max(self.height(Node.left),self.height(Node.right))

tree = Node()

tree.data = 1             #root node
tree.left=Node()
tree.left.data=2
tree.right=Node()
tree.right.data=3
tree.left.left=Node()
tree.left.left.data=4
tree.left.right=Node()
tree.left.right.data=5
print(tree.data)
print(tree.left.data)
print(tree.right.data)
print(tree.left.left.data)
print(tree.left.right.data)
tree.inorder_traversal(Node=tree)
tree.preorder_traversal(Node=tree)
tree.postorder_traversal(Node=tree)
print(tree.sum_of_Nodes(Node=tree))
print(tree.height(Node=tree))


