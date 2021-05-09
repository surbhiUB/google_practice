class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def printLevelOrder(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while (len(queue)>0):

        print(queue[0].key)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)
        
def preOrder(root):
    if root:
        print(root.key)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printLevelOrder(root)
inOrder(root)
preOrder(root)
postOrder(root)

