import streamlit as st
import re
import pandas as pd
from sentence_transformers import SentenceTransformer


# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

# Function to clean user query
def clean_data(data):
    # Remove punctuation and convert to lowercase
    data = re.sub(r'[^\w\s]', '', data)
    data = data.lower()
    return data

# Function to extract subtitle IDs from the 'num_list' column
def extract_id(id_list):
    return [item.split('-')[0] for item in id_list]

# Streamlit UI
st.title("Movie Subtitle Search Engine")
search_query = st.text_input("Please enter the name of a movie or series for searching.")

if st.button("Search"):
    st.subheader("Relevant Subtitle Files")
    search_query = clean_data(search_query)
    query_embed = model.encode(search_query).tolist()
    
    # Simulated query to the provided DataFrame
    df_10_percentage = pd.read_csv("C:/Users/deshp/Downloads/df_10_percentage.csv")  # Replace "your_data.csv" with the actual file path
    
    # Replace this section with your actual database querying code
    # For demonstration purposes, we'll just simulate a query using the provided DataFrame
    id_list = df_10_percentage['Movies/Series'].tolist()
    
    # Display the results
    for id in id_list:
        file_name = f"{id}"
        st.markdown(f"[{file_name}](https://www.opensubtitles.org/en/subtitles/{id})")