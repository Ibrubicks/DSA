class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=[]
        for i in range(m):
            l.append(nums1[i])
        for i in range(n):
            l.append(nums2[i])
        l.sort()

        for i in range(m+n):
            nums1[i]=l[i]