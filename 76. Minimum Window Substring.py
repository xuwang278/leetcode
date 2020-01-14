class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict = {}
        for char in t:
            dict[char] = dict.get(char, 0) + 1

        lo = hi = start = cnt = 0
        minLen = float("inf")

        while hi < len(s):
            r = s[hi]
            if r in dict:
                dict[r] = dict.get(r) - 1
                if dict[r] == 0:
                    cnt += 1

            while cnt == len(dict):
                if hi - lo + 1 < minLen:
                    minLen = hi - lo + 1
                    start = lo

                l = s[lo]
                if l in dict:
                    dict[l] = dict.get(l) + 1
                    if dict[l] == 1:
                        cnt -= 1
                lo += 1

            hi += 1
        

        return "" if minLen == float("inf") else s[start:start + minLen]

    
    