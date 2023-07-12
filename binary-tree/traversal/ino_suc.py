def ino_suc(root,key):
    if not root:
        return False
    found=ino_suc(root.left,key)
    if not found:
        if root.val>key:
            print('inosuc is ',root.val) 
            return  True
        return ino_suc(root.right,key)
    


'''
               10
          5            20 
      2     6     15        25
              7


'''
    