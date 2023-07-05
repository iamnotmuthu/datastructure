def lowest_anc(root,left,right):
    if not root:
        return
    if root.val==left or root.val==right:
        return root
    lf=lowest_anc(root.left,left,right)
    rf=lowest_anc(root.right,left,right)
    if lf and rf:
        return root
    elif(lf):
        return lowest_anc(root.left,left,right)
    else :
        return lowest_anc(root.right,left,right)
    
    


    



