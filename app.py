# app.py
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load cleaned dataset
# -----------------------------
df = pd.read_csv(
    r"C:\Users\abira\OneDrive\downloads\MedQuAD-master\MedQuAD-master\All_MedQuAD_QA_Cleaned.csv"
)

# Extract questions and answers
questions = df["Question"].values
answers = df["Answer"].values

# -----------------------------
# Fit TF-IDF vectorizer
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = vectorizer.fit_transform(questions)

# -----------------------------
# Simple list of medical keywords for basic entity recognition
# -----------------------------
medical_keywords = [
    "asthma", "cancer", "diabetes", "infection", "fever", "headache", "surgery", "tumor",
    "symptom", "treatment", "medication", "disease", "nausea", "pain", "blood pressure"
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🩺 Medical Q&A Chatbot")
st.write("Ask any medical question and get reliable answers from the MedQuAD dataset.")

user_input = st.text_input("Enter your medical question:")

if user_input:
    # Entity recognition (basic)
    detected_entities = [word for word in medical_keywords if word in user_input.lower()]

    # Similarity-based retrieval
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, question_vectors).flatten()
    best_match_index = similarities.argmax()

    # Display best match
    st.subheader("🔍 Best Match:")
    st.markdown(f"**Q:** {questions[best_match_index]}")
    st.markdown(f"**A:** {answers[best_match_index]}")

    # Show detected medical entities
    if detected_entities:
        st.subheader("🧠 Detected Medical Entities:")
        st.write(", ".join(detected_entities))
