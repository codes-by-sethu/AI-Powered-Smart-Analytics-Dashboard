import pandas as pd
import ollama
import json
import os

# 1. LOAD THE DATA
# Ensure you have created the feedback_data.csv file first
DATA_PATH = "feedback_data.csv"
OUTPUT_PATH = "analyzed_feedback.csv"

def analyze_sentiment(text):
    """
    Uses Llama 3.2 to extract sentiment and theme in structured JSON format.
    """
    prompt = f"""
    Analyze the following feedback and return ONLY a JSON object with two keys:
    "sentiment" (Positive, Negative, or Neutral) and 
    "theme" (one-word category like Support, Pricing, Speed, UX, or AI).

    Feedback: "{text}"
    """
    
    response = ollama.generate(model="llama3.2", prompt=prompt)
    
    # Clean the response to ensure it only contains JSON
    response_text = response['response'].strip()
    try:
        return json.loads(response_text)
    except:
        # Fallback in case the LLM adds conversational text
        if "Positive" in response_text: s = "Positive"
        elif "Negative" in response_text: s = "Negative"
        else: s = "Neutral"
        return {{"sentiment": s, "theme": "General"}}

def main():
    if not os.path.exists(DATA_PATH):
        print(f"Error: {DATA_PATH} not found.")
        return

    df = pd.read_csv(DATA_PATH)
    print(f"--- Processing {len(df)} feedback entries ---")

    sentiments = []
    themes = []

    for index, row in df.iterrows():
        print(f"Analyzing ID {row['id']}...")
        result = analyze_sentiment(row['feedback_text'])
        sentiments.append(result.get('sentiment'))
        themes.append(result.get('theme'))

    # 2. ENRICH DATASET
    df['sentiment'] = sentiments
    df['theme'] = themes

    # 3. EXPORT FOR POWER BI
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"--- Analysis Complete! Saved to {OUTPUT_PATH} ---")

if __name__ == "__main__":
    main()