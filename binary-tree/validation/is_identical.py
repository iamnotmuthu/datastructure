def is_identical(r1,r2):
    if  (not r1 and  r2) or (r1 and not 2) :
        return False
    elif not (r1 and r2 ):
        return True
    return (r1.val==r2.val ) and (is_identical(r1.left,r2.left)) and (is_identical(r1.right,r2.right))