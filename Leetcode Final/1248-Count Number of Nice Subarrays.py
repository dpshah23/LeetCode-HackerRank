class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n=len(nums)
        i=0
        count=0
        ans=0
        for j in range(n):
            if nums[j] & 1:
                k-=1
                count=0
            while k==0:
                k+= nums[i] & 1
                i+=1
                count+=1
            ans+=count
        return ans
        