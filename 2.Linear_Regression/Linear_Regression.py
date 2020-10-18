import tweepy
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


def get_twitter_api():
    #Enter the access Tokens from Twitter Developer Account
    #Visit http://developer.twitter.com/
    ACCESS_TOKEN = "****"          
    ACCESS_TOKEN_SECRET = "****" 
    API_KEY = "****" 
    API_SECRET_KEY = "****



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
    favorite_data, retweet_data = collect_twitter_data(api, "@cnnbrk")
    print(favorite_data)
    print(retweet_data)

    # reshape row data to column data
    retweet_data_col = np.array(retweet_data).reshape((-1, 1))
    print(retweet_data_col)

    regr = linear_model.LinearRegression()
    regr.fit(retweet_data_col, favorite_data)
    print("Coeffcient", regr.coef_)
    print("Intercepts", regr.intercept_)

    x = np.array(range(0, max(retweet_data)))
    y = eval('regr.coef_*x + regr.intercept_')
    plt.plot(x, y)
    plt.scatter(retweet_data, favorite_data, color='red')
    plt.xlabel("Retweets")
    plt.ylabel("Favorites")
    plt.show()


if __name__ == "__main__":
    main()
