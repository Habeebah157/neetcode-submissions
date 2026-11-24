from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list)   # userId → [(timestamp, tweetId)]
        self.following = defaultdict(set)      # followerId → {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Gather tweets from self + followees
        feed = self.user_tweets[userId][:]
        for followeeId in self.following[userId]:
            feed.extend(self.user_tweets[followeeId])
        
        # Sort by timestamp descending
        feed.sort(key=lambda x: x[0], reverse=True)
        
        # Return top 10 tweet IDs
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)