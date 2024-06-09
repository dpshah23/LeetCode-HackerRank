class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        find=0
        isfind=False
        for i in nums:
            find+=1
            if i==target:
                
                return find-1
        if isfind==False:
            return -1

obj1=Solution()
print(obj1.search([4,5,6,7,0,1,2],0))