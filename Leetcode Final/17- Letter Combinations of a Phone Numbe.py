class Solution(object):
    def track(self, n, charnum):
        if n in charnum:
            return charnum[n]
        return []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

       
        charnum = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        res = [''] 

        for digit in digits:
            letters = self.track(digit, charnum)
            temp_res = []
            for prefix in res:
                for letter in letters:
                    temp_res.append(prefix + letter)
            res = temp_res

        return res
