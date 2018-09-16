class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inOrderPrint(root):
    if not root:
        return
    inOrderPrint(root.left)
    print(root.val)
    inOrderPrint(root.right)

def inOrderWithoutRecursion(root):
   node = root
   list = []
   counter = 0
   while( counter == 0):
       if node != None:
           list.append(node)
           node = node.left
       else:
           if len(list) > 0:
               node = list.pop()
               print(node.val)
               node = node.right
           else:
               counter = 1
   return


test = Node(8)
test.left = Node(3)
test.right = Node(10)
test.left.left = Node(1)
test.left.right = Node(6)
test.right.right= Node(14)
test.right.right.left = Node(13)
test.left.right.left = Node(4)
test.left.right.right = Node(15)

inOrderPrint(test)
inOrderWithoutRecursion(test)
