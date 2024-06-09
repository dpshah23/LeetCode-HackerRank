class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup_num = {}
        index = 0
        while index < len(nums):
            if nums[index] in dup_num:
                nums.pop(index)
            else:
                dup_num[nums[index]] = True
                index += 1
        return len(nums)
