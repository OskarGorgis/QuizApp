from GUI_functionalities.MainWindowClass import QuizMainWindow
from PySide6 import QtWidgets
import sys


def load_window():
    app = QtWidgets.QApplication([])
    main_window = QuizMainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    load_window()
