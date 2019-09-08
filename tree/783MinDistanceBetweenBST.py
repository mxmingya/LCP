# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    diff = float('inf')
    prev = -float('inf')
    
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.diff = min(self.diff, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.diff