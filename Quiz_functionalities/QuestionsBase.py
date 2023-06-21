import html, random
from Quiz_functionalities.CooperatingWithDatabase import get_questions
from GUI_functionalities.FileManagingFunctions import get_question_from_file


class QuestionBase:
    questions = []
    difficulty_level = "easy"

    def __init__(self):
        self.load_questions_to_database()

    def load_questions_to_database(self):
        self.load_question_from_database(10, self.difficulty_level)
        if random.randint(0, 1) == 1:
            question = get_question_from_file()
            if question != -1:
                self.questions[random.randint(0, 9)] = question

    def decode_questions(self):
        for question in self.questions:
            question["correct_answer"] = html.unescape(question["correct_answer"])
            question["incorrect_answers"] = [html.unescape(answer) for answer in question["incorrect_answers"]]
            question["question"] = html.unescape(question["question"])

    def load_question_from_database(self, number_of_questions, difficulty_level):
        try:
            self.questions = get_questions(number_of_questions, difficulty_level)
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

    def increase_difficulty(self):
        if self.difficulty_level == "easy":
            self.difficulty_level = "medium"
            self.load_questions_to_database()
        elif self.difficulty_level == "medium":
            self.difficulty_level = "hard"
            self.load_questions_to_database()

