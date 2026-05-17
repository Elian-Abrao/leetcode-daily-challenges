import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # Track tweets as (timestamp, tweetId) pairs for each user
        # Using list since we need ordered insertion and recent retrieval
        self.tweets = defaultdict(list)
        
        # Track who each user follows (set for O(1) add/remove/check)
        self.following = defaultdict(set)
        
        # Global timestamp to maintain tweet ordering across all users
        # Decremented each time so we can use min-heap for max behavior
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store tweet with decreasing timestamp for recency ordering
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Use min-heap to efficiently merge K sorted lists (tweets from followed users)
        # Heap stores: (timestamp, tweetId, userId, index_in_user_tweets)
        min_heap = []
        
        # Add user's own most recent tweet to heap (user sees their own tweets)
        if userId in self.tweets and self.tweets[userId]:
            timestamp, tweet_id = self.tweets[userId][-1]
            heapq.heappush(min_heap, (timestamp, tweet_id, userId, len(self.tweets[userId]) - 1))
        
        # Add most recent tweet from each followed user
        for followee_id in self.following[userId]:
            if followee_id in self.tweets and self.tweets[followee_id]:
                timestamp, tweet_id = self.tweets[followee_id][-1]
                heapq.heappush(min_heap, (timestamp, tweet_id, followee_id, len(self.tweets[followee_id]) - 1))
        
        # Extract up to 10 most recent tweets using heap
        news_feed = []
        while min_heap and len(news_feed) < 10:
            timestamp, tweet_id, user_id, index = heapq.heappop(min_heap)
            news_feed.append(tweet_id)
            
            # If this user has more tweets, add the next most recent one
            if index > 0:
                next_timestamp, next_tweet_id = self.tweets[user_id][index - 1]
                heapq.heappush(min_heap, (next_timestamp, next_tweet_id, user_id, index - 1))
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # User cannot follow themselves (guaranteed by constraints but safe to check)
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followee if exists (discard won't raise error if not present)
        self.following[followerId].discard(followeeId)