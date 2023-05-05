# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        visited = set()
        def bfs(node,k):
            if node in visited: return
            visited.add(node)
            que = deque()
            level = 0
            que.append((level,node))
            while que:
                if level == k: 
                   return result.extend([j.val for i,j in que])
                l = len(que)
                level += 1
                for _ in range(l):
                    _,node = que.popleft()
                    if node.left and node.left not in visited:
                        visited.add(node.left)
                        que.append((level,node.left))
                    if node.right and node.right not in visited:
                        visited.add(node.right)
                        que.append((level,node.right))
        def dfs(root,k):
            if root:
                if root == target:
                    bfs(root,k)
                    return k - 1
                left = dfs(root.left,k)
                right = dfs(root.right,k)
                if left != None and not right:
                    bfs(root,left)
                    return left - 1
                elif right != None and not left:
                    bfs(root,right)
                    return right - 1
        dfs(root,k)
        return result