def bfs(root):
    if not root:
        return
    q=[]
    q.append(root)
    while(q):
        root=q.pop(0)
        print(root, end='   ')
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
    
    
