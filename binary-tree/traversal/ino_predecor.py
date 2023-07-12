def ino_pre(root,key):
    if not root:
        return False
    found=ino_pre(root.right,key)
    if not found:
        if root.val<key:
            print('inorder predessor is ',root.val) 
            return  True
        return ino_pre(root.left,key)
    


'''
               10
          5            20 
      2     6     15        25
              7


'''
    