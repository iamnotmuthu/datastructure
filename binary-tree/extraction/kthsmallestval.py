

k=3
def kthsmall(root):
    global k
    if not root:
        return None
    left=kthsmall(root.left)
    if left:        
        return left
    k=k-1
    if k==0:
        return root
    return kthsmall(root.right)


    

    