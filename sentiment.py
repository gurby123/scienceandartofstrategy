import nltk
nltk.download('vader_lexicon')  # download the pre-trained model

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# create an instance of the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# define some text to analyze
text = "I love this movie! The acting was great and the plot kept me engaged."

# use the sentiment analyzer to get a sentiment score for the text
scores = sid.polarity_scores(text)

# print the sentiment score
print(scores)
