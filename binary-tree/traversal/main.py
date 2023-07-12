import sys
import os

from traversal.preorder import *
from traversal.inorder import *
from traversal.postorder import *
from traversal.bfs import *
from traversal.vertical import *
from traversal.zigzag import *
from traversal.diagnol import *
from traversal.boundary import *
from traversal.ino_suc import *




def start_traversal(root):
    print('traversal begins')
    print('recursive preorder traversal')
    pre(root)
    print()
    print('iterative preorder traversal')
    preiter(root)
    print()
    print('optimized iterative preorder traversal')
    preiter_opt(root)
    print()
    print('pre order traversal over')
    print()

    print('inorder traversal begins')  
    print('recursive inorder traversal')
    ino(root)
    print()
    print('iterative inorder traversal')
    inoiter(root)
    print()
    print('inorder over')
    print()


    print('postorder traversal begins')
    print('recursive postorder traversal')
    post(root)
    print()
    print('iterative postorder traversal')
    postiter(root)
    print()
    print('post order over')
    print()

    print('iterative bfs traversal')
    bfs(root)
    print()
    print('bfs over')
    print()

    print('vertical order traversal')
    vert(root)
    print()
    print('vertical over')
    print()

    print('zig zag traversal')
    zz(root)
    print()
    print('zigzag over')
    print()


    print('diagnol traversal')
    diag(root)
    print()
    print('diagnol traversal over')
    print()

    print('boundry traversal')
    boundry(root)
    print()
    print('boundry traversal over' )
    print()

    print('ino_suc',ino_suc(root,5))

    print('all traversal over')
    

