def topview(root):
    if not root:
        return
    dict={}
    vert(root,0,dict)
    print(dict)
    for k in dict.keys():
        v=dict.get(k)
        if len(v)>1:
            print(v[0],v[-1])
        else:
            print(v[0])


def vert(root, l,dict):
    if not root:
        return
    if l in dict.keys():
         dict[l].append(root)
    else:
        dict[l]=[]
        dict[l].append(root)
   
    vert(root.left,l-1,dict)
    vert(root.right,l+1,dict)