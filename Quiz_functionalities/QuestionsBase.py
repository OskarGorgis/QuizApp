import html
import random
from Quiz_functionalities.CooperatingWithDatabase import get_questions
from GUI_functionalities.FileManagingFunctions import get_question_from_file


class QuestionBase:
    questions = []

    def __init__(self):
        self.load_questions_to_database()

    def load_questions_to_database(self):
        self.load_question_from_database(10)
        if random.randint(0, 1) == 1:
            question = get_question_from_file()
            if question != -1:

                self.questions[random.randint(0, 9)] = question

    def decode_questions(self):
        for question in self.questions:
            question["correct_answer"] = html.unescape(question["correct_answer"])
            question["incorrect_answers"] = [html.unescape(answer) for answer in question["incorrect_answers"]]
            question["question"] = html.unescape(question["question"])

    def load_question_from_database(self, number_of_questions):
        try:
            self.questions = get_questions(number_of_questions)
            self.decode_questions()
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
            self.load_questions_to_database()
        return question
