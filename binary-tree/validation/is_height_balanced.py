from extraction.height import *

def is_balanced(root):
    if not root:
        return True
    lh=h(root.left)
    rh=h(root.right)
    return abs(lh-rh)<=1 and is_balanced(root.left) and is_balanced(root.right)