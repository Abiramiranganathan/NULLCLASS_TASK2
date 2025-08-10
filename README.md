# NULLCLASS_TASK2
DATA SCIENCE
Description:
Task 2 involved building a Medical Q&A Chatbot using the MedQuAD dataset, which contains trusted medical question-answer pairs from sources like NIH and NLM. The dataset was first extracted from XML files, cleaned, and stored as a CSV. Using TF-IDF vectorization and cosine similarity, the chatbot retrieves the most relevant answer to a user’s medical query. A simple medical entity recognition feature detects keywords like diseases, symptoms, and treatments. The chatbot was implemented with Streamlit, providing a user-friendly web interface where users can type medical questions and instantly receive accurate responses.
MedQuAD Dataset Link: https://github.com/abachaa/MedQuAD

How to Run the Medical Q&A Chatbot:
Download the app.py file and place it in the same directory where the MedQuAD dataset is stored.

Open Command Prompt:
Press Windows + R, type cmd, and press Enter.

Navigate to the Project Directory:
Copy the path of your dataset folder.

In the command prompt, type:
bash
cd "C:\Users\abira\OneDrive\Downloads\MedQuAD-master\MedQuAD-master"
Run the Streamlit Application:

bash
streamlit run app.py

Access the Chatbot:
After running the above command, Streamlit will display a local URL (e.g., http://localhost:8501).
Open this URL in your browser to start using the chatbot.
