class Solution(object):
    def longestPalindrome(self, s):
        length=0
        oddchars=[]
        for i in s:
            if i not in oddchars:
                oddchars.append(i)
            else:
                oddchars.remove(i)
                length+=2
                
        if not oddchars:
            return length
        else:
            return length+1

        