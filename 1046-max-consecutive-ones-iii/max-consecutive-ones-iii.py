class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        n = len(nums)
        zcount = 0
        maxlen=0
        for r in range(n):
            if nums[r]==0:
                zcount+=1
            while zcount > k:
                if nums[l]==0:
                    zcount-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen