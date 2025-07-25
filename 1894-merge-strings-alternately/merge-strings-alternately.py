class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #ibrahim
        l = ""
        n = min(len(word1),len(word2))
        for i in range(n):
            l+=word1[i]+word2[i]
        if len(word1)>len(word2):
            l+=word1[n:]
        elif len(word2)>len(word1):
            l+=word2[n:]

        return l
