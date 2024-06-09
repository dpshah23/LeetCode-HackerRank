class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        tptr=0
        sptr=0

        while sptr<len(s) and tptr<len(t):
                if s[sptr]==t[tptr]:
                    tptr+=1
                sptr+=1

        return len(t)-tptr


        