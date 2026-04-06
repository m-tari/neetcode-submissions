from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)  # userId -> list of (-time, tweetId)
        self.followMap = defaultdict(set)  # userId (follower) -> set of followeesId
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -=  1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Add the latest tweet of all followees to the heap
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append((time, tweetId, followeeId, index - 1))

        heapq.heapify(minHeap)
        # Pop the latest tweet in the current heap state, then add the next candidate for the next pop
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (time, tweetId, followeeId, index - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
       
