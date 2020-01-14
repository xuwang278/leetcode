class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dict = set(wordList)
        if endWord not in dict: return 0

        # from collections import deque 
        # q = deque([beginWord])
        q = collections.deque([beginWord])
        step = 0
        while q:
            size = len(q)
            for s in range(size):
                top = q.popleft()   
                for i in range(len(top)):
                    # c = top[i] # not necessary
                    for ch in string.ascii_lowercase:
                        # if ch == c: continue
                        next = top[:i] + ch + top[i+1:]
                        if next == endWord: return step + 2
                        if next not in dict: continue
                        dict.remove(next)
                        q.append(next)
            step += 1
        return 0


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dict = set(wordList)
        if endWord not in dict: return 0

        q = collections.deque([beginWord])
        step = 0
        while q:
            size = len(q)
            for s in range(size):
                top = q.popleft()   
                next_words = [top[:i] + ch + top[i+1:] for i in range(len(top)) for ch in string.ascii_lowercase]
                for next in next_words:
                    if next == endWord: return step + 2
                    if next not in dict: continue
                    dict.remove(next)
                    q.append(next)
            step += 1
        return 0
        