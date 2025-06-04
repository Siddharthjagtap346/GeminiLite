# GeminiLite Semantic Search

🧠 GeminiLite is an expert-level semantic search engine built with Python, Flask, and TF-IDF vectorization. It supports multilingual queries, voice input, and provides highlighted relevant results with a clean UI designed using Tailwind CSS.

---

## Features

- **Semantic Search** using classic TF-IDF vectorization.
- **Voice Input** powered by Web Speech API (browser support required).
- **Multilingual Support** for searching in multiple languages.
- **Dark Mode Toggle** with smooth transitions.
- **Highlighted Search Terms** in results.
- **API Endpoint** for programmatic search access.
- Responsive, modern UI with Tailwind CSS.
- Suggested queries and clickable tags for easy searching.

---

## Technologies Used

- Python 3.x
- Flask web framework
- scikit-learn (for TF-IDF vectorization)
- Tailwind CSS for styling
- JavaScript Web Speech API for voice input

---

## Setup and Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/GeminiLite.git
   cd GeminiLite
Create a virtual environment (recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app

bash
Copy
Edit
python app.py
Open your browser and go to

cpp
Copy
Edit
http://127.0.0.1:5000/
Usage
Type your query in the search box or use the 🎤 voice input button to speak your query.

Click suggested tags or questions for quick searches.

Toggle between dark and light mode using the 🌙 button.

View highlighted keywords and relevance scores in results.

API
GET /api/search?q=your_query

Returns JSON array of search results with highlights and relevance scores.

Project Structure
cpp
Copy
Edit
GeminiLite/
├── app.py
├── vector_engine.py
├── data/
│   └── corpus.txt
├── templates/
│   └── index.html
├── static/
│   └── (CSS and JS files if any)
├── requirements.txt
└── README.md
Screenshots



Future Improvements
Integrate deep learning models like transformers for semantic understanding.

Add support for more natural language queries.

Improve voice recognition with multi-language capabilities.

Add user authentication and personalized search history.

Contact
Created by [Your Name]
GitHub: https://github.com/yourusername
Email: your.email@example.com

License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### [Download the complete README.md file here](sandbox:/mnt/data/README.md)

---

If you want, I can also help you draft a professional GitHub repo description or help with any other part! Just ask.
