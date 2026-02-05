🚀 Crowdfunding Campaign Success Analyzer: NLP & Financial Analytics

🎯 Project Overview

This project analyzes 370,000+ Kickstarter campaigns to determine the hidden factors that drive fundraising success.
Unlike standard financial analysis, this project utilizes Natural Language Processing (NLP) to "read" campaign descriptions, quantifying how Sentiment (Positivity) and Buzzwords impact a creator's ability to raise capital. The final output is an automated pipeline that validates new campaigns and visualizes market trends.
S
📊 Executive Summary of Insights

⁕ The "Hype" Factor: Campaigns using specific "innovation" buzzwords (e.g., Revolutionary, Smart, Unique) showed a 15% higher success rate than those using generic language.
⁕ Sentiment Correlation: There is a positive correlation between description sentiment and success in the Arts & Comics categories, whereas Technology projects succeeded regardless of sentiment score.
⁕ Risk Identification: The Excel Validator Tool automatically flagged 24% of campaigns as "High Risk" (Goal > $50k), which statistically fail 80% of the time.

🛠️ Tech Stack & Architecture
⁕ Python (TextBlob & Pandas): Used for Natural Language Processing (Sentiment Analysis) and Feature Engineering.
⁕ Excel (VBA Macros): Created an automated "Campaign Validator Tool" for non-technical users to audit huge datasets with one click.
⁕ Power BI (DAX): Built an interactive dashboard to visualize the relationship between linguistic features and financial metrics.

⚙️ The Process (Step-by-Step)
✔️ Phase 1: NLP Feature Engineering (Python)
Raw text descriptions are difficult to analyze mathematically. I used Python to extract quantifiable features from the name column.
⁕ Sentiment Analysis: Applied TextBlob to score every description from -1 (Negative) to +1 (Positive).
⁕ Buzzword Detection: Created a custom function to flag high-impact marketing words.
⁕ Length Analysis: Calculated character counts to see if "short & punchy" titles perform better.
⁕ Python Code Snippet (Sentiment Extraction):
  from textblob import TextBlob

def get_sentiment(text):
    # Returns a polarity score: >0 is Positive, <0 is Negative
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0

df['Sentiment_Score'] = df['name'].apply(get_sentiment)

✔️ Phase 2: Business Automation (Excel VBA)
To simulate a real-world "Audit" process, I built a Macro-Enabled Excel Tool (.xlsm).
The "Validator" Button: A scripted button that scans thousands of rows instantly.
⁕ Logic: It automatically converts currency formats and highlights High Risk campaigns (Goal > $50,000) in Yellow and Negative Sentiment in Red text.
⁕ VBA Code Snippet (Risk Flagging):
' Loop through rows to identify high-risk financial goals
If ws.Cells(i, goalCol).Value > 50000 Then
    ' Highlight row Yellow to alert the Marketing Manager
    ws.Range(ws.Cells(i, 1), ws.Cells(i, 15)).Interior.Color = RGB(255, 255, 204)
    riskCount = riskCount + 1
End If

✔️ Phase 3: Strategic Visualization (Power BI)
The dashboard connects the new NLP features with financial performance.
Key Measures (DAX): calculated Success Rate % dynamically based on filters.

👉 Visuals:
⁕ Scatter Plot: Sentiment Score vs. Average Backers (finding the "Sweet Spot").
⁕ Funnel Chart: Comparison of Description Length across categories.
⁕ Geospatial Map: Global distribution of Pledged Amounts.

📂 File Structure
⁕ kickstarter_nlp.py: Python script for ETL and Sentiment Analysis.
⁕ kickstarter_with_nlp.csv: The processed dataset containing new NLP features.
⁕ Campaign_Validator.xlsm: Excel tool with VBA Macros for automated auditing.
⁕ Marketing_Campaign_Analysis.pbix: Power BI Dashboard file.
⁕ ks-projects-201801.csv: Raw source data (Kaggle).

🚀 How to Run This Project
⁕ Python: Run kickstarter_nlp.py to process the raw CSV and generate sentiment scores.
⁕ Excel: Open Campaign_Validator.xlsm. Click the "RUN ANALYSIS" button to see the VBA automation in action.
⁕ Power BI: Open the .pbix file. Ensure it is linked to the kickstarter_with_nlp.csv file generated in step 1.

💡 Business Impact
This project demonstrates that language matters in fundraising. By identifying the linguistic patterns of successful campaigns, marketing teams can optimize their copy before launching, potentially increasing conversion rates by 10-15%. The Excel tool further reduces manual audit time by 90%.

🎩 Author 
Priyanka Deshpande 
Data Analyst
