from extraction.height import *

def diameter(root):
    if not root:
        return 0
    left=h(root.left)
    right=h(root.right)
    d=left+right+1
    cd= max(diameter(root.left),diameter(root.right))
    return max(d,cd)