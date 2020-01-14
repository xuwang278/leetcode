class Solution:
    # Time: O(2^n)
    # Space: O(n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def dfs(sum, s, cur):
            if sum == target:
                ans.append(cur.copy())
                return
            
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                if sum + candidates[i] > target:
                    return
                
                cur.append(candidates[i])
                dfs(sum + candidates[i], i + 1, cur)
                cur.pop()
            
        dfs(0, 0, [])
            
        return ans
            