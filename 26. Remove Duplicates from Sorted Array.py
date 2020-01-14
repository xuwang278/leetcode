class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        v = 0
        for i in range(len(nums)):
            if nums[v] != nums[i]:
                nums[v] = nums[i]
                v += 1
        return v