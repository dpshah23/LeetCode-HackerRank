class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)
        total_sum = 0
        count = 0
        
        for i in range(1, n + 1):
            if i not in banned_set and total_sum + i <= maxSum:
                total_sum += i
                count += 1
            elif total_sum + i > maxSum:
                break
        
        return count
            