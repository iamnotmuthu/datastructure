def is_identical(r1,r2):
    if  (not r1 and  r2) or (r1 and not 2) :
        return False
    elif not (r1 and r2 ):
        return True
    return (r1.val==r2.val ) and (is_identical(r1.left,r2.left)) and (is_identical(r1.right,r2.right))
    
def is_mirror(r1,r2):
    if  (not r1 and  r2) or (r1 and not r2) :
        return False
    elif not (r1 and r2 ):
        return True
    return (r1.val==r2.val)  and (is_mirror(r1.left,r2.right)) and (is_mirror(r1.right,r2.left))
    


def isbst(root, min, max):
    if not root:
        return True
    if (root.left) and (root.val<root.left.val) :
            return False
    if (root.right) and (root.val>root.right.val):
            return False
    return (isbst(root.left,0,root.val)) and isbst(root.right,root.val,100)