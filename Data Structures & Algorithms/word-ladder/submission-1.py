from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for m in range(len(word)):
                pattern = word[:m] + "*" + word[m + 1:]
                adj[pattern].append(word)

        visit = set()
        queue = deque()
        queue.append(beginWord)
        l = 0
        while queue:
            l += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return l
                for m in range(len(word)):
                    pattern = word[:m] + "*" + word[m + 1:]                
                    for w in adj[pattern]:
                        if w not in visit:
                            visit.add(w)
                            queue.append(w)


        return 0