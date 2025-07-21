# -SENTIMENT-ANALYSIS
*COMPANY NAME*-- CODTECH IT SOLUTIONS PVT.LTD

*NAME*: DIVYA H

*INTERN ID*: CT04DG233

*DOMAIN*:  DATA ANALYTICS

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR 

# DESCRIPTION FOR TASK 4:
Task Overview: Sentiment Analysis Using Natural Language Processing (NLP)
In this task, the focus is on applying Natural Language Processing (NLP) techniques to analyze sentiments expressed in textual data such as tweets, product reviews, survey responses, or feedback forms. These unstructured text sources hold rich information about customer opinions, user experiences, and social sentiment that, when analyzed, can provide critical insights for business, research, or social monitoring.

The primary objective is to classify the sentiments embedded in the text as positive, negative, or neutral. To achieve this, the task involves several stages: cleaning and preprocessing the raw text, applying sentiment analysis tools like TextBlob, and visualizing common words using a WordCloud. This hands-on project helps in mastering foundational NLP skills and understanding how machines can derive meaning from human language.

# Objective of the Task
This task aims to:

Transform raw text into clean, structured form suitable for analysis.

Apply sentiment polarity analysis to determine the emotional tone of the text.

Visualize the most common or important words in the corpus.

Build a basic but functional text classification pipeline to automate the categorization of sentiments.

This approach is widely used in applications such as customer service analytics, product feedback evaluation, brand monitoring on social media, and more.

# Key Skills Practiced
1. NLP Preprocessing (Cleaning, Lemmatization, Stopword Removal)
Before performing any analysis, the raw text must be cleaned and normalized. This process includes:

Lowercasing all text to standardize input.

Removing punctuation, special characters, numbers, and irrelevant symbols using regex or string methods.

Tokenization: Splitting text into individual words or tokens.

Stopword Removal: Eliminating common words like “the”, “is”, and “and” that don’t add significant value to sentiment analysis.

Lemmatization: Reducing words to their base or dictionary form (e.g., “running” becomes “run”) to reduce word variation.

Tools like NLTK, spaCy, or built-in string functions in Python are typically used in this stage.

2. Sentiment Polarity Analysis
After preprocessing, TextBlob is used to perform sentiment analysis. TextBlob is a simple NLP library built on top of NLTK and Pattern, and it provides a built-in method for analyzing the polarity and subjectivity of text:

Polarity: A float within the range [-1.0, 1.0], where -1 is extremely negative, and 1 is extremely positive.

Subjectivity: A float within the range [0.0, 1.0], where 0 is very objective, and 1 is very subjective.

Based on polarity, we can classify the sentiment of a sentence or document as:

Positive: Polarity > 0

Neutral: Polarity = 0

Negative: Polarity < 0

This simple yet effective classification can be applied across thousands of text samples to get a big-picture view of audience sentiment.

3. WordCloud Visualization
A WordCloud is a popular way to visually explore the most frequent words in a corpus. It presents words in varying font sizes based on their frequency or importance. It helps:

Identify keywords and topics people are talking about.

Highlight frequent positive or negative terms.

Serve as an engaging way to communicate textual insights in reports or dashboards.

Libraries like wordcloud and matplotlib are used to generate these visualizations.

4. Text Classification
Although this task uses rule-based classification with TextBlob, the framework lays the foundation for more advanced machine learning-based text classification, such as using Naive Bayes, Logistic Regression, or Transformers. Here’s a basic classification process:

Preprocess the text.

Calculate sentiment scores using TextBlob.

Classify based on polarity thresholds.

Assign a sentiment label to each record (positive, neutral, negative).

The classified results can then be aggregated or visualized to observe trends over time, geography, product type, or demographic groups.

# Example Use Case
Imagine working with a dataset of 10,000 customer reviews for a retail brand. Here's how this task would unfold:

Clean and tokenize the review texts.

Lemmatize and remove stopwords to normalize the content.

Use TextBlob to assign a sentiment score to each review.

Classify each review based on its polarity.

Visualize the most frequent positive and negative terms using separate WordClouds.

Aggregate the sentiment results to report overall brand perception or identify problem areas.
  
- ---output---
- <img width="881" height="606" alt="Image" src="https://github.com/user-attachments/assets/127a4814-6685-4bf0-9331-28d80f0700ee" />

<img width="676" height="271" alt="Image" src="https://github.com/user-attachments/assets/e3557599-6c7a-4dde-873a-4e448e783db4" />

<img width="876" height="734" alt="Image" src="https://github.com/user-attachments/assets/4fef5841-40fd-4404-aa29-a0d0ec17a9ff" />

  

