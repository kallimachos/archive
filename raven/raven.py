# Add option that uses api.DestroyStatus to delete the authenticated user's most recent tweet.
# Fix the -s option.

import argparse
import twitter_functions

def main():
    parser = argparse.ArgumentParser()
    woeid = 1100661

    parser.add_argument("-f", "--find",
                      type=str,
                      dest="search_term",
                      nargs=1,
                      help="Display tweets containing a particular string.")

    parser.add_argument("-t", "--trending-topics",
                      action="store_true",
                      help="Display the trending topics.")

    parser.add_argument("-w", "--trending-tweets",
                      action="store_true",
                      dest="trending_tweets",
                      help="Display tweets from all of the trending topics.")

    parser.add_argument("-o", "--woeid",
                      type=int,
                      dest="woeid",
                      help="Localize to a particular WOEID. Defaults to Brisbane. Vancouver is 9807. (Only affects -t and -w).")

    parser.add_argument("-l", "--timeline",
                      action="store_true",
                      help="Display a user's home timeline.")

    parser.add_argument("-u", "--user-tweets",
                      type=str,
                      action="store",
                      dest="userid",
                      help="Display a user's tweets.")

    parser.add_argument("-s", "--user-stream",
                      action="store_true",
                      help="Display the authenticated user's Twitter stream. CURRENTLY DOES NOT WORK.")

    parser.add_argument("-p", "--post",
                        type=str,
                        dest="message",
                        nargs=1,
                        help="Post a status update (tweet) on Twitter.")

    args = parser.parse_args()
    if args.woeid:
        woeid = args.woeid
    if args.userid:
        userid = args.userid

    if args.search_term:
        twitter_functions.find(args.search_term)
    elif args.trending_topics:
        twitter_functions.trendingTopics(woeid)
    elif args.trending_tweets:
        twitter_functions.trendingTweets(woeid)
    elif args.timeline:
        twitter_functions.userHomeTimeline()
    elif args.userid:
        twitter_functions.userTweets(args.userid)
    elif args.user_stream:
        twitter_functions.userStream()
    elif args.message:
        twitter_functions.postTweet(args.message)
    else: twitter_functions.userHomeTimeline()

if __name__ == "__main__":
    main()
