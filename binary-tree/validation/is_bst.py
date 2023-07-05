def is_bst(root, min, max):
    if not root:
        return True
    if (root.left) and (root.val<root.left.val) :
            return False
    if (root.right) and (root.val>root.right.val):
            return False
    return (is_bst(root.left,0,root.val)) and is_bst(root.right,root.val,100)