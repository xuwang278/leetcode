class Solution:
    # https://zxi.mytechroad.com/blog/searching/leetcode-78-subsets/

    # SOl 1: dfs + backtracking
    # Time: O(n*(2^n)), all subsets C(0,m) + C(1,m) + ... + C(m,m) = O(2^n); copy costs O(n)
    # Space: O(2^n), ans
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(n, s, cur):
            if n == len(cur):
                ans.append(cur.copy())
                return

            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(n, i + 1, cur)
                cur.pop()

        for i in range(len(nums) + 1):
            dfs(i, 0, [])
        
        return ans

    # Sol 2: bit
    def subsets(self, nums: List[int]) -> List[List[int]]:

