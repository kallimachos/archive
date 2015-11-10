import twitter
import util
import colour
from config import *

api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)

def printScreenName(name):
    print colour.green + "@" + name + colour.end + ": ",

def find(searchTerm):
    """
    Print recent tweets containing `searchTerm`.

    To test this function, at the command line run:
        python raven.py --search=<search term>
    For example,
        python raven.py --search=python
    """

    try:
        tweets = api.GetSearch(searchTerm)
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    if len(tweets) > 10:
        tweets = tweets[:10]

    print ''
    for tweet in tweets:
        printScreenName(tweet.user.screen_name)
        util.safe_print(tweet.GetText())
    print ''

def trendingTopics(woeid):
    """twitter apisearch
    Print the currently trending topics.

    To test this function, at the command line run:
        python raven.py -t
    """
    try:
        trending_topics = api.GetTrendsWoeid(woeid)
    except twitter.TwitterError:
        trending_topics = api.GetTrendsCurrent()
    except twitter.urllib2.URLError:
      print ("Unable to connect to network, giving up.")
      twitter.sys.exit()
    for topic in trending_topics:
        util.safe_print(topic.name)

def trendingTweets(woeid):
    """
    Print tweets for all the trending topics.

    To test this function, at the command line run:
        python raven.py -w
    """
    try:
        trending_topics = api.GetTrendsWoeid(woeid)
    except twitter.TwitterError:
        trending_topics = api.GetTrendsCurrent()
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    print ''
    for topic in trending_topics:
        print colour.yellow + "**",topic.name + colour.end
        esc_topic_name = twitter.urllib2.quote(topic.name.encode('utf8'))
        tweets = api.GetSearch(esc_topic_name)
        for tweet in tweets[:5]:
            printScreenName(tweet.user.screen_name)
            util.safe_print(tweet.GetText())
        print ''

def userHomeTimeline():
    """
    Fetch a collection of the most recent Tweets and retweets posted by the
    authenticating user and the users they follow.
    """
    try:
        tweets = api.GetHomeTimeline(count=5)
    except twitter.TwitterError:
        print ("User @" + username + " not found")
        twitter.sys.exit()
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    print ''
    for tweet in tweets:
        printScreenName(tweet.user.screen_name)
        util.safe_print(tweet.GetText())
    print ''


def userTweets(username):
    """
    Print recent tweets by `username`.

    You may find the twitter.Api() function GetUserTimeline() helpful.

    To test this function, at the command line run:
        python raven.py -u <username>
    For example,
        python raven.py -u bostonpython
    """
    try:
        tweets = api.GetUserTimeline(screen_name=username, count=5)
    except twitter.TwitterError:
        print ("User @" + username + " not found")
        twitter.sys.exit()
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    for tweet in tweets:
        util.safe_print(tweet.GetText())

def userStream():
    """
    Displays the authenticated user's Twitter stream.
    """
    try:
        tweets = api.GetUserStream()
    except twitter.TwitterError:
        print ("User @" + username + " not found")
        twitter.sys.exit()
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    for tweet in tweets:
        print tweet
        #util.safe_print(tweet.GetText())

def postTweet(message):
    """
    Post the 'message' status update (tweet) on twitter.
    """
    try:
        status = api.PostUpdate(message)
    except twitter.TwitterError:
        print ("User @" + username + " not found")
        twitter.sys.exit()
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()
    print "Tweet successful.\n"