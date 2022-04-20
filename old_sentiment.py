# cities = ['Silchar','Guwahati']
# score = []
# sentiment = []

# for city in cities:
#     city_data = pd.read_csv("./final datasets/" + city + "_data.csv")
# for i in range(len(city_data)):
#     fullText = ""
#     if city_data.loc[i,'Full Text']==city_data.loc[i,'Full Text']:
#         fullText = city_data.loc[i,'Full Text']
#         words = fullText.split(' ')
#         sentimentScore = 0
#     for word in words:
#         sentimentScore += sia.polarity_scores(word)['compound']    
#     sentimentScore /= len(fullText)
#     score.append(sentimentScore)
#     if (sentimentScore < -0.5):
#         sentiment.append('Very Negative')
#     elif (sentimentScore < 0.0): 
# sentiment.append('Negative')
#     elif (sentimentScore == 0.0):
#         sentiment.append('Neutral')
#     elif (sentimentScore > 0.5):
#         sentiment.append('Very Positive')
#     elif (sentimentScore > 0.0):
#         sentiment.append('Positive')

# city_data['Sentiment Score'] = score
# city_data['Sentiment'] = sentiment
# city_data.to_csv("./final datasets/" + city + "_data.csv")