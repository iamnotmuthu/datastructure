def post(root):
    if not root:
        return
    post(root.left)
    post(root.right)
    print(root,end='   ')


def postiter(root):
    if not root:
        return
    s1=[]
    s2=[]
    s1.append(root)

    while(s1):
        root=s1.pop()
        s2.append(root)
        if(root.left):
            s1.append(root.left)
        if(root.right):
            s1.append(root.right)
    
    while(s2):
        root=s2.pop()
        print(root,end ='   ')


            

            