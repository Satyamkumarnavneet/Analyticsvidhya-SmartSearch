import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json

base_url = "https://courses.analyticsvidhya.com/"
course_paths = [
    "/courses/frameworks-for-effective-problem-solving",
    "/courses/your-ultimate-guide-to-becoming-an-agentic-ai-expert-by-2025",
    "/courses/a-comprehensive-learning-path-to-become-a-data-analyst-in-2025",
    "/courses/reimagining-genai-common-mistakes-and-best-practices-for-success",
    "/courses/coding-a-chatgpt-style-language-model-from-scratch-in-pytorch",
    "/courses/mastering-multilingual-genai-open-weights-for-indic-languages",
    "/courses/learning-autonomous-driving-behaviors-with-llms-and-rl",
    "/courses/genai-applied-to-quantitative-finance-for-control-implementation",
    "/courses/navigating-llm-tradeoffs-techniques-for-speed-cost-scale-and-accuracy",
    "/courses/applied-machine-learning-beginner-to-professional",
    "courses/ace-data-science-interviews",
    "courses/data-science-hacks-tips-and-tricks",
    "courses/getting-started-with-decision-trees",
    "courses/loan-prediction-practice-problem-using-python",
    "courses/big-mart-sales-prediction-using-r",
    "courses/twitter-sentiment-analysis",
    "courses/pandas-for-data-analysis-in-python",
    "courses/support-vector-machine-svm-in-python-and-r",
    "courses/nano-course-dreambooth-stable-diffusion-for-custom-images",
    "courses/building-large-language-models-for-code",
    "courses/cutting-edge-llm-tricks",
]

index = faiss.read_index("course_faiss.index")
with open("course_details.json", "r") as f:
    course_details = json.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_courses(query, top_k=5):
    # Encode the query to get its embedding
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    
    # Search the FAISS index for the top_k most similar courses
    distances, indices = index.search(query_embedding, top_k)
    results = []
    for idx, dist in zip(indices[0], distances[0]):
        course = course_details[idx]
        results.append({
            "title": course["title"],
            "description": course["description"],
            "curriculum": course["curriculum"],  # Include curriculum
            "additional_info": course["additional_info"],  # Include additional info
            "link": base_url + course_paths[idx],  # Use the base URL and course paths to generate the full link
            "distance": dist
        })
    return results

# Streamlit UI
st.title("Smart Search for Free Courses")
st.write("Search for free courses on Analytics Vidhya!")

query = st.text_input("Enter your query:")
if query:
    results = search_courses(query)
    for res in results:
        st.subheader(res['title'])
        st.write(res['description'])
        
        if res['curriculum']:
            st.write("### Curriculum")
            for item in res['curriculum']:
                st.write(f"- {item}")
        
        if res['additional_info']:
            st.write("### Additional Information")
            st.write(f"**Duration:** {res['additional_info'].get('duration', 'N/A')}")
            st.write(f"**Rating:** {res['additional_info'].get('rating', 'N/A')}")
            st.write(f"**Difficulty:** {res['additional_info'].get('difficulty', 'N/A')}")
        
        st.markdown(f"[Learn More]({res['link']})")
