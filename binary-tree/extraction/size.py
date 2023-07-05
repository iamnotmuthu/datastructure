def size(root):
    if not root:
        return 0
    return size(root.left)+1+size(root.right)
   