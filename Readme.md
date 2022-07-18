# Twitter Sentimental Analysis

#### **PROBLEM STATEMENT:**

Analyzing twitter sentiments based on latest twitter data.

#### **MOTIVATION:**

Sentimental analysis is an extremely common machine learning problem and is used in a lot of activities like product predictions, movie recommendations, and several others.
Currently for every machine learner new to this field, like myself, exploring this domain has become an integrate facet, and so I explored this topic and tried to build a project of my own. I thought it would be a good idea to obtain insights into how Twitter users felt about different domains.
I enjoyed the process and learned many things through my journey.

#### **ABSTRACT**

Nowadays, people from all around the world use social media to share their views or any information. Twitter is an online news and social networking site where people communicate in short messages called tweets. Users share their daily lives, post their opinions on everything such as brands and places.
Companies can benefit from this massive platform in various ways:
• They can use twitter to increase their brand awareness
• Inform customers about the updates
• To get instant feedback about their product and services
• Collect data related to opinions on them
The most important thing for a company is to listen to market and meet the customers need. When companies grow it becomes difficult for them to pay attention to each customer’s review and know what people think about them, this is where SENTIMENTAL ANALYSIS comes to use.

#### **SENTIMENTAL ANALYSIS**

Sentimental analysis is the process of detecting positive and negative sentiment in text. It is also known as opinion mining.
Sentimental analysis has been acquiring a crucial role in both commercial and research applications because of their possible applicability to several different fields. Therefore, a huge number of companies have included the analysis of opinions and sentiments of customers as part of their mission.
One of the most interesting applications of these approaches involves the automatic analysis of social network messages, on the basis of the feelings and emotions conveyed.

#### **WHY SENTIMENTAL ANALYSIS?**

o Business: In marketing field companies use it to develop their strategies, to understand customer’s feelings towards products or brand, how people respond to their campaigns or product launches and why some of their products fail.
o Politics: In political field, it is used to keep track of political view, to detect consistency and inconsistency between statements and actions at the government level. It can be used to predict election results as well!
o Public Actions: It is also used to monitor and analyze social phenomena, and determing the general mood of the public.

#### **METHODS AND TOOLS REQUIRED**

This project was done using NLP (Natural Language Processing) techniques. Twitter receives over 500 million tweets per day, across the globe. Hence, our work is to retrieve the data and analyze it.

#### **DEVELOPER ACCOUNT**

In order to fetch tweets through Twitter API, one needs to create a “TWITTER DEVELOPER ACCOUNT” from twitter developer portal and register an app through their twitter account.
![image](https://user-images.githubusercontent.com/90335449/179509023-22cfbfba-c43c-4f31-b9e3-abf5b5c8bf67.png)

Once the app is created, open the ‘Keys and Tokens’ tab, and copy ‘API Key’, ‘API Secret’, ‘Access token’ and ‘Access Token Secret’.
![image](https://user-images.githubusercontent.com/90335449/179509053-246a4466-0e2d-4b9f-a54f-7fbd5f008879.png)

**I carried out the following steps for the project:**</br>
• Import libraries</br>
• Tweets mining</br>
• Data cleaning</br>
• Tweets processing</br>
• Data exploration</br>
• Sentimental Analysis</br>
![image](https://user-images.githubusercontent.com/90335449/179509106-dc8aa6e2-dc40-49e2-83fd-611484869d84.png)

#### **IMPORTING LIBRARIES**

Python libraries like :-
• Tweepy :- for tweets mining
• Pandas :- for data cleaning/manipulation
• TextBlob :- for sentimental analysis
• MatPlotlib :- Data exploration
• WordCloud :- Data exploration
• Re :- Regular expression, it lets you check is a particular string matches a given expression

#### **TWEETS MINING**

Authorize twitter API client.

We use this code to fetch tweets, and filter the retweets and links after authorization of Twitter API.
![image](https://user-images.githubusercontent.com/90335449/179509143-89129b80-c12b-454f-b7b9-5b9c9374a3ce.png)

I created a dataframe using pandas library.

#### **DATA CLEANING AND TWEETS PROCESSING**

Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.
The ultimate goal is to clean up the individual tweets.
To remove the mentions, #, and emojis, I created a function cleanTxt(text) which uses re library.
![image](https://user-images.githubusercontent.com/90335449/179509190-d95b51c3-2012-4d88-accc-637c915f2271.png)

To make the cleaning more efficient, I converted all the tweets to lower case, removed the punctuation marks, or any irrelevant character and also removed stop words from the tokens, by using stop words library.
Stop words are the commonly used words which are irrelevant in text analysis like I, am, you, are, etc.
Additionally, I used a concept known as “Lemmatization”. This is a process of returning words to their “base” form. I implemented it using WordNetLemmatizer.

Note that, the more you clean your data, the more effective and accurate your result will be.

#### **DATA EXPLORATION**

##### **WORD CLOUD**

It is a visual representation of text data, which is often used to depict keyword metadata.
![image](https://user-images.githubusercontent.com/90335449/179509303-0c0bea02-ad77-4f8a-9ee9-968cb1025913.png)

Using the WordCloud library, you can generate a Word Cloud based on the word frequency and superimpose these words on any image. In this case, I used a rectangular block and Matplotlib to display the image. The Word Cloud shows, words with higher frequency in bigger text size while “not-so” common words are in smaller text sizes.
It can also be used to check whether our cleaning was successful or not, by taking a look at word cloud and seeing if the words make any sense or not.

#### **SENTIMENTAL ANALYSIS**

For this analysis, I went with TextBlob. Text Blob analyzes sentences by giving each tweet a Subjectivity and polarity score. Based on the Polarity score, one can define which tweets were Positive, Negative, or Neutral.
Polarity simply means emotions expressed in a sentence. Emotions are closely related to sentiments. The strength of a sentiment is typically linked to the intensity of certain emotions, e.g., joy and anger.
Subjectivity, subjective sentence expresses some personal feelings, views, or beliefs. A subjective sentence may not express any sentiment.
I created two columns of subjectivity and polarity in my dataframe.
![image](https://user-images.githubusercontent.com/90335449/179509367-9736ec22-07c4-4eda-af12-1bf07181e7e1.png)

A polarity score of < 0 is Negative, 0 is Neutral while>0 is Positive. I used the “apply” method on the “Polarity” column in my dataframe to return the respective sentiment category. And create a column “Analysis”.
Now, subsequently analysis has been for all the positive/negative tweets or not.

#### **POLARITY AND SUBJECTIVITY GRAPH**

![image](https://user-images.githubusercontent.com/90335449/179509400-3575b12d-0730-4a7b-888a-73f764b3231f.png)

#### **CALCULATING THE PERCENTAGE AND NUMBER OF POSITIVE, NEGATIVE, NEUTRAL TWEETS**

![image](https://user-images.githubusercontent.com/90335449/179509415-bf1de545-d611-4a2c-823f-2e2e5211366e.png)

#### **DISTRIBUTION OF SENTIMENTS CATEGORY**

![image](https://user-images.githubusercontent.com/90335449/179509446-7eb87bee-10c2-4b8f-852e-f13760a2c1d5.png)

#### **PROJECT LIMITATIONS AND CHALLENGES**

Insufficient or limited word coverage as many new words and their semantics must be updated in the lexical database.
The accuracy of sentiment classification is also challenging task in sentimental analysis for example, words such as “love” and “hate” are on positive (+1) and negative (-1) scores in polarity. But there are in-between conjugations of words such as “not-so-bad” that can mean “neutral”.
Also, people use irony and sarcasm in casual conversations and memes on social media. The act of expressing negative sentiment using backhanded compliments can make it difficult for sentimental analysis tools to detect the true context of what the response is actually implying.

#### **Conclusion**

I learned many new techniques and enjoyed the process. There were a lot of problems, but removing errors, yeah, that’s what we have to learn. The project may not give accurate results in some cases as mentioned above, and there are quite a few solutions too, I will definitely explore this domain further.

#### **REFERENCES**

• https://www.ijcaonline.org/research/volume125/number3/dandrea-2015-ijca-905866.pdf
• https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
• https://textblob.readthedocs.io/en/dev/_modules/textblob/en/sentiments.html
• https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
• https://towardsdatascience.com/step-by-step-twitter-sentiment-analysis-in-python-d6f650ade58d
