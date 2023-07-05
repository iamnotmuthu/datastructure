def is_mirror(r1,r2):
    if  (not r1 and  r2) or (r1 and not r2) :
        return False
    elif not (r1 and r2 ):
        return True
    return (r1.val==r2.val)  and (is_mirror(r1.left,r2.right)) and (is_mirror(r1.right,r2.left))