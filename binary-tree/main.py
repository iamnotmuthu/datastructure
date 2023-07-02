from traversal.preorder import *
from bst import BST
bst=BST()


'''
               10
          5          20 
      2     6     15    25


'''

bst.add(10)
bst.add(20)
bst.add(5)
bst.add(2)
bst.add(6)
bst.add(15)
bst.add(25)
print('bst added')
pre(bst.root)
print()
preiter(bst.root)