class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score=0
        for i in range(0,len(s)-1):
        
            if i+1<=len(s):
                diff=ord(s[i])-ord(s[i+1])
                score+=abs(diff)
            else:
                break
        return score

        