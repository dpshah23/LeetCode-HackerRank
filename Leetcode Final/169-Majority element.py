class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numcount={}
        n=len(nums)
        for i in nums:
            if i not in numcount.keys():
                numcount[i]=1
            else:
                numcount[i]+=1
    
        return max(zip(numcount.values(), numcount.keys()))[1]
        