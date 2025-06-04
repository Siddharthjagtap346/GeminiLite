from flask import Flask, render_template, request, jsonify
import re
from vector_engine import VectorSearchEngine

# For translation
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

with open("data/corpus.txt", "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f if line.strip()]

engine = VectorSearchEngine(docs)

def highlight_text(doc, query):
    if not query:
        return doc
    # Escape and split query into terms
    terms = re.escape(query).split()
    pattern = re.compile(r'(' + '|'.join(terms) + r')', re.IGNORECASE)
    return pattern.sub(r'<mark>\1</mark>', doc)

def relevance_blocks(score):
    blocks = int(score * 10)
    return "▰" * blocks + "▱" * (10 - blocks)

def relevance_color(score):
    if score >= 0.75:
        return "text-green-600"
    elif score >= 0.5:
        return "text-lime-500"
    elif score >= 0.3:
        return "text-yellow-500"
    else:
        return "text-red-500"

# Translation models cache
_translation_models = {}

def get_translation_model(src_lang):
    if src_lang not in _translation_models:
        model_name_map = {
            "hi": "Helsinki-NLP/opus-mt-hi-en",
            "ja": "Helsinki-NLP/opus-mt-ja-en",
        }
        if src_lang in model_name_map:
            model_name = model_name_map[src_lang]
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)
            _translation_models[src_lang] = (tokenizer, model)
        else:
            _translation_models[src_lang] = None
    return _translation_models[src_lang]

def detect_language(query):
    # Basic Unicode block detection for Hindi and Japanese
    if any('\u0900' <= ch <= '\u097F' for ch in query):  # Hindi range
        return "hi"
    elif any('\u3040' <= ch <= '\u30FF' for ch in query):  # Japanese Hiragana/Katakana/Kanji
        return "ja"
    return "en"

def translate_to_english(query):
    lang = detect_language(query)
    if lang == "en":
        return query
    model_data = get_translation_model(lang)
    if model_data is None:
        return query  # Unsupported language fallback
    tokenizer, model = model_data
    batch = tokenizer.prepare_seq2seq_batch([query], return_tensors="pt", padding=True)
    translated = model.generate(**batch)
    english_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return english_text

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query", "").strip()
        translated_query = translate_to_english(query)
        raw_results = engine.search(translated_query)
        results = []
        for doc, score in raw_results:
            # Highlight original query terms in doc for UX consistency
            highlights = highlight_text(doc, query)
            bar = relevance_blocks(score)
            color = relevance_color(score)
            results.append((doc, score, highlights, bar, color))
    return render_template("index.html", results=results, query=query)

@app.route("/api/search", methods=["GET"])
def api_search():
    query = request.args.get("q", "").strip()
    translated_query = translate_to_english(query)
    raw_results = engine.search(translated_query)
    results = []
    for doc, score in raw_results:
        highlights = highlight_text(doc, query)
        bar = relevance_blocks(score)
        color = relevance_color(score)
        results.append({"doc": doc, "score": score, "highlight": highlights, "bar": bar, "color": color})
    return jsonify(results)

@app.route("/docs")
def docs():
    api_docs = {
        "openapi": "3.0.0",
        "info": {
            "title": "GeminiLite Semantic Search API",
            "version": "1.0"
        },
        "paths": {
            "/api/search": {
                "get": {
                    "summary": "Semantic search endpoint",
                    "parameters": [
                        {
                            "name": "q",
                            "in": "query",
                            "required": True,
                            "description": "Search query",
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Search results",
                            "content": {
                                "application/json": {
                                    "example": [
                                        {"doc": "OpenAI develops ChatGPT.", "score": 0.68, "highlight": "OpenAI develops <mark>ChatGPT</mark>."}
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return jsonify(api_docs)

if __name__ == "__main__":
    app.run(debug=True)
