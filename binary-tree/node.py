class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None
    
    def __repr__(self) -> str:
        return str(self.val)