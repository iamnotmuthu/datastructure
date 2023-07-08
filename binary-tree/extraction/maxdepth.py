def depth(root):
    if not root:
        return 0
    return max(depth(root.left)+1,depth(root.right)+1)