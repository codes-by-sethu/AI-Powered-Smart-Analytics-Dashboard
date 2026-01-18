import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE CONFIG
st.set_page_config(page_title="AI Smart Analytics", layout="wide")
st.title("📊 AI-Powered Smart Analytics Dashboard")

# 2. LOAD ANALYZED DATA
@st.cache_data
def load_data():
    return pd.read_csv("analyzed_feedback.csv")

try:
    df = load_data()

    # 3. METRICS ROW
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Feedback", len(df))
    col2.metric("Positive Sentiment", len(df[df['sentiment'] == 'Positive']))
    col3.metric("Top Theme", df['theme'].mode()[0])

    st.divider()

    # 4. VISUALIZATIONS
    left_chart, right_chart = st.columns(2)

    with left_chart:
        st.subheader("Sentiment Distribution")
        fig_sent = px.pie(df, names='sentiment', color='sentiment',
                         color_discrete_map={'Positive':'#00CC96','Negative':'#EF553B','Neutral':'#636EFA'})
        st.plotly_chart(fig_sent, use_container_width=True)

    with right_chart:
        st.subheader("Key Feedback Themes")
        theme_counts = df['theme'].value_counts().reset_index()
        fig_theme = px.bar(theme_counts, x='theme', y='count', color='theme')
        st.plotly_chart(fig_theme, use_container_width=True)

    # 5. RAW DATA TABLE
    st.subheader("Detailed Analysis")
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error("Please run classifier.py first to generate the analyzed_feedback.csv file!")