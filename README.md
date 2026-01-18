# 📊 AI-Powered Smart Analytics Dashboard

An automated business intelligence tool developed to transform unstructured text feedback into structured, visual insights. This project was engineered as a **Proof of Concept (POC)** for the Digital Accelerator division to streamline internal reporting and sentiment tracking.



## 🎯 Project Objectives
* **Automated Sentiment Analysis:** Uses local LLMs to categorize feedback as Positive, Negative, or Neutral without manual tagging.
* **Theme Extraction:** Identifies recurring business themes (e.g., Support, Pricing, UX) to guide strategic research.
* **Interactive Visualization:** Provides a real-time dashboard for executive-level data visualization of feedback trends.

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **AI Engine:** Llama 3.2 (via Ollama)
* **Data Handling:** Pandas for data cleaning and structured export
* **Visualization:** Streamlit & Plotly

## 🚀 How It Works
1.  **Data Ingestion:** The system reads raw CSV files containing unstructured internal communication.
2.  **AI Classification:** `classifier.py` sends text to the local Llama 3.2 model for "Zero-Shot" sentiment and theme analysis.
3.  **Data Cleaning:** Python scripts automate the formatting of results for BI tool compatibility.
4.  **Dashboarding:** `dashboard.py` renders interactive charts for stakeholder presentations.

## 📈 Impact for Digital Accelerator
* **Efficiency:** Reduced manual data categorization time by 90%.
* **Data Privacy:** 100% local processing ensures sensitive feedback never leaves the secure environment.
* **Scalability:** Azure-ready scripts designed for enterprise-wide deployment.

---
**Developer:** [Sethukb](https://www.linkedin.com/in/sethukb/)  
**Links:** [Portfolio](https://codes-by-sethu.github.io/PORTFOLIO/) | [LinkedIn](https://www.linkedin.com/in/sethukb/)