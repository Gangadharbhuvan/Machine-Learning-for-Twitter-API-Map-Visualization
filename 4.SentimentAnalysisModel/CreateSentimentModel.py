import random
import pickle
from nltk.corpus import twitter_samples, stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import NaiveBayesClassifier
from nltk import classify


def clean_data(token):
    return [item for item in token if not item.startswith('@') and not item.startswith('http')]


def to_lower(token):
    return [item.lower() for item in token]


def lemmatize(token):
    lemmatizer = WordNetLemmatizer()

    result = []
    for item, tag in pos_tag(token):
        if tag[0].lower() in "nva":
            result.append(lemmatizer.lemmatize(item, tag[0].lower()))
        else:
            result.append((lemmatizer.lemmatize(item)))

    return result


def remove_stop_words(token, stop_words):
    return [item for item in token if item not in stop_words]


def transform_features(token):
    feature_set = {}
    for feature in token:
        if feature not in feature_set:
            feature_set[feature] = 0
        feature_set[feature] += 1
    return feature_set


def main():
    # Step 1: Gather data
    positive_tweets = twitter_samples.tokenized('positive_tweets.json')
    negative_tweets = twitter_samples.tokenized('negative_tweets.json')
    print(positive_tweets[0])
    print(negative_tweets[0])

    # Step 2: Clean, lemmatize and remove stop words from data
    stop_words = stopwords.words('english')
    positive_tweets = [remove_stop_words(lemmatize(clean_data(to_lower(item))), stop_words) for item in positive_tweets]
    negative_tweets = [remove_stop_words(lemmatize(clean_data(to_lower(item))), stop_words) for item in negative_tweets]
    print(positive_tweets[0])
    print(negative_tweets[0])

    # Step 3: Transform data
    positive_tweets = [(transform_features(token), "Positive") for token in positive_tweets]
    negative_tweets = [(transform_features(token), "Negative") for token in negative_tweets]
    print(positive_tweets[0])
    print(negative_tweets[0])

    # Step 4: Create data set
    dataset = positive_tweets + negative_tweets
    random.shuffle(dataset)

    training_data = dataset[:7000]
    test_data = dataset[7000:]

    # Step 5: Train the model
    classifier = NaiveBayesClassifier.train(training_data)

    # Step 6: Test accuracy
    print("Accuracy:", classify.accuracy(classifier, test_data))
    print(classifier.show_most_informative_features(10))

    # Step 7: Save the model
    with open("my_classifier.pickle", "wb") as f:
        pickle.dump(classifier, f)


if __name__ == "__main__":
    main()
