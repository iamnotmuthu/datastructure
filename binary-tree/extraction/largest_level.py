def largest_level(root):
    if not root:
        return 0
    print(root, end='   ')
    s=[]
    s.append(root)
    s.append(None)
    while(s):
        root=s.pop(0)
        if root:
            if root.left:
                 s.append(root.left)
            if root.right:
                s.append(root.right)
        else:
            mx=getmax(s)
            if mx>0:
                s.append(None)

def getmax(s):
    if not s:
        return 0
    max=0
    for root in s:
        max=root.val if root.val > max else max
    print(max,end=' ')
    return max
    
            

            
