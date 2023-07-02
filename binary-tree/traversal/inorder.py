def ino(root):
    if not root:
        return
    ino(root.left)
    print(root,end='   ')
    ino(root.right)
    
def inoiter(root):
    if not root :
        return
    s=[]
   
    while(s or root ):
        if root:
            s.append(root)
            root=root.left
        else:
            root=s.pop()
            print(root,end='   ')
            root=root.right
