import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import matplotlib.pyplot as plt

class Twitter:
    def __init__(self):
        #key and token for authentication
        consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        consumer_secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        access_token_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

        #attempt authentication
        try:
            #create OAuthHandler obj
            self.auth = OAuthHandler(consumer_key, consumer_secret_key)
            #set access token and secret
            self.auth.set_access_token(access_token, access_token_key)
            #create tweepy  API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication failed.")

    #utility function to clean tweet text by removing links, specail characters
    def clean_tweets(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|(^0-9A-Za-z\t])|(\w+:\/\/\/\S+)","",tweet).split())

    #utility function to classify sentiment of tweets
    def get_sentiment(self,tweet):
        analysis = TextBlob(self.clean_tweets(tweet))
        if analysis.sentiment.polarity > 0.00:
            return "Positive"
        elif analysis.sentiment.polarity < 0.00:
            return "Negative"
        elif analysis.sentiment.polarity == 0.00:
            return "Neutral"

    #Function to fetch tweets and parse them.
    #storing every parse tweet as a dictonary to a list
    def get_classify(self, query, count):
        tweets = []

        try:
            #call twitter api to fetch tweets
            fatched_tweets = self.api.search(q = query, c = count)
            # parsing tweets one by one
            for tweet in fatched_tweets:
                parsed_tweets = {}
                parsed_tweets['Text'] = tweet.text
                parsed_tweets['Sentiment'] = self.get_sentiment(tweet.text)
                if tweet.retweet_count > 0:
                    if parsed_tweets not in tweets:
                        tweets.append(parsed_tweets)
                    else:
                        tweets.append(parsed_tweets)
            return tweets
        except tweepy.TweepError as e:
            print("Error: "+str(e))

#Utility function to calculate percentage
def parcentage(value,total):
    return 100 * value // total

if __name__ == '__main__':
    #creating object of Twitter class
    SA = Twitter()

    searchTerm = input("Enter the keyword: ")
    noOfCount = int(input("Enter the no of tweets to count: "))

    #calling function to get tweets
    tweets = SA.get_classify(query=searchTerm, count=noOfCount)

    #creating list of different sentimental tweets
    positive = [tweet for tweet in tweets if tweet['Sentiment'] == 'Positive']
    negative = [tweet for tweet in tweets if tweet['Sentiment'] == 'Negative']
    neutral = [tweet for tweet in tweets if tweet['Sentiment'] == 'Neutral']

    positiveSize = len(positive)
    negativeSize = len(negative)
    neutralSize = len(neutral)

    #calculating percentages
    positivePercantage = parcentage(positiveSize,len(tweets))
    negativePercantage = parcentage(negativeSize,len(tweets))
    neutralPercantage = parcentage(neutralSize, len(tweets))

    print("Positive tweets percantage is: {}%".format(positivePercantage))
    print("Negative tweets percantage is: {}%".format(negativePercantage))
    print("Neutral tweets percantage is: {}%".format(neutralPercantage))

    #showing top 10 tweets
    print("Positive tweets are: ")
    for tweet in positive[:10]:
        print(tweet['Text'])

    print("Negative tweets are: ")
    for tweet in negative[:10]:
        print(tweet["Text"])

    #Creating a pie plot for visualisation
    label = ['Positive ['+str(positivePercantage)+'%]', 'Negative ['+str(negativePercantage)+'%]', 'Neutral ['+str(neutralPercantage)+'%]']
    size = [positivePercantage, negativePercantage, neutralPercantage]
    colors = ['Yellowgreen', 'Red', 'Gold']
    patches, text = plt.pie(size, colors = colors, startangle = 90)
    plt.legend(patches, label, loc = 'best')
    plt.title('How people reacted on '+searchTerm+' by analyzing '+str(noOfCount)+' tweets.')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
