class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        max_beauty = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            max_beauty = max(max_beauty, right - left + 1)
        
        return max_beauty
            