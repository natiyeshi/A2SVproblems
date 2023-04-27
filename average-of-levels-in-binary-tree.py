# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque()
        que.append((1,root))
        result = [root.val]
        tree = defaultdict(list)
        while que:
            level,node = que.popleft()
            value = count = 0
            if node.left: 
                que.append([level + 1,node.left])
                temp = [0,0]
                if tree[level]:
                    temp = tree[level]
                temp[0] += 1
                temp[1] += node.left.val
                tree[level] = temp
            if node.right:
                que.append([level + 1,node.right])
                temp = [0,0]
                if tree[level]:
                    temp = tree[level]
                temp[0] += 1
                temp[1] += node.right.val
                tree[level] = temp
        for itr in tree:
           temp = tree[itr][1] / tree[itr][0]
           result.append(temp)
        print(tree)
        return result