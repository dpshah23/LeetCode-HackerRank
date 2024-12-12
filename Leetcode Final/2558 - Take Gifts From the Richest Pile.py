import heapq
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            max_gift = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(max_gift ** 0.5))
        
        return -sum(max_heap)
            