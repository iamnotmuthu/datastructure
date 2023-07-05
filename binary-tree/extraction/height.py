def h(root):
    if not root:
        return 0
    return max(h(root.left),h(root.right))+1