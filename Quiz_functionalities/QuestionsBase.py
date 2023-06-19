from Quiz_functionalities.CooperatingWithDatabase import get_questions
from GUI_functionalities.FileManagingFunctions import get_question_from_file
import random


class QuestionBase:
    questions = []

    def __init__(self):
        self.load_question_from_database()

    def load_question_from_database(self):
        try:
            self.questions = get_questions(10)
        except ImportError:
            print("Import Error")

    def load_question_from_file(self):
        question = get_question_from_file()
        if question != -1:
            self.questions.append(question)

    def get_question(self):
        question = self.questions[0]
        del self.questions[0]
        if len(self.questions) < 1:
            self.load_question_from_database()
        return question
