class TreeNode():
    def __init__(self, value=0, left = None, right = None):
        self.val = value
        self.right = right
        self.left = left

class Solution():
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = TreeNode(value)
        if self.root == None:
            self.root = new_node
        else:
            ptr = self.root
            while True:
                if value > ptr.val:
                    if ptr.right == None:
                        ptr.right = new_node
                        break
                    else:
                        ptr = ptr.right
            
                elif value < ptr.val:
                    if ptr.left == None:
                        ptr.left = new_node
                        break
                    else:
                        ptr = ptr.left 
                else: raise KeyError()

    def print(self):
        queue = []
        queue.append(self.root)
        while len(queue)!=0:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def minDiffinBST(self, root = None):
        root = self.root
        if self.root == None:
            raise ValueError("NONEEEEE")

        self.counter = self.root.val

        def helper(root):
            # create a base case. Recursion stops when root does not exist
            if root == None:
                return 
            left = helper(root.left)
            right = helper(root.right)
            
            print(root.val)
            print(left)
            print(right)
            
            self.counter = min(self.counter, abs(root.val - left), abs(root.val-right))
            return root.val    
        helper(root)
        return counter

if __name__ == "__main__":
    a = Solution()
    a.insert(1)
    a.insert(0)
    a.insert(48)
    a.insert(12)
    a.insert(49)
    a.print()
    a.minDiffinBST()