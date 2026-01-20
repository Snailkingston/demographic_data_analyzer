import streamlit as st
import pandas as pd
from demographic_data_analyzer import *

st.set_page_config(page_title="Demographic Data Analyzer", layout="centered")

st.title("Demographic Data Analyzer")
st.write("Upload the census dataset to analyze demographic questions.")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")

    st.subheader("Analysis Questions")

    if st.button("1. Count of people by race"):
        result = count_by_race(df)
        st.table(result)

    if st.button("2. Average age of men"):
        result = average_age_men(df)
        st.write(result)

    if st.button("3. % of people with Bachelors"):
        result = percentage_bachelors(df)
        st.write(f"{result}%")

    if st.button("4. % of people with advanced education earning >50K"):
        result = percentage_advanced_edu_rich(df)
        st.write(f"{result}%")

    if st.button("5. % of people without advanced education earning >50K"):
        result = percentage_non_advanced_edu_rich(df)
        st.write(f"{result}%")

    if st.button("6. Minimum hours worked per week"):
        result = min_hours(df)
        st.write(result)

    if st.button("7. % of people working min hours earning >50K"):
        result = rich_percentage_min_hours(df)
        st.write(f"{result}%")

    if st.button("8. Country with highest % earning >50K"):
        country, perc = country_highest_earning(df)
        st.write(f"{country}: {perc}%")

    if st.button("9. Most popular occupation in India earning >50K"):
        result = top_occupation_india_rich(df)
        st.write(result)
