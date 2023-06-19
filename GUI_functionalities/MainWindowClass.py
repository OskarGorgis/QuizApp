from PySide6 import QtWidgets
from GUI import GeneratedQuizWindow2

class QuizMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuizMainWindow, self).__init__()

        # Inicjalizacja obiektu UI z pliku Pythona
        self.ui = GeneratedQuizWindow2.Ui_MainWindow()
        self.ui.setupUi(self)

        #disable adding question part
        self.ui.question_add.setDisabled(True)
        self.ui.answer_a_add.setDisabled(True)
        self.ui.answer_b_add.setDisabled(True)
        self.ui.answer_c_add.setDisabled(True)
        self.ui.answer_d_add.setDisabled(True)
        self.ui.confirm_add.setDisabled(True)



