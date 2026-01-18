import pandas as pd
import ollama
import json
import os

# Configuration
DATA_PATH = "feedback_data.csv"
OUTPUT_PATH = "analyzed_feedback_v2.csv"

def analyze_feedback_pro(text):
    """
    Advanced classification: Sentiment, Theme, Priority, and Smart Actions.
    """
    prompt = f"""
    You are an AI Business Analyst. Analyze the feedback below and return ONLY a JSON object.
    
    JSON Schema:
    {{
        "sentiment": "Positive/Negative/Neutral",
        "confidence": 0.0 to 1.0,
        "theme": "One-word category",
        "priority": "Low/Medium/High",
        "action_item": "A short 5-word recommendation for the team"
    }}

    Feedback: "{text}"
    """
    
    try:
        response = ollama.generate(model="llama3.2", prompt=prompt)
        # Extracting JSON specifically to handle LLM preamble text
        raw_res = response['response'].strip()
        start = raw_res.find('{')
        end = raw_res.rfind('}') + 1
        return json.loads(raw_res[start:end])
    except Exception as e:
        # Fallback for errors to keep the pipeline moving (Development Support)
        return {
            "sentiment": "Neutral", "confidence": 0.0, 
            "theme": "General", "priority": "Low", 
            "action_item": "Manual review required"
        }

def main():
    if not os.path.exists(DATA_PATH):
        print(f"Error: {DATA_PATH} not found. Run csv_creator.py first.")
        return

    df = pd.read_csv(DATA_PATH)
    print(f"🚀 Accelerating Analysis for {len(df)} entries...")

    results = []
    for _, row in df.iterrows():
        print(f"Processing ID {row['id']}...")
        analysis = analyze_feedback_pro(row['feedback_text'])
        results.append(analysis)

    # Convert list of dicts to DataFrame and merge
    analysis_df = pd.DataFrame(results)
    final_df = pd.concat([df, analysis_df], axis=1)

    # Data Cleaning: Ensure numeric types for visualization
    final_df['confidence'] = pd.to_numeric(final_df['confidence'])

    final_df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Success! Enhanced data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()