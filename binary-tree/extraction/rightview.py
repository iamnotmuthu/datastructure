def rightview(root):
    if not root:
        return
    dict ={}
    right(root,0,dict)
    for key in dict.keys():
        print(dict.get(key), end = '    ')



def right(root,l,dict):
    if not root:
        return
    key= dict.get(l)
    dict[l]=root
    right(root.left,l+1,dict)
    right(root.right,l+1,dict)
    