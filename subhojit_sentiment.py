# This python program:
# 1. Opens sample csv file 'sampleCSV'
# 2. Generates new csv file 'outputCSV'
# 3. tranlates (or attempts to translate) main text data in sampleCSV to english
# 4. Analyses sentiment of the main text and scores it as well as corresponds the scores to very -ve, -ve, neutral, +ve and very +ve
# 5. Writes each row and data to outputCSV

import csv
from numpy import full
from translate import Translator
from textblob import TextBlob as TB
import emoji

sampleCSV = 'Silchar.csv'
outputCSV = 'TranslatedSilchar.csv'

rowNum = 1

with open (sampleCSV, 'r', encoding = 'utf-8') as csvFile:
    with open (outputCSV, 'w', encoding = 'utf-8', newline = '') as outFile:

        data = csv.DictReader (csvFile)
        # fieldNames = ['Id', 'Created (UTC)', 'Latitude', 'Longitude', 'Text', 'Full Text', 'Translated Text', 'User Name', 'User Mentions', 'Hashtags', 'Language', 'Retweet count', 'Country', 'Place', 'Image']
        fieldNames = ['Full Text', 'Translated Text', 'Sentiment Score', 'Sentiment']
        writer = csv.DictWriter (outFile, fieldnames = fieldNames)
        writer.writerow ({'Full Text': 'Full Text', 'Translated Text': 'Translated Text', 'Sentiment Score': 'Sentiment Score', 'Sentiment': 'Sentiment'})

        for ii in data:
            fullText = ii['Text'] + " " + ii['Full Text']
            fullText = " ".join (fullText.split())
            fullText = emoji.demojize(fullText,delimiters=("", " ")).replace('_',' ').replace('-',' ')

            language = ii['Language']

            if (language != 'en'):
                translatedText = Translator(from_lang = language, to_lang = 'en').translate (text = fullText)
            else:
                translatedText = fullText
            translatedText = TB (translatedText)

            sentimentScore = translatedText.sentiment.polarity
            sentimentScore = float (sentimentScore)
            if (sentimentScore < -0.5):
                sentiment = 'Very Negative'
            elif (sentimentScore < 0.0): 
                sentiment = 'Negative'
            elif (sentimentScore == 0.0):
                sentiment = 'Neutral'
            elif (sentimentScore > 0.5):
                sentiment = 'Very Positive'
            elif (sentimentScore > 0.0):
                sentiment = 'Positive'

            writer.writerow ({'Full Text': fullText, 'Translated Text': translatedText, 'Sentiment Score': sentimentScore, 'Sentiment': sentiment})

            print ('Row', rowNum, 'Done')
            rowNum += 1