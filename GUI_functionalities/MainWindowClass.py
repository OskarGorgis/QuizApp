from PySide6 import QtWidgets
from GUI import GeneratedQuizWindow
from Quiz_functionalities.QuestionsBase import QuestionBase
from GUI_functionalities.FileManagingFunctions import read_highest_score, save_score_in_file, save_question_to_file
import random, sys


class QuizMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuizMainWindow, self).__init__()

        self.lives = 0
        self.points = 0
        self.correct_answer_place = 0
        self.adding_question = False

        # Inicjalizacja obiektu UI z pliku Pythona
        self.ui = GeneratedQuizWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.clear_screen.clicked.connect(self.set_default)
        self.ui.clear_screen.clicked.connect(self.set_default)
        self.ui.start_quiz.clicked.connect(self.start_quiz)
        self.ui.next.clicked.connect(self.next_question)
        self.ui.confirm_add.clicked.connect(self.confirm_name)
        self.ui.confirm_add.clicked.connect(self.confirm_question)
        self.ui.exit.clicked.connect(self.starting_set)
        self.ui.add_question.clicked.connect(self.add_question)
        self.ui.answer_a.clicked.connect(self.on_checkBox_A_stateChanged)
        self.ui.answer_b.clicked.connect(self.on_checkBox_B_stateChanged)
        self.ui.answer_c.clicked.connect(self.on_checkBox_C_stateChanged)
        self.ui.answer_d.clicked.connect(self.on_checkBox_D_stateChanged)

        # Wczytanie pytań do bazy
        self.question_base = QuestionBase()

        self.starting_set()

    def set_default(self):
        self.ui.current_score.setText(f"Current score: {self.points}")
        self.ui.live_counter.display(self.lives)
        self.ui.main_question.setText("Press Start Quiz")
        self.ui.answer_a.setText("A")
        self.ui.answer_b.setText("B")
        self.ui.answer_c.setText("C")
        self.ui.answer_d.setText("D")
        self.load_high_scores()

    def load_high_scores(self):
        hs_text = "High score: "
        hs_text += read_highest_score()
        self.ui.high_score.setText(hs_text)

    @staticmethod
    def shuffle_answers(correct_answer, incorrect_answers):
        ca_place = random.randint(1, 4)
        answers = incorrect_answers
        print(ca_place)
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
        self.ui.answer_a.setChecked(False)
        self.ui.answer_b.setText(answers[1])
        self.ui.answer_b.setChecked(False)
        self.ui.answer_c.setText(answers[2])
        self.ui.answer_c.setChecked(False)
        self.ui.answer_d.setText(answers[3])
        self.ui.answer_d.setChecked(False)
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
        self.ui.clear_screen.setDisabled(True)
        self.ui.exit.setDisabled(False)
        self.lives = 3
        self.points = 0
        self.ui.answer_a.setDisabled(False)
        self.ui.answer_b.setDisabled(False)
        self.ui.answer_c.setDisabled(False)
        self.ui.answer_d.setDisabled(False)
        self.ui.add_question.setDisabled(True)
        self.ui.current_score.setText(f"Current score: {self.points}")
        self.ui.next.setDisabled(False)
        self.ui.live_counter.display(self.lives)
        self.display_question()

    def end_quiz(self):
        points = self.points
        self.ui.main_question.setText(f"You lost!\nYour score: {points}"
                                      f"\nEnter your name on the right and click Confirm"
                                      f"\n(Only first 10 letters of first line will count)")
        self.ui.next.setDisabled(True)
        self.ui.question_add.setDisabled(False)
        self.ui.confirm_add.setDisabled(False)

    def confirm_name(self):
        if not self.adding_question:
            text_tab = self.ui.question_add.toPlainText().splitlines()
            self.ui.question_add.setDisabled(True)
            self.ui.question_add.clear()
            self.ui.confirm_add.setDisabled(True)
            self.ui.clear_screen.setDisabled(False)
            self.ui.exit.setDisabled(True)
            if len(text_tab) != 0:
                if not text_tab[0].isspace():
                    text = text_tab[0][:10]
                    text = str(self.points) + " " + text
                    save_score_in_file(text)
                else:
                    self.ui.main_question.setText("No entry in the first line of text\nThe result was not saved")
            else:
                self.ui.main_question.setText("The specified field has not been filled\nThe result was not saved")
            self.starting_set()

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
            if self.points == 1000 or 2000:
                self.question_base.increase_difficulty()
            self.ui.current_score.setText(f"Current score: {self.points}")
            self.ui.live_counter.display(self.lives)
            self.display_question()

    def starting_set(self):
        # variables
        self.lives = 0
        self.points = 0
        self.correct_answer_place = 0
        self.adding_question = False
        # widgets
        self.ui.question_add.setDisabled(True)
        self.ui.answer_a_add.setDisabled(True)
        self.ui.answer_b_add.setDisabled(True)
        self.ui.answer_c_add.setDisabled(True)
        self.ui.answer_d_add.setDisabled(True)
        self.ui.answer_a.setChecked(False)
        self.ui.answer_b.setChecked(False)
        self.ui.answer_c.setChecked(False)
        self.ui.answer_d.setChecked(False)
        self.ui.confirm_add.setDisabled(True)
        self.ui.next.setDisabled(True)
        self.ui.answer_a.setDisabled(True)
        self.ui.answer_b.setDisabled(True)
        self.ui.answer_c.setDisabled(True)
        self.ui.answer_d.setDisabled(True)
        self.ui.exit.setDisabled(True)
        self.ui.add_question.setDisabled(False)
        self.ui.start_quiz.setDisabled(False)
        self.set_default()

    def add_question(self):
        self.ui.start_quiz.setDisabled(True)
        self.ui.question_add.setDisabled(False)
        self.ui.answer_a_add.setDisabled(False)
        self.ui.answer_b_add.setDisabled(False)
        self.ui.answer_c_add.setDisabled(False)
        self.ui.answer_d_add.setDisabled(False)
        self.ui.confirm_add.setDisabled(False)

        self.ui.answer_a.setDisabled(True)
        self.ui.answer_b.setDisabled(True)
        self.ui.answer_c.setDisabled(True)
        self.ui.answer_d.setDisabled(True)

        self.adding_question = True
        self.ui.main_question.setText("Enter the content of the question into the large rectangle, and the content of"
                                      " the answer into the rectangles below\nPut the correct answer in the upper "
                                      "left rectangle on the answer, then click confirm")

    def confirm_question(self):
        if self.adding_question:
            question = self.ui.question_add.toPlainText()
            correct_answer = self.ui.answer_a_add.text()
            incorrect_answers = [self.ui.answer_b_add.text(), self.ui.answer_c_add.text(),
                                self.ui.answer_d_add.text()]

            self.ui.question_add.setDisabled(True)
            self.ui.question_add.clear()
            self.ui.answer_a_add.setDisabled(True)
            self.ui.answer_a_add.clear()
            self.ui.answer_b_add.setDisabled(True)
            self.ui.answer_b_add.clear()
            self.ui.answer_c_add.setDisabled(True)
            self.ui.answer_c_add.clear()
            self.ui.answer_d_add.setDisabled(True)
            self.ui.answer_d_add.clear()

            if len(question) == 0 or len(correct_answer) == 0 or len(incorrect_answers[0]) == 0 \
                    or len(incorrect_answers[1]) == 0 or len(incorrect_answers[2]) == 0:
                self.ui.main_question.setText(
                    "At least one of the fields is empty!\n"
                    "Question not added. Try again by completing all fields correctly!")
                self.ui.start_quiz.setDisabled(False)
            else:
                save_question_to_file(question, correct_answer, incorrect_answers)

            self.ui.confirm_add.setDisabled(True)
            self.starting_set()

    def on_checkBox_A_stateChanged(self):
        self.ui.answer_b.setChecked(False)
        self.ui.answer_c.setChecked(False)
        self.ui.answer_d.setChecked(False)

    def on_checkBox_B_stateChanged(self):
        self.ui.answer_a.setChecked(False)
        self.ui.answer_c.setChecked(False)
        self.ui.answer_d.setChecked(False)

    def on_checkBox_C_stateChanged(self):
        self.ui.answer_a.setChecked(False)
        self.ui.answer_b.setChecked(False)
        self.ui.answer_d.setChecked(False)

    def on_checkBox_D_stateChanged(self):
        self.ui.answer_a.setChecked(False)
        self.ui.answer_b.setChecked(False)
        self.ui.answer_c.setChecked(False)


def run_app():
    app = QtWidgets.QApplication([])
    main_window = QuizMainWindow()
    main_window.show()
    sys.exit(app.exec())

