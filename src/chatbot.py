import json
import re
from pathlib import Path

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Download required NLTK data
nltk.download("stopwords", quiet=True)


class FAQChatbot:

    def __init__(self, faq_file):

        # Load FAQ data
        with open(faq_file, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        # English stopwords
        self.stop_words = set(stopwords.words("english"))

        # Store every example question
        self.questions = []
        self.answer_indexes = []

        for index, faq in enumerate(self.faqs):

            for question in faq["questions"]:

                self.questions.append(
                    self.preprocess(question)
                )

                self.answer_indexes.append(index)

        # Create TF-IDF model
        self.vectorizer = TfidfVectorizer()

        # Convert FAQ questions into vectors
        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def preprocess(self, text):
        """
        Clean and prepare text for NLP processing.
        """

        text = text.lower()

        # Keep letters, numbers and spaces
        text = re.sub(r"[^a-z0-9\s]", " ", text)

        words = text.split()

        # Remove common stopwords
        words = [
            word
            for word in words
            if word not in self.stop_words
        ]

        return " ".join(words)

    def get_response(self, user_question):
        """
        Find the most similar FAQ and return its answer.
        """

        cleaned_question = self.preprocess(
            user_question
        )

        user_vector = self.vectorizer.transform(
            [cleaned_question]
        )

        similarity_scores = cosine_similarity(
            user_vector,
            self.question_vectors
        )[0]

        # Find highest similarity
        best_match_index = similarity_scores.argmax()

        best_score = similarity_scores[
            best_match_index
        ]

        # Find which FAQ the matched question belongs to
        faq_index = self.answer_indexes[
            best_match_index
        ]

        # Minimum similarity required
        threshold = 0.30

        if best_score >= threshold:

            answer = self.faqs[
                faq_index
            ]["answer"]

            return answer, best_score

        return (
            "Sorry, I couldn't find a relevant answer. "
            "Please try asking about AI, NLP, object detection, "
            "object tracking, or AI music generation.",
            best_score
        )


# Test the chatbot
if __name__ == "__main__":

    project_folder = Path(
        __file__
    ).resolve().parent.parent

    faq_file = project_folder / "data" / "faqs.json"

    chatbot = FAQChatbot(faq_file)

    print("FAQ Chatbot test")
    print("----------------")

    test_questions = [
        "What is YOLO?",
        "Can AI find objects in videos?",
        "How can AI create songs?",
        "What is TF IDF?"
    ]

    for question in test_questions:

        answer, score = chatbot.get_response(
            question
        )

        print("\nQuestion:", question)
        print("Answer:", answer)
        print(
            "Similarity:",
            round(score, 2)
        )