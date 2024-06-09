class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=sum(nums)
        expected=n*(n+1)//2
        return expected-s