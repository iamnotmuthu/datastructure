import copy

from traversal.main import start_traversal
from extraction.main import start_analysis

from validation.main import *

from bst import BST
bst=BST()

'''
               10
          5            20 
      2     6     15        25


'''

print('tree construction started')
bst.add(10)
bst.add(20)
bst.add(5)
bst.add(2)
bst.add(6)
bst.add(15)
bst.add(25)
bst.add(7)
print('tree constructed')
## tree construction over

start_traversal(bst.root)
start_analysis(bst.root)
start_validation(bst.root)


