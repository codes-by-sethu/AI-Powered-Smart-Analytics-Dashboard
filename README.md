Here is a **pure technical version** — concise, engineer-focused, no storytelling.

---

## 📊 AI-Powered Smart Analytics Dashboard (Technical Overview)

### System Purpose

End-to-end pipeline for automated analysis of unstructured textual feedback using a **local LLM**, producing structured, confidence-scored outputs and real-time visual analytics.

---

## 🧠 Core Architecture

**1. LLM Inference Layer**

* Model: **Llama 3.2** (Ollama, local runtime)
* Mode: **Zero-shot classification**
* Tasks:

  * Sentiment classification: `{Positive, Neutral, Negative}`
  * Theme extraction: `{Support, Pricing, UX, Performance, Other}`
  * Action suggestion generation
  * Confidence estimation per prediction

**2. Prompt-Driven Classification**

* Deterministic structured JSON output
* Strict schema enforcement for downstream processing
* Temperature tuned for classification stability

---

## 🔁 Data Pipeline

**Input:**

* CSV files containing raw text feedback

**Processing Steps:**

1. Text normalization and null handling
2. Batched LLM inference via Ollama API
3. JSON response validation and parsing
4. Priority scoring logic based on:

   * Negative sentiment
   * Theme severity
   * Confidence threshold

**Output:**

* Clean, structured DataFrame (CSV / in-memory)

---

## 📊 Analytics & Visualization Layer

* **Framework:** Streamlit
* **Charts:** Plotly (bar, trend, heatmap)
* **Views:**

  * Sentiment distribution
  * Theme frequency
  * Urgent issue table
  * Confidence vs priority heatmap

---

## ⚙️ Tech Stack

* **Python:** 3.11+
* **LLM Runtime:** Ollama
* **Model:** Llama 3.2
* **Data Processing:** Pandas
* **Dashboard:** Streamlit + Plotly

---

## 🚀 Execution Flow

```text
CSV → classifier.py → LLM inference → structured CSV → dashboard.py → Streamlit UI
```

---

## ✨ V2 Enhancements

* Priority-based issue detection
* AI confidence scoring (avg ≈ 0.79)
* Per-feedback action recommendations
* Multi-dimension heatmaps (sentiment × priority × confidence)

---

## 🔐 Deployment & Scalability

* Fully **offline / on-prem compatible**
* No external API calls → GDPR-safe
* Container-ready, **Azure-deployable**
* Scales horizontally with batch processing

---

## 🛠️ Setup

```bash
pip install -r requirements.txt
ollama pull llama3.2
python classifier.py
streamlit run dashboard.py
```
