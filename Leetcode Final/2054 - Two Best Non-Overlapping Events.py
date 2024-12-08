class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        INF=10**20
        events.sort()
        
        best_previous= -INF
        h=[]
        best= max(v for _,_,v in events)

        for s,e,v in events:

            while len(h)>0 and h[0][0]<=s:   
                _,nv=heapq.heappop(h)
                best_previous=max(best_previous,nv)

            heapq.heappush(h,(e+1,v))
            
            best=max(best,best_previous+v)
        return best        