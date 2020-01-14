class Solution:
    # Sol 1: linear scan
    # Time: O(n)
    # Space: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    # Sol 2: Binary Search
    # Time: O(logn)
    # Space: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1]: 
                hi = mid
            else:
                 lo = mid
        return lo if nums[lo] > nums[hi] else hi
