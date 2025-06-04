import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class VectorSearchEngine:
    def __init__(self, docs):
        self.docs = docs
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(docs)
        self.feature_names = np.array(self.vectorizer.get_feature_names_out())

    def search(self, query, top_k=5, top_keywords=3):
        query_vec = self.vectorizer.transform([query])
        cosine_similarities = (self.tfidf_matrix * query_vec.T).toarray().flatten()

        top_doc_indices = cosine_similarities.argsort()[::-1][:top_k]
        results = []

        for idx in top_doc_indices:
            doc = self.docs[idx]
            score = cosine_similarities[idx]
            doc_vec = self.tfidf_matrix[idx].toarray().flatten()
            top_kw_indices = doc_vec.argsort()[::-1][:top_keywords]
            top_kw = self.feature_names[top_kw_indices]
            results.append((doc, score))  # ✅ Only returning (doc, score)
        return results
