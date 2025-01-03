import streamlit as st
from langchain.vectorstores import Pinecone
from langchain.embeddings import SentenceTransformersEmbeddings

# Initialize LangChain and Pinecone
embeddings = SentenceTransformersEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Pinecone(embeddings.embed_query, pinecone.Index("smart-search"))

# Define search function
def search_courses(query):
    results = vectorstore.similarity_search(query, k=5)
    return [{"title": res.metadata['title'], "description": res.metadata['description'], "link": res.metadata['link']} for res in results]

# Streamlit UI
st.title("Smart Search for Free Courses")
st.write("Search for free courses on Analytics Vidhya!")

query = st.text_input("Enter your query:")
if query:
    results = search_courses(query)
    for res in results:
        st.subheader(res['title'])
        st.write(res['description'])
        st.markdown(f"[Learn More]({res['link']})")
