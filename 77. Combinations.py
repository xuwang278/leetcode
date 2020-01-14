class Solution:
    # time: O(2^n)
    # space: O(n)
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(s, cur):
            if len(cur) == k:
                ans.append(cur.copy())
                return

            for i in range(s, n + 1):
                cur.append(i)
                dfs(i + 1, cur)
                cur.pop()

        dfs(1, [])
        return ans
