class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j1 = list(jewels)
        s1 = list(stones)
        for i in range(len(s1)):
            for j in range(len(j1)):
                if(s1[i]==j1[j]):
                    count+=1
        return count