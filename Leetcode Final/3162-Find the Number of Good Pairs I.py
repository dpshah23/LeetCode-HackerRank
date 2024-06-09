class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        paircount=0
        for i in nums1:
            for j in nums2:
                if i%(j*k)==0:
                    paircount+=1

        return paircount 
        
        