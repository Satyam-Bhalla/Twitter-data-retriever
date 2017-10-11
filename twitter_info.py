#importing libraries
import tweepy
import auth


#creating Oauth authentication
auth = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)
auth.set_access_token(auth.access_token, auth.access_token_secret)


#object for API class in tweepy
api = tweepy.API(auth)


#input the person username
print('Enter the username')
screen_name = input()


#initializing lists and variables
info = api.get_user(screen_name)

    
#Function definitions
#Function to print timeline of user
def user_tweets(screen_name):
    tweet_txt = []
    public_tweets = api.user_timeline(screen_name) #count parameter can also be passed as user_time method
    for tweet in public_tweets:
            tweet_txt.append(tweet.text.encode('UTF-8').decode('UTF-8'))
    for i in tweet_txt:
        try:
            print(i)
        except UnicodeEncodeError:
            print()


#Getting user info            
def user_info(screen_name):
    try:
        print('Username :',info.screen_name)
    except UnicodeEncodeError:
        print('Username has emojis which python shell can not print')
    try:
        print('Description :',info.description)
    except UnicodeEncodeError:
        print('Description has emojis which python shell can not print')
    try:
        print('Number Of Followers :',info.followers_count)
    except UnicodeEncodeError:
        print('Followers must be integers')


#Getting info about user followers and how many followers do they have
def user_followers(screen_name):
    for follower in api.followers(screen_name,count=100):
        try:
            print('Follower name',str(follower.screen_name).upper(),' has followers ',str(follower.followers_count))
        except UnicodeEncodeError:
            print()


#Getting the friends information like followers,following,url,description
def user_following(screen_name):
    for friend in info.friends(count=100):
        try:
           print('Friend name =>',friend.screen_name,'\n\t\tAbout :\t',friend.description,'\n\t\tFollowers :\t',friend.followers_count,'\n\t\tFollows :\t',friend.friends_count,'\n\t\tUrl :\t',friend.entities['url']['urls'][0]['expanded_url'],'\n')
        except UnicodeEncodeError:
            print()
        except KeyError:
            print(friend.url)
        except Exception as e:
            print()
##user_info(screen_name)
##user_tweets(screen_name)
##user_followers(screen_name)
##user_following(screen_name)



