
def pre(root):
    if not root:
        return
    print(root.val,end='   ')
    pre(root.left)
    pre(root.right)

def preiter(root):
    stack=[]
    stack.append(root)
    while(stack or root):
        if root:
            stack.append(root)
            print('adding',root)
            root=root.left
        else:
            root=stack.pop()
            print('removing',root)
            root=root.right