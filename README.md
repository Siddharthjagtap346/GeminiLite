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

2. **Create a virtual environment (recommended)**
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the Flask app**
python app.py

5. **Open your browser and go to**
http://127.0.0.1:5000/
---

## Usage
-Type your query in the search box or use the 🎤 voice input button to speak your query.

-Click suggested tags or questions for quick searches.

-Toggle between dark and light mode using the 🌙 button.

-View highlighted keywords and relevance scores in results.

---

## API
-GET /api/search?q=your_query


## 📁 Project Structure

```
GeminiLite/
├── app.py                 # Main Flask backend
├── vector_engine.py       # TF-IDF-based semantic search logic
├── data/
│   └── corpus.txt         # Dataset of documents to search from
├── templates/
│   └── index.html         # Tailwind-powered frontend interface
├── static/                # (Optional) JS, CSS, or assets folder
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Screenshots 

-UI
![image](https://github.com/user-attachments/assets/6a632f84-f7ee-40cb-94e1-24bb5ddfe27a)

-Voice search ui
![Screenshot 2025-06-04 201538](https://github.com/user-attachments/assets/3c64a571-f6dc-4355-b297-d42eb5ff675c)

-Search output
![image](https://github.com/user-attachments/assets/de1572b9-5973-4602-b9d0-4334e0611f92)
 ---


 ## License
This project is licensed under the MIT License.

