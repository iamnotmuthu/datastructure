from validation.is_identical import *

def is_sub_tree(parent,child):
    if not parent:
        return False
    if not child:
     return True
    if is_identical(parent,child):
        return True
    return is_sub_tree(parent.left, child) or is_sub_tree(parent.right,child)