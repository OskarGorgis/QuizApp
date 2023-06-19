from PySide6 import QtWidgets
from GUI import GeneratedQuizWindow2

class QuizMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuizMainWindow, self).__init__()

        # Inicjalizacja obiektu UI z pliku Pythona
        self.ui = GeneratedQuizWindow2.Ui_MainWindow()
        self.ui.setupUi(self)
