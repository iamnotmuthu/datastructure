from node import Node
class BST:
    def __init__(self) -> None:
        self.root=None
    
    def add(self,val):
        if not self.root:
            self.root=Node(val)
        else:
            self._insert(self.root,val)

    def _insert(self,root,val):

        if val < root.val:
            if root.left is None:
                root.left=Node(val)
            else:
                self._insert(root.left,val)
        else:
            if root.right is None:
                root.right=Node(val)
            else:
                self._insert(root.right,val)