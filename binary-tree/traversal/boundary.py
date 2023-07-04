def boundry(root):
    if not root:
        return
    print(root, end='   ')
    left(root.left)
    print()
    right(root.right)
    print()
    leaf(root)


def left(root):
    if not root:
        return
    if(root.left or root.right):
        print(root, end= ' ')
    root=root.left
    left(root)

def right(root):
    if not root:
        return
    if(root.left or root.right):
        print(root, end= ' ')
    root=root.right
    right(root)

def leaf(root):
    if not root:
        return
    leaf(root.left)
    if not (root.left or root.right):
        print(root, end='   ')
    leaf(root.right)

'''
               10
          5            20 
      2     6     15        25


'''