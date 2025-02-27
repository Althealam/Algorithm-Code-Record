# dp（先物品，后背包）
# 完全背包问题，其中物品是若干个完全平方数（i^2)，背包是n
# 1. dp数组的含义：dp[j]指的是和为j的完全平方数的最少数量
# 2. 递推公式：
# （1）当j还没加上i^2的时候，和为j-i^2的完全平方数的最少数量为dp[j-i^2]
# 这时候为dp[j-i^2]+1
# （2）当加上了后，为dp[j]
# dp[j]=min(dp[j-i^2]+1,dp[j])
# 3. 递推顺序：这个是一个组合问题，和排列没关系
# 先背包，后物品
# 4. 初始化：dp[0]=0 dp[j]=float('inf')（一定要初始化为最大值，这样递推的时候才不会被初始值覆盖）

# 时间复杂度：
# 1. 外层循环：从1到sqrt(n)，因此时间复杂度为O(sqrt(n))
# 2. 内层循环：n
# 总的时间复杂度为O(n**(3/2))
# 空间复杂度：
# 1. 使用了一个大小为n+1的数组dp来存储
# 总的空间复杂度为O(n)

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,int(n**0.5)+1): # 先遍历物品
            for j in range(i*i,n+1): # 后遍历背包
                dp[j]=min(dp[j],dp[j-i*i]+1)
        return dp[n] if dp[n]!=float('inf') else -1

        