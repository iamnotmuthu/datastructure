def vert(root):
    if not root:
        return
    dict={}
    setdict(root,0,dict)
    print('dictionary values are ',dict)
    keys=list(dict.keys())
    keys.sort()
    for k in keys:
        print(dict.get(k), end='    ')
    


def setdict(root,val,dict):
    if not root:
        return
    if val in dict.keys():
        dict[val].append(root)
    else:
        dict[val]=[]
        dict[val].append(root)
    setdict(root.left,val-1,dict)
    setdict(root.right,val+1,dict)

    