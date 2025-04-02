import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

if "conversation_history_data" not in st.session_state:
    st.session_state.conversation_history_data = []

def add_custom_css_data_bot():
    st.markdown("""
    <style>
    .user-message {
        background-color: #e0f7fa;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .bot-message {
        background-color: #f1f8e9;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def app():
    add_custom_css_data_bot()
    st.title("Data Analysis and Context Generation")

    uploaded_file = st.file_uploader("Choose a data file...", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.type == "text/csv":
            import pandas as pd
            data = pd.read_csv(uploaded_file)
            st.session_state.data = data
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            import pandas as pd
            data = pd.read_excel(uploaded_file)
            st.session_state.data = data
        
        st.write(data)

        st.chat_message("📊").write("Analyze the trends in this dataset.")

        user_prompt = st.chat_input("Enter your prompt here:")
        
        if user_prompt and "data" in st.session_state:
            # Hardcoded default prompt for analyzing datasets
            default_prompt = """
            You are tasked with analyzing a CSV file containing columns of dates and sales values. 

            The CSV file has the following columns:
            - **Date**: The date of the sale, formatted as MM-DD-YYYY or MM/DD/YYYY
            - **Sales**: The sales amount for that date

            Your job is to understand the data thoroughly and generate insightful responses based on it. You may need to provide answers related to:
            - Total sales in a month
            - Average sales per month
            - Sales on a specific day
            - And similar queries related to the sales data

            Ensure that your responses are clear and precise. Do not return any code as part of your answers.

            For instance, if you were given data like this:
            Date         | Sales
            -------------|--------
            10-01-2013   | 123.65499
            10-02-2013   | 125.455
            10-03-2013   | 108.58483
            10-04-2013   | 118.67466
            10-05-2013   | 121.33866
            10-06-2013   | 120.65533
            10-07-2013   | 121.795
            10-08-2013   | 123.033
            10-09-2013   | 124.049
            10-10-2013   | 125.96116
            10-11-2013   | 125.27966
            10-12-2013   | 125.9275
            10/13/2013   | 126.38333
            10/14/2013   | 135.24199
            10/15/2013   | 133.20333
            10/16/2013   | 142.76333
            10/17/2013   | 137.92333
            10/18/2013   | 142.95166

            You would need to analyze the data and provide answers without including any code in your response. Focus on deriving insights and making calculations based on the data provided.
            """

            
            combined_prompt = f"{default_prompt}\n{user_prompt}"

            data_text = st.session_state.data.to_string()

            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(
                [combined_prompt, data_text],
                generation_config = genai.types.GenerationConfig(
                                  temperature = 0.7),
                stream=True)
            response.resolve()

            st.session_state.conversation_history_data.append(("👦🏻", user_prompt, "user-message"))
            st.session_state.conversation_history_data.append(("🤖", response.text, "bot-message"))

            # Display the conversation history
            for speaker, message, css_class in st.session_state.conversation_history_data:
                st.markdown(f'<div class="{css_class}">{speaker} : {message}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
