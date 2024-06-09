class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        sets = set(dictionary)
        words = sentence.split()
        def findreplace(word):
            for i in range(1,len(word)+1):
                if word[:i] in sets:
                    return word[:i]
            return word
            
        replaceword=[findreplace(word) for word in words]
        return ' '.join(replaceword)
        