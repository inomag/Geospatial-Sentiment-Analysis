# Geospatial Sentiment Analysis

## Dataset Information

We use and compare various different methods for sentiment analysis on tweets (a binary classification problem). The training dataset is expected to be a csv file of type `Demojized, Captions, Latitude, Longitude, Created Time, Sentiment, Sentiment Score, Full text` where the `Demojized` column consists of raw tweet text with the emojis translated, `Captions` consisting the captions of the instagram post mentioned in the tweet, `Full Text` consisting whole demojized and captions which are further translated to English, `Sentiment score` is between `-1` (negative) to `1` (positive), and `Sentiment` is the remark given within a certain range of sentiment score.

## Requirements

There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.  
* `numpy`
* `pandas`
* `goslate`
* `textblob`
* `emoji`

## Usage

### Preprocessing 

1. Run `image_urls.ipynb` on test data. This will generate a dataset which will consist all the redirected image urls.
2. Run `translate.ipynb` on test data. This gives the demojized, captions, and the other necessary columns in the training dataset. 
3. Run `sentiment.ipynb` on training data. This will generate the sentiment score and remark of the full text.

After the above steps, you should have two extra files for each test dataset: `<Name>_captions.csv` `<Name>_Data.csv` which are the image urls and final dataset respectively.

... *In Progress*
