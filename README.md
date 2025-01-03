# Smart Search for Free Courses on Analytics Vidhya

## Project Overview

Smart Search is a project aimed at implementing an advanced search feature for free courses available on the Analytics Vidhya platform. The goal is to enable users to find the most relevant courses based on natural language queries using state-of-the-art machine learning techniques.

## Objective

The objective of this project is to implement a Smart Search feature that allows users to find the most relevant courses on the Analytics Vidhya platform based on their natural language queries. This is achieved using LangChain, FAISS, and Sentence Transformers to provide an efficient, scalable, and accurate search experience.


## Key Features
- Advanced search algorithms
- User-friendly interface
- Real-time search results
- Customizable search parameters

## Technologies Used
- LangChain
- FAISS
- Sentence Transformers (all-MiniLM-L6-v2)
- Streamlit

## Architecture
1. **Data Collection & Preprocessing:** Scraping course data from Analytics Vidhya.
2. **Embedding Generation:** Converting textual data into numerical vectors using Sentence Transformers.
3. **FAISS Indexing:** Building an efficient similarity search system.
4. **Integration with Streamlit:** Developing a user-friendly search interface.
5. **Ranking and Result Presentation:** Displaying relevant courses based on cosine similarity.


## Directory Structure
```
Analyticsvidhya-SmartSearch/
│
├── courses.json               # Scraped course data
├── scrape_courses.py          # Data scraping script
├── index_courses.py           # Embedding and indexing script
├── app.py                     # Streamlit application
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

## Implementation Details
- **Data Collection:** Scraping course titles, descriptions, curriculum, and additional information.
- **Embedding Generation:** Using Sentence Transformers to generate embeddings.
- **FAISS Indexing:** Creating an efficient and scalable search index.
- **Streamlit Integration:** Implementing a search interface for user interaction.
- **Ranking Mechanism:** Using cosine similarity to rank and display courses.

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Satyamkumarnavneet/Analyticsvidhya-SmartSearch.git
2. Navigate to the project directory:
   ```bash
   cd Analyticsvidhya-SmartSearch
3. Install dependencies:
   ```
   pip install -r requirements.txt
4. Run the application:
   ```
   streamlit run app.py
## Performance
- FAISS-based indexing ensures fast search results even for large datasets.
- The system is scalable and can handle a large number of courses efficiently.

## Usage
- Open your web browser and go to ```http://localhost:8501```.
- Enter your search query in the search bar.
- Customize search parameters if needed.
- View the search results in real-time.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For support, email `navneetsatyamkumar@gmail.com`.

---



