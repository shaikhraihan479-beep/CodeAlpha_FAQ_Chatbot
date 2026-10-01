\# 🤖 AI FAQ Chatbot



An AI-powered FAQ chatbot developed using Python and Natural Language Processing (NLP).



The chatbot understands different ways of asking a question and finds the most relevant answer from a predefined FAQ dataset using TF-IDF and Cosine Similarity.



\---



\## 📌 Project Overview



This project was developed as part of the CodeAlpha Artificial Intelligence Internship.



The chatbot is designed to answer frequently asked questions related to:



\- Artificial Intelligence

\- Machine Learning

\- Natural Language Processing

\- Computer Vision

\- Object Detection

\- Object Tracking

\- YOLO

\- AI Music Generation

\- MIDI

\- LSTM

\- TF-IDF

\- Cosine Similarity

\- Chatbots



The application provides a professional web-based chat interface using Streamlit.



\---



\## 🎯 Objective



The main objective of this project is to build an FAQ chatbot that can:



\- Accept questions from the user

\- Process natural language input

\- Compare the question with stored FAQ questions

\- Find the most relevant question

\- Return the corresponding answer

\- Handle questions written in different ways

\- Provide a fallback response when no relevant answer is found



\---



\## 🧠 How the Chatbot Works



The chatbot follows these main steps:



1\. The user enters a question through the Streamlit interface.

2\. The question is cleaned using NLP preprocessing.

3\. Stopwords and unnecessary characters are removed.

4\. The cleaned question is converted into a TF-IDF vector.

5\. The vector is compared with all stored FAQ questions.

6\. Cosine Similarity is used to measure similarity.

7\. The FAQ with the highest similarity score is selected.

8\. If the similarity score is above the required threshold, the corresponding answer is returned.

9\. Otherwise, the chatbot displays a fallback message.



\### Simple Flow



User Question  

↓  

Text Preprocessing  

↓  

TF-IDF Vectorization  

↓  

Cosine Similarity  

↓  

Best FAQ Match  

↓  

Answer



\---



\## 🛠️ Technologies Used



\### Programming Language

\- Python



\### Natural Language Processing

\- NLTK

\- Stopword Removal

\- Text Preprocessing



\### Machine Learning / Text Matching

\- Scikit-learn

\- TF-IDF Vectorization

\- Cosine Similarity



\### User Interface

\- Streamlit

\- HTML

\- CSS



\### Data Format

\- JSON



\---



\## 📂 Project Structure



&#x20;   CodeAlpha\_FAQ\_Chatbot/

&#x20;   │

&#x20;   ├── data/

&#x20;   │   └── faqs.json

&#x20;   │

&#x20;   ├── output/

&#x20;   │   ├── chatbot\_demo.png

&#x20;   │   └── screenshots/

&#x20;   │

&#x20;   ├── src/

&#x20;   │   ├── app.py

&#x20;   │   └── chatbot.py

&#x20;   │

&#x20;   ├── venv/

&#x20;   │

&#x20;   ├── .gitignore

&#x20;   ├── README.md

&#x20;   └── requirements.txt



\---



\## 📄 Main Files



\### `src/app.py`



This file creates the Streamlit web interface.



It handles:



\- Chat interface

\- User input

\- Chat history

\- Application design

\- Displaying chatbot responses



\### `src/chatbot.py`



This file contains the main chatbot logic.



It handles:



\- Loading the FAQ dataset

\- Text preprocessing

\- TF-IDF vectorization

\- Cosine similarity

\- Finding the best FAQ match

\- Returning the appropriate answer



\### `data/faqs.json`



This file contains the predefined FAQ questions and answers used by the chatbot.



\### `requirements.txt`



Contains the Python libraries required to run the project.



\---



\## 🔧 Installation



\### 1. Clone the repository



Clone this project from GitHub to your computer.



\### 2. Create a virtual environment



&#x20;   python -m venv venv



\### 3. Activate the virtual environment



Windows:



&#x20;   venv\\Scripts\\activate



\### 4. Install required libraries



&#x20;   pip install -r requirements.txt



\### 5. Run the chatbot



From the project folder, run:



&#x20;   streamlit run src/app.py



The application will open in your browser.



\---



\## 💬 Example Questions



You can ask questions such as:



\- What is artificial intelligence?

\- What is machine learning?

\- What is NLP?

\- What is YOLO?

\- What is object detection?

\- How does object tracking work?

\- How can AI generate music?

\- What is MIDI?

\- What is TF-IDF?

\- What is cosine similarity?



The chatbot can also recognize different wording for similar questions.



For example:



"What is YOLO?"



and



"How does YOLO detect objects?"



can be matched with the same FAQ topic.



\---



\## 🔍 NLP and Similarity Matching



\### Text Preprocessing



The chatbot first prepares the text by:



\- Converting text to lowercase

\- Removing unnecessary characters

\- Splitting text into words

\- Removing common English stopwords



\### TF-IDF



TF-IDF converts text into numerical values based on the importance of words in the FAQ dataset.



\### Cosine Similarity



Cosine Similarity compares the user's question with the stored FAQ questions.



A higher similarity score means the questions are more similar.



The chatbot uses a similarity threshold to avoid returning unrelated answers.



\---



\## 🖥️ User Interface



The chatbot uses Streamlit to provide a web-based interface.



The interface includes:



\- Professional dark-themed design

\- Chat input

\- User messages

\- AI assistant responses

\- FAQ topic suggestions

\- Chat history



\---



\## 🧪 Testing



The chatbot was tested using different questions related to the supported FAQ topics.



Example test questions include:



\- What is YOLO?

\- Can AI find objects in videos?

\- How can AI create songs?

\- What is TF-IDF?



The chatbot also provides a fallback response when the similarity score is below the required threshold.



\---



\## ⚠️ Limitations



This chatbot is an FAQ-based NLP system.



It does not generate completely new answers like a Large Language Model (LLM).



Its answers depend on the information available in the FAQ dataset.



Questions outside the supported topics may result in the fallback response.



\---



\## 🚀 Future Improvements



Possible future improvements include:



\- Adding more FAQ categories

\- Adding more example questions

\- Improving similarity matching

\- Adding voice input

\- Adding multilingual support

\- Connecting the chatbot to a larger knowledge base

\- Adding an LLM-based response system



\---



\## 👨‍💻 Project Information



\*\*Project:\*\* AI FAQ Chatbot  

\*\*Internship:\*\* CodeAlpha Artificial Intelligence Internship  

\*\*Domain:\*\* Artificial Intelligence / Natural Language Processing  

\*\*Language:\*\* Python



\---



\## 📌 Conclusion



This project demonstrates how Natural Language Processing and text similarity techniques can be used to create a practical FAQ chatbot.



The system combines text preprocessing, TF-IDF vectorization, Cosine Similarity, and a Streamlit interface to provide an interactive question-answering application.

