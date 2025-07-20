class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        k=0
        
        while l<=r:
            m=l+(r-l)//2
            if target<nums[m]:
                r=m-1
                k-=1
            elif target>nums[m]:
                l=m+1
                k+=1
            else:
                return m
        return l
            
        
        