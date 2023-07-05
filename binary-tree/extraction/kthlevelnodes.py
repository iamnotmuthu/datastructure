def kthlevel(root,k,curr):
    if not root:
        return
    if k==curr:
        print(root.val,end= '   ')
    else:
        kthlevel(root.left,k,curr+1)
        kthlevel(root.right,k,curr+1)