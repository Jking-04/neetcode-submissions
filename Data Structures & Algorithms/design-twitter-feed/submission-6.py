import heapq
class Twitter:

    def __init__(self):
        self.follow_dict = {}
        self.tweets = []
        self.post_count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_count += 1
        self.tweets.append([self.post_count,userId,tweetId])
        
        if userId not in self.follow_dict:
            self.follow_dict[userId] = [userId]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        personal_tweets = [(-p_count,t_id) for p_count,u_id,t_id in self.tweets if u_id in self.follow_dict[userId] ]
        news_feed = []

        heapq.heapify(personal_tweets)
        while personal_tweets and len(news_feed)<10:
            _,new_t_id =heapq.heappop(personal_tweets)
            news_feed.append(new_t_id)

        return news_feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_dict:
            if followeeId not in self.follow_dict[followerId]:
                self.follow_dict[followerId].append(followeeId)
        else:
            self.follow_dict[followerId] = [followerId,followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.follow_dict:
            if followeeId in self.follow_dict[followerId]:
                self.follow_dict[followerId].remove(followeeId)

        
