import copy
import os
import sys

sys.path.insert(0, os.path.abspath('../'))

from bst import BST
from validation.is_bst import *
from validation.is_identical import *
from validation.is_mirror import *
from validation.is_subtree import *


def start_validation(root):
    print('validation starts')
    root2=copy.deepcopy(root)
    root2.left.left.val=9
    print('is identical tree ', is_identical(root,root2))
    print('is identical tree ', is_identical(root,root))

    mst=BST()
    mst.add(2)
    mst.add(1)
    mst.add(3)

    mst2=copy.deepcopy(mst)
    mst2.root.left.val=3
    mst2.root.right.val=1

    print()
    print('is mirror', is_mirror(mst.root,mst2.root))
    print('is mirror', is_mirror(mst.root,mst.root))


    print()
    print('isbst',is_bst(root,0,100))
    print('isbst',is_bst(mst2.root,0,100))

    print()
    print('is_sub_tree',is_sub_tree(root,root))
    print('is_sub_tree',is_sub_tree(root,root2))
