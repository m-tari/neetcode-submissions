from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word1 in wordList:
            for word2 in wordList:
                i = 0
                d = 0
                while i < len(word1):
                    if word1[i] == word2[i]:
                        i += 1
                        continue
                    else:
                        d += 1
                        i += 1
                    if d > 1:
                        break
                if d == 1:
                    adj[word1].append(word2)

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
                for n in adj[word]:
                    if n not in visit:
                        visit.add(word)
                        queue.append(n)


        return 0