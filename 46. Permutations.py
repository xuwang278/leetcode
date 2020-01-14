class Solution:
    # time: O(n*n!)
    # space: O(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False] * len(nums)
        
        def dfs(cur):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                    
                visited[i] = True
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                visited[i] = False
            
        dfs([])
        
        return ans

        
    # Sol 1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return

        visited, list, ans = [False] * len(nums), [], []
        self.dfs(nums, visited, list, ans)
        return ans

    def dfs(self, nums, visited, list, ans):    
        if len(list) == len(nums):
            ans.append([] + list) # deep copy of list
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
                
            visited[i] = True
            list.append(nums[i]) # modify
            self.dfs(nums, visited, list, ans)
            list.pop() # backtrack
            visited[i] = False

    # dfs version 2： pass in new list each time 
    def dfs(self, nums, visited, list, ans):    
        if len(list) == len(nums):
            ans.append(list)
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            self.dfs(nums, visited, list + [nums[i]], ans)
            visited[i] = False
        

    # Sol 2: modify nums
    def permute_(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: 
            return []
        
        ans = []
        self.dfs(nums, [], ans)
        return ans
    
    def dfs_(self, nums, list, ans):
        if not nums:
            ans.append(list)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], list + [nums[i]], ans)
        
        # list.append(nums[i]) - add nums[i] to list
        # list + [nums[i]] - create a new list that contains items in list and nums[i]