class Solution(object):
    def search(self, nums, target):
        find=0
        isfind=False
        for i in nums:
            find+=1
            if i==target:
                
                return find-1
        if isfind==False:
            return -1
