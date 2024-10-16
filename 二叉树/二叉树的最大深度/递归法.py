# 方法：递归法
# 时间复杂度：O(n)，每个节点都会被访问一次
# 空间复杂度
# 最坏情况下是O(n)，二叉树是单链状（即所有节点只有左子树/右子树），递归的深度会达到n
# 最佳情况下是O(logn)，二叉树是平衡的，比如完全二叉树，那么递归的最大深度是树的高度h=logn

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        