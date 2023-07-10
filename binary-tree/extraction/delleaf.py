def delleaf(root):
    if not root:
        return
    if isLeaf(root.left):
        root.left=None
    if isLeaf(root.right):
        root.right=None
    delleaf(root.left)
    delleaf(root.right)
    


def isLeaf(root):
    if not root:
        return False
    return not (root.left or root.right)
        

