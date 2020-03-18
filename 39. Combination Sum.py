class Solution:
    # Time: O(2^n)
    # Space: O(n)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(sum, s, cur):
            if sum > target:
                return
            if sum == target:
                ans.append(cur.copy())
                return
            
            for i in range(s, len(candidates)):
                cur.append(candidates[i])
                dfs(sum + candidates[i], i, cur);
                cur.pop()
        
        dfs(0, 0, [])
        return ans

    # sort
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(sum, s, cur):
            if sum == target:
                ans.append(cur.copy())
                return
            
            for i in range(s, len(candidates)):
                if sum + candidates[i] > target:
                    return
                cur.append(candidates[i])
                dfs(sum + candidates[i], i, cur);
                cur.pop()
        
        dfs(0, 0, [])
        return ans
    
    # new version
    # 2020/03/18
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        l = []
        
        def dfs(s, curSum):
            if curSum == target:
                ans.append(l.copy())
                return
            
            if curSum > target:
                return
            
            for i in range(s, len(candidates)):
                print(i)
                l.append(candidates[i])
                dfs(i, curSum + candidates[i])
                l.pop()
        
        dfs(0, 0)
        
        
        return ans
    
        
