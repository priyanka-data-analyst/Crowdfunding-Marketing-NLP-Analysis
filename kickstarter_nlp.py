import pandas as pd
from textblob import TextBlob
import re

# 1. LOAD THE DATA
# PASTE YOUR WORKING PATH HERE inside the quotes!
file_path = "ks-projects-201801.csv"
print("Loading dataset... (This might take 30 seconds)")
df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)

# Filter for just the columns we need to speed it up
# We only need ID, Name, Category, Goal, Pledged, State, and most importantly: NAME (Description)
df = df[['ID', 'name', 'category', 'main_category', 'currency', 'deadline', 'goal', 'launched', 'pledged', 'state', 'backers', 'country']]

# Drop rows where the name (description) is missing
df = df.dropna(subset=['name'])

# 2. DEFINE NLP FUNCTIONS

def get_sentiment(text):
    """Returns a score from -1 (Negative) to 1 (Positive)"""
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0

def check_buzzwords(text):
    """Returns 1 if the campaign uses 'hype' words, 0 otherwise"""
    buzzwords = ['innovative', 'revolutionary', 'help', 'unique', 'first', 'smart']
    text_lower = str(text).lower()
    for word in buzzwords:
        if word in text_lower:
            return 1 # Found a buzzword
    return 0

# 3. APPLY THE NLP (The heavy lifting)
print("Analyzing text descriptions... (This takes a moment)")

# Create Feature 1: Description Length (Character count)
df['Name_Length'] = df['name'].astype(str).apply(len)

# Create Feature 2: Buzzword Flag
df['Has_Buzzword'] = df['name'].apply(check_buzzwords)

# Create Feature 3: Sentiment Score (How positive is the title?)
# We use the first 10,000 rows for speed testing.
# Remove .head(10000) if you want to run it on ALL rows (might take 5 mins).
df_small = df.head(20000).copy()
df_small['Sentiment_Score'] = df_small['name'].apply(get_sentiment)

# 4. EXPORT
output_file = "kickstarter_with_nlp.csv"
df_small.to_csv(output_file, index=False)
print(f"Success! Processed file saved as: {output_file}")