class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        
        nums.sort()

        def dfs(nums, d, start, list):
            if len(list) == d:
                self.ans.append(list + [])
                return

            for i in range(start, len(nums)):

                if i > start and nums[i] == nujs[i - 1]:
                    continue

                list.append(nums[i])
                dfs(nums, d, i + 1, list)
                list.pop()

        for d in range(len(nums) + 1):
            dfs(nums, d, 0, [])
        
        return self.ans