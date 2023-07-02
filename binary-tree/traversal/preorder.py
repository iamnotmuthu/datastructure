
def pre(root):
    if not root:
        return
    print(root.val,end='   ')
    pre(root.left)
    pre(root.right)

def preiter(root):
    stack=[]
    while(stack or root):
        if root:
            stack.append(root)
            print(root, end ='   ')
            root=root.left
        else:
            root=stack.pop()
            root=root.right


def preiter_opt(root):
    if not root:
        return
    stack =[]
    stack.append(root)
    while(stack):
        if root:
            print(root, end='   ')
            if root.right is not None:
                stack.append(root.right)
            root=root.left
        else:
            root=stack.pop()
            