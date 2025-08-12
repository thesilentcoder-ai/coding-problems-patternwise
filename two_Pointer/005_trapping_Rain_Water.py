class Solution:
    def trap(self, height: List[int]) -> int:
        
        lwall = rwall = 0
        n = len(height)
        lmaxh = [0] *n
        rmaxh = [0] *n
        
        for i in range(n):
            j = -i-1
            lmaxh[i] = lwall
            rmaxh[j] = rwall
            lwall = max(lwall, height[i]) 
            rwall = max(rwall, height[j])
 
        maxarea = 0
        for i in range(n):
            pot = min(lmaxh[i],rmaxh[i])
            maxarea += max(0,pot-height[i])

        return maxarea
