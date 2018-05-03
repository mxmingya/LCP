# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def reverse(list):
        	l = len(list)
        	for i in range(l):
        		temp = list[i]
        		list[i] = list[l-i-1]
        		list[l-i-1] = list[i]
        res = []
        queue = deque([])
        queue.append(root)
        i = 0
        while queue:
        	length = len(queue)
        	print(length)
        	cur = []
        	if root.left:
        		queue.append(root.left)
        	if root.right:
        		queue.append(root.right)
        	for i in range(length):
        		cur.append(queue.popleft())
        	if i % 2 == 1:
        		reverse(cur)
        	res.append(cur)
        	i = i + 1
        return res
