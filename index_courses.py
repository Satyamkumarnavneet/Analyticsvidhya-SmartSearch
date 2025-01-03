import os
from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone
pc = Pinecone(api_key="pcsk_3w7D2y_7gKiuNtfY95GV24vcf97XdGM1P1FptTGru9huTGHnG4byA6baqXgL7bGVVEnWYY")

# Check if index exists, if not create one
if 'course-index' not in pc.list_indexes().names():
    pc.create_index(
        name='course-index', 
        dimension=1536,  # Set the dimension of your embeddings here
        metric='euclidean',  # or cosine, depending on your needs
        spec=ServerlessSpec(
            cloud='aws',
            region='us-west-2'
        )
    )
