# TASK 4: PERFORM SENTIMENT ANALYSIS USING NLP

# Step 1: Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import re
import string

# Step 2: Create Sample Dataset
data = {
    'review': [
        "I love this phone",
        "This product is amazing",
        "Best experience ever!",
        "Worst phone I've used",
        "Terrible product, waste of money",
        "I hate this service",
        "Absolutely wonderful",
        "So disappointed",
        "I’m not happy with this",
        "Great purchase, very satisfied"
    ],
    'sentiment': [
        'positive', 'positive', 'positive', 'negative', 'negative',
        'negative', 'positive', 'negative', 'negative', 'positive'
    ]
}
df = pd.DataFrame(data)
print(" Sample Data:")
print(df.head())

# Step 3: Text Preprocessing Function
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\[.*?\]', '', text)  # Remove text in brackets
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'<.*?>+', '', text)  # Remove HTML tags
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    text = re.sub(r'\n', '', text)  # Remove newline characters
    text = re.sub(r'\w*\d\w*', '', text)  # Remove words with digits
    return text

df['clean_review'] = df['review'].apply(clean_text)
print("\n Cleaned Text:")
print(df[['review', 'clean_review']])

# Step 4: Vectorize Text Data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['clean_review'])
y = df['sentiment']

# Step 5: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 7: Predict & Evaluate
y_pred = model.predict(X_test)

print("\n Accuracy:", accuracy_score(y_test, y_pred))
print("\n Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['negative', 'positive'], yticklabels=['negative', 'positive'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
