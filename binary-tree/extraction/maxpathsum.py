def maxpathsum(root):
    if not root :
        return 0
    if root.left is None and root.right is None:
        return root.val    
    lms=maxpathsum(root.left)
    rms=maxpathsum(root.right)
    return (lms if lms>rms else rms)+root.val
   

            

    

'''
                10
          5            20 
      2     6     15        25
              7




'''

