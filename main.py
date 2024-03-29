import tweepy  # An easy-to-use Python library for accessing the Twitter API.
# TextBlob is a Python library for processing textual data.
from textblob import TextBlob
import pandas as pd  # open source data analysis and manipulation tool
# matplotlib is multi-platform data visualization library built on Numpy array
import matplotlib.pyplot as plt
# This module provides regular expression matching operations similar to those found in Perl.
import re
from wordcloud import WordCloud
plt.style.use('fivethirtyeight')
TwitterProfileId = input("Please Enter the Keyword for the analysis :")
# Twitter API Credentials
APIkey = ""
APISecretKey = ""
accessToken = ""
accessTokenSecreat = ""
# create the object for authentication
Auth = tweepy.OAuthHandler(APIkey, APISecretKey)
Auth.set_access_token(accessToken, accessTokenSecreat)
api = tweepy.API(Auth)
# display
posts = api.user_timeline(
    screen_name=TwitterProfileId, count=500, tweet_mode='extended')
i = 1
# print(posts)
for tweet in posts[:50]:  # just want to see the top 50 from 500
    print(str(i) + ') ' + tweet.full_text + '\n')
    i = i+1

# Creating dataframe with a column having name "tweets"
df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweet'])
print(df)

# make a function to clean tweets


def cleanTxt(texts):
    texts = re.sub('@[A-Za-z0-9]+', '', texts)  # removing mentions
    texts = re.sub("#", '', texts)  # removing #
    texts = re.sub('RT[\s]+', '', texts)  # removing Retweets
    texts = re.sub('https?:\/\/\S+', '', texts)  # removing links
    return texts


df['Tweet'] = df['Tweet'].apply(cleanTxt)
print(df)
# sentiments
analysis = TextBlob("Yesterday was a brilliant day")
analysis.sentiment
# creating function to get the tweet subjectivity


def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# creating function to get the tweet Polarity


def get_polarity(text):
    return TextBlob(text).sentiment.polarity


# create 2 columns 'Subjectivity' and 'Polarity'
df['Subjectivity'] = df['Tweet'].apply(get_subjectivity)
df['Polarity'] = df['Tweet'].apply(get_polarity)
print(df)

# Lets do Analysis

# Word Cloud Visualization
allwords = ' '.join([i for i in df['Tweet']])
Cloud = WordCloud(width=500, height=300, random_state=0,
                  max_font_size=100).generate(allwords)

plt.imshow(Cloud)
plt.show()

# Creating function to process positive,neutral and negative


def getAnalysis(ranking):
    if ranking < 0:
        return 'Negative'
    elif ranking == 0:
        return 'Neutral'
    else:
        return 'Positive'


df['Analysis'] = df['Polarity'].apply(getAnalysis)
print(df)

df[df['Analysis'] == 'Neutral']

df['Analysis'].value_counts()


print(df.shape)

# plotting scatter plot
plt.figure(figsize=(10, 8))
for i in range(0, df.shape[0]):
    plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')

plt.title("Sentimental Analyze")
plt.xlim(-1, 1)
plt.xlabel('Polarity(x axis)')
plt.ylabel('Subjectivity(y axis)')
plt.show()
# Only 3 neutral tweets would be shown because of data overlap

df['Analysis'].value_counts().plot(kind='bar')
plt.title("Sentimental Analyze")
plt.xlabel('Polarity(x axis)')
plt.ylabel('Count(y axis)')
plt.show()

# Lets get positive tweets only
i = 1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for j in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][j] == 'Positive'):
        print(str(i) + ') ' + sortedDF['Tweet'][j])
        print()
        i = i+1

# Lets get negative tweets only
i = 1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for j in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][j] == 'Negative'):
        print(str(i) + ') ' + sortedDF['Tweet'][j])
        print()
        i = i+1


# Lets get neutral tweets only
i = 1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for j in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][j] == 'Neutral'):
        print(str(i) + ') ' + sortedDF['Tweet'][j])
        print()
        i = i+1
