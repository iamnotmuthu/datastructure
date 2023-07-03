def diag(root):
    if not root:
        return
    dict={}
    setboundval(dict,root,0)
    print(dict)

    keys=list(dict.keys())
    keys=sorted(keys, reverse=True)
    for k in keys:
        print(dict.get(k), end ='   ')

def setboundval(dict,root, val):
    if not root:
        return
    if val not in dict.keys():
        dict[val]=[]
    dict[val].append(root)
    setboundval(dict,root.left,val-1)
    setboundval(dict,root.right,val)
