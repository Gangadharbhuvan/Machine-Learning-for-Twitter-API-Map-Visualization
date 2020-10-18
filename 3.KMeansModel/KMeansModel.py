import tweepy
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def get_twitter_api():
    #Enter the access Tokens from Twitter Developer Account
    #Visit http://developer.twitter.com/
    ACCESS_TOKEN = "****"          
    ACCESS_TOKEN_SECRET = "****" 
    API_KEY = "****" 
    API_SECRET_KEY = "****"


    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api


def collect_twitter_data(api, twitter_user):
    favorite_data = []
    retweet_data = []
    for status in tweepy.Cursor(api.user_timeline, id=twitter_user).items(100):
        favorite_data.append(status.favorite_count)
        retweet_data.append(status.retweet_count)

    return favorite_data, retweet_data


def main():
    api = get_twitter_api()
    favorite_data, retweet_data = collect_twitter_data(api, "@cnnbrk")  #@cnnbrk - CNN Breaking News, you can try with your Twitter account too
    print(favorite_data)
    print(retweet_data)

    X = []
    for i in range(len(retweet_data)):
        X.append([retweet_data[i], favorite_data[i]])
    X = np.array(X)

    kmeans = KMeans(n_clusters=3).fit(X)
    labels = kmeans.labels_

    colors = ['r.', 'g.', 'y.', 'c.']
    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[labels[i]])

    plt.xlabel("Retweets")
    plt.ylabel("Favorites")
    plt.show()


if __name__ == "__main__":
    main()
