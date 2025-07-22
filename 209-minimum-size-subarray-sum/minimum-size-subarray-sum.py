class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        minlen=float('inf')
        currsum=0
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum>=target:
                minlen=min(minlen,r-l+1)
                currsum-=nums[l]
                l+=1

        return 0 if minlen==float('inf') else minlen