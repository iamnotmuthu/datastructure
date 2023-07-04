import copy

from traversal.preorder import *
from traversal.inorder import *
from traversal.postorder import *
from traversal.bfs import *
from traversal.vertical import *
from traversal.zigzag import *
from traversal.diagnol import *
from traversal.boundary import *

from analysis.height import *
from analysis.size import *

from validation.identical import *

from bst import BST
bst=BST()


'''
               10
          5            20 
      2     6     15        25


'''

bst.add(10)
bst.add(20)
bst.add(5)
bst.add(2)
bst.add(6)
bst.add(15)
bst.add(25)
bst.add(7)
print('bst added')
## tree construction over


# traversal begins
pre(bst.root)
print()
preiter(bst.root)
print()
preiter_opt(bst.root)
print()
print('pre order over')

#preorder over

ino(bst.root)
print()
inoiter(bst.root)
print()
print('inorder over')

post(bst.root)
print()
postiter(bst.root)
print()
print('post order over')

bfs(bst.root)
print()
print('bfs over')

vert(bst.root)
print()
print('vertical over')
zz(bst.root)

print()
print('zigzag over')

diag(bst.root)
print()
print('diagnol over')

boundry(bst.root)
print()
print('traversal over')
print()
print()


print('analysis starts')
print('size is ',size(bst.root))
print('height is ',h(bst.root))
print('analysis over')
print()
print()

print('validation starts')
bst2=copy.deepcopy(bst)
bst2.root.left.left.val=9
print('is identical tree ', is_identical(bst.root,bst2.root))

