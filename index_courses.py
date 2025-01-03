import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from scrape_courses import all_course_details  # Import the scraped course data

# Initialize SentenceTransformer model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to store course details in FAISS
def store_in_faiss(course_details):
    titles = [course["title"] for course in course_details]
    descriptions = [course["description"] for course in course_details]

    # Combine titles and descriptions into one string for a more comprehensive embedding
    combined_texts = [title + " " + description for title, description in zip(titles, descriptions)]

    # Generate embeddings for course details
    embeddings = model.encode(combined_texts)

    # Convert embeddings to numpy array for FAISS
    embeddings = np.array(embeddings).astype("float32")

    # Initialize FAISS index
    dimension = embeddings.shape[1]  # Get the dimensionality of the embeddings
    index = faiss.IndexFlatL2(dimension)  # Use L2 distance for similarity

    # Add embeddings to FAISS index
    index.add(embeddings)

    return index

# Store course details in FAISS
faiss_index = store_in_faiss(all_course_details)

# Optionally, save the FAISS index to disk
faiss.write_index(faiss_index, "course_faiss.index")

print("Indexing completed. FAISS index saved to 'course_faiss.index'.")
