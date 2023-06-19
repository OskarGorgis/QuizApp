from PySide6 import QtWidgets
from GUI import GeneratedQuizWindow2
from Quiz_functionalities.QuestionsBase import QuestionBase
from GUI_functionalities.FileManagingFunctions import read_highest_score
import random


class QuizMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuizMainWindow, self).__init__()

        self.lives = 0
        self.points = 0
        self.correct_answer_place = 0

        # Inicjalizacja obiektu UI z pliku Pythona
        self.ui = GeneratedQuizWindow2.Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_high_scores()

        # Disable adding question part
        self.ui.question_add.setDisabled(True)
        self.ui.answer_a_add.setDisabled(True)
        self.ui.answer_b_add.setDisabled(True)
        self.ui.answer_c_add.setDisabled(True)
        self.ui.answer_d_add.setDisabled(True)
        self.ui.confirm_add.setDisabled(True)
        self.ui.next.setDisabled(True)

        self.ui.clear_screen.clicked.connect(self.set_default)
        self.ui.clear_screen.clicked.connect(self.load_high_scores)
        self.ui.start_quiz.clicked.connect(self.start_quiz)
        self.ui.next.clicked.connect(self.next_question)

        # Wczytanie pytań do bazy
        self.question_base = QuestionBase()

    def set_default(self):
        self.ui.current_score.setText(f"Current score: {self.points}")
        self.ui.live_counter.display(self.lives)
        self.ui.main_question.setText("Press Start Quiz")
        self.ui.answer_a.setText("A")
        self.ui.answer_b.setText("B")
        self.ui.answer_c.setText("C")
        self.ui.answer_d.setText("D")

    def load_high_scores(self):
        hs_text = "High score: "
        hs_text += read_highest_score()
        self.ui.high_score.setText(hs_text)

    def shuffle_answers(self, correct_answer, incorrect_answers):
        ca_place = random.randint(1, 4)
        answers = incorrect_answers
        if ca_place == 4:
            answers.append(correct_answer)
        else:
            answer = answers[ca_place-1]
            answers[ca_place-1] = correct_answer
            answers.append(answer)
        return answers, ca_place

    def display_question(self):
        question = self.question_base.get_question()
        self.ui.main_question.setText(question["question"])
        answers, correct_answer_place = self.shuffle_answers(question["correct_answer"], question["incorrect_answers"])
        self.ui.answer_a.setText(answers[0])
        self.ui.answer_b.setText(answers[1])
        self.ui.answer_c.setText(answers[2])
        self.ui.answer_d.setText(answers[3])
        self.correct_answer_place = correct_answer_place

    def check_answer(self, correct_answer):
        match correct_answer:
            case 1:
                return self.ui.answer_a.isChecked() and not self.ui.answer_b.isChecked() and \
                    not self.ui.answer_c.isChecked() and not self.ui.answer_d.isChecked()
            case 2:
                return not self.ui.answer_a.isChecked() and self.ui.answer_b.isChecked() and \
                    not self.ui.answer_c.isChecked() and not self.ui.answer_d.isChecked()
            case 3:
                return not self.ui.answer_a.isChecked() and not self.ui.answer_b.isChecked() and \
                    self.ui.answer_c.isChecked() and not self.ui.answer_d.isChecked()
            case 4:
                return not self.ui.answer_a.isChecked() and not self.ui.answer_b.isChecked() and \
                    not self.ui.answer_c.isChecked() and self.ui.answer_d.isChecked()

    def start_quiz(self):
        self.lives = 3
        self.points = 0
        self.ui.current_score.setText(f"Current score: {self.points}")
        self.ui.next.setDisabled(False)
        self.ui.live_counter.display(self.lives)
        self.display_question()

    def end_quiz(self):
        self.set_default()
        self.ui.main_question.setText(f"You lost!\nYour score: {self.points}"
                                      f"\nEnter your name on the left and click Confirm")
        self.ui.next.setDisabled(True)
        self.enter_name()

    def enter_name(self):
        self.ui.question_add.setDisabled(False)
        self.ui.confirm_add.setDisabled(False)

    def next_question(self):
        if not self.check_answer(self.correct_answer_place):
            self.lives -= 1
            self.ui.live_counter.display(self.lives)
            if self.lives == 0:
                self.end_quiz()
            else:
                self.display_question()
        else:
            self.points += 100
            self.ui.current_score.setText(f"Current score: {self.points}")
            self.ui.live_counter.display(self.lives)
            self.display_question()





