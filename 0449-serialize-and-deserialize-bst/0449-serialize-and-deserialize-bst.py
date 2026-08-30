# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        output = []
        def dfs(node):
            if not node:
                return 
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(output)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        def make_tree(node,val):
            if not node:
                return TreeNode(val)
            if val > node.val:
                node.right = make_tree(node.right, val)
            elif val < node.val:
                node.left = make_tree(node.left, val)
            return node
        
        for val in data[1:]:
            make_tree(root, int(val))
        return root
                




# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans