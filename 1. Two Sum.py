class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or not len(nums):
            return [-1, -1]
        
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i
            
        return [-1, -1]

