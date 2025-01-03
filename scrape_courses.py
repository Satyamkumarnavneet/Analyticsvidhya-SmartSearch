import requests
from bs4 import BeautifulSoup

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

def scrape_course_details(course_path):
    url = base_url + course_path
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract title
    title = soup.find("h1").text.strip() if soup.find("h1") else "No title found"
    
    # Extract description
    description = soup.find("meta", {"name": "description"})["content"].strip() if soup.find("meta", {"name": "description"}) else "No description found"

    # Extract curriculum
    curriculum_header = soup.find("h3", class_="section__heading", string="Course curriculum")
    curriculum = []
    if curriculum_header:
        # Get the list of curriculum items
        curriculum_list = curriculum_header.find_next("ul", class_="text-icon__list section__body")
        if curriculum_list:
            curriculum = [item.get_text(strip=True) for item in curriculum_list.find_all("h4")]
    
    # Extract additional course information (duration, rating, difficulty)
    additional_info = {}
    info_list = soup.select(".text-icon__list-item")
    for item in info_list:
        icon = item.find("i")
        if icon:
            if "fa-clock-o" in icon.get("class", []):
                additional_info["duration"] = item.find("h4").text.strip() if item.find("h4") else "No duration"
            elif "fa-star" in icon.get("class", []):
                additional_info["rating"] = item.find("h4").text.strip() if item.find("h4") else "No rating"
            elif "fa-signal" in icon.get("class", []):
                additional_info["difficulty"] = item.find("h4").text.strip() if item.find("h4") else "No difficulty level"

    return {
        "title": title,
        "description": description,
        "curriculum": curriculum,
        "additional_info": additional_info
    }

all_course_details = []
for path in course_paths:
    details = scrape_course_details(path)
    if details:
        all_course_details.append(details)

import json
with open("course_details.json", "w") as f:
    json.dump(all_course_details, f, indent=4)

print("Scraping completed. Details saved to 'course_details.json'.")