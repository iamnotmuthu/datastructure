def is_child_sum(root):
    if not root:
        return True
    if not (root.left or root.right):
        return True
    left= root.left.val if root.left else 0
    right=root.right.val if root.right else 0
    return (root.val==left+right) and is_child_sum(root.left) and (is_child_sum(root.right))