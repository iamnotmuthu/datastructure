
def pre(root):
    if not root:
        return
    print(root.val,end='   ')
    pre(root.left)
    pre(root.right)

def preiter(root2):
    root=root2
    stack=[]
    stack.append(root)
    while(stack):
        if root:
            stack.append(root)
            print(root, end ='   ')
            root=root.left
        else:
            root=stack.pop()
            root=root.right