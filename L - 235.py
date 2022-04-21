class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        current = root

        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            
            elif p.val < current.val and q.val < current.val:
                current = current.left
            
            else:
                return current