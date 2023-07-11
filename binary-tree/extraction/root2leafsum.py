'''
               10
          5            20 
      2     6     15        25
              7


'''

def root2leafsum(root,sum):
    if not root:
        return
    
    if not (root.left or root.right):
        print('sum is ',sum+root.val)
    
    root2leafsum(root.left,sum+root.val)
    root2leafsum(root.right,sum+root.val)
    

    