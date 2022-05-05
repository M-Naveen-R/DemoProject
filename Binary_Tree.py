# Binary Tree



class Node:
    def __init__(self,x) -> None:
        self.left = None
        self.right = None
        self.data = x
        

def createbt():
    root = None
    val = int(input("Enter Data: "))
    if val == -1:
        return None
    root = Node(val)
    print(f'Enter value for left of {val} ')
    root.left = createbt()

    print(f'enter Value for Right of {val}')
    root.right = createbt()

    return root

# Height Of A Binary Tree
def height(root):
    if root == None:
        return 0

    return max(height(root.left),height(root.right)) + 1


# Size Of A Binary Tree

def size(root):
    if root == None:
        return 0

    return size(root.left)+size(root.right) + 1

# Maximum Value In A Binary Tree

def max_val(root):
    if root == None:
        return 0
    
    return max(root.data,   max(  max_val(root.left),  max_val(root.right)  )   )

# Binary Tree Traversals 
# 1 - Level Order Traversal

def levelorder(root):
    if root:
        levelorder(root.left)
        print(root.Data)
        levelorder(root.right)


# 2 - Pre Order Traversal

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

# 3 - Post Order Traversal

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)