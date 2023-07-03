def zz(root):
    if not root:
        return
    s1=[]
    s2=[]
    s1.append(root)
    while(len(s1)>0 or len(s2)>0):
        while s1:
            root=s1.pop()
            print(root, end='   ')
            if root.right:
                s2.append(root.right)
            if root.left:
                s2.append(root.left)
        while s2:
            root=s2.pop()
            print(root, end='   ')
            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)
