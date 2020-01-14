class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        visited = [False] * len(nums)
        
        def dfs(cur):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                visited[i] = False
        
        dfs([])
        return ans