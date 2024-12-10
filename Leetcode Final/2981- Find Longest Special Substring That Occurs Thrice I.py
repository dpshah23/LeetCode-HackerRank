class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        for length in range(len(s), 0, -1):
            freq = defaultdict(int)
            for i in range(len(s) - length + 1):
                substring = s[i:i+length]
                if len(set(substring)) == 1:
                    freq[substring] += 1
            for substring, count in freq.items():
                if count >= 3:
                    return length
        return -1