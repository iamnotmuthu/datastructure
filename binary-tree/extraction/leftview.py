def leftview(root):
    if not root:
        return
    dict ={}
    left(root,0,dict)


def left(root,l,dict):
    if not root:
        return
    key= dict.get(l)
    if not key:
        print(root)
    dict[l]=root
    left(root.left,l+1,dict)
    left(root.right,l+1,dict)
    