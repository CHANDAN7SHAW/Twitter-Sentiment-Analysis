# Twitter-Sentiment-Analysis
Sentiment analysis of tweets for a given keyword using Python.

Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. 
It’s also known as opinion mining, deriving the opinion or attitude of a speaker.

## Installation
We used few python libraries to implement this entire project
1. Tweepy: Tweepy is open-sourced, hosted on GitHub and enables Python to communicate with Twitter platform and use its API. 
           install it using folloing pip command:
           'pip install tweepy'
           
2.TextBlob: TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural 
language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification,translation,
and more.
            install it using following pip command
            'pip install textblob'
                            
Also we need to install some NLTK corpora. Corpora is nothing but a large and structured set of texts.
            install it using folloing command
            'python -m textblob.download.corpora'

##Authentication
In order to fetch tweets through Twitter API, one needs to register an App through their twitter account. 
Follow these steps for the same:
            - open 'https://apps.twitter.com/' link and click the button: 'Crrate new app'
            -	Fill the application details and create one dummy app.
            -	Open the ‘Keys and Access Tokens’ tab.
            -	Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.
            
We follow these 3 major steps in our program:
            - Authorize twitter api client
            -	Make a GET request to twitter API to fetch tweets for a particular query
            - Parse the tweets, classify each tweets as positive, negative or neutral.
            
##visualization
 At last we create one pie plot to visualize the final analysis of toal outcome.
