class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 1: return min(A[0])
        m = len(A)
        dp = [[0] * m for _ in range(m)]
        
        for i in range(m):
            for j in range(m):
                # first row keep the same as A
                if i == 0:
                    dp[i][j] = A[i][j]
                else:
                    # see the previous row
                    left = dp[i-1][j-1] if j > 0 else float("inf")
                    mid = dp[i-1][j]
                    right = dp[i-1][j+1] if j < m - 1 else float("inf")
                    
                    dp[i][j] = min(left, mid, right) + A[i][j] # add current val
        return min(dp[-1])
