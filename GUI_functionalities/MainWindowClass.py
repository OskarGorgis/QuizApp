from PySide6 import QtWidgets
from GUI import GeneratedQuizWindow2
from GUI_functionalities.File_managing_functions import read_highest_score
import os

class QuizMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuizMainWindow, self).__init__()

        # Inicjalizacja obiektu UI z pliku Pythona
        self.ui = GeneratedQuizWindow2.Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_high_scores()

        #disable adding question part
        self.ui.question_add.setDisabled(True)
        self.ui.answer_a_add.setDisabled(True)
        self.ui.answer_b_add.setDisabled(True)
        self.ui.answer_c_add.setDisabled(True)
        self.ui.answer_d_add.setDisabled(True)
        self.ui.confirm_add.setDisabled(True)

        self.ui.clear_screen.clicked.connect(self.set_default)
        self.ui.clear_screen.clicked.connect(self.load_high_scores)

    def set_default(self):
        self.ui.current_score.setText("Current score: 0")
        self.ui.live_counter.display(0)
        self.ui.main_question.setText("")
        self.ui.answer_a.setText("A")
        self.ui.answer_b.setText("B")
        self.ui.answer_c.setText("C")
        self.ui.answer_d.setText("D")

    def load_high_scores(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Data_files", "high_scores"))
        hs_text = "High score: "
        hs_text += read_highest_score(file_path)
        self.ui.high_score.setText(hs_text)




