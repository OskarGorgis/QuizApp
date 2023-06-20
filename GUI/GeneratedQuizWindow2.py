# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quiz_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(600, 80, 281, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.start_quiz = QPushButton(self.verticalLayoutWidget)
        self.start_quiz.setObjectName(u"start_quiz")

        self.verticalLayout.addWidget(self.start_quiz)

        self.add_question = QPushButton(self.verticalLayoutWidget)
        self.add_question.setObjectName(u"add_question")

        self.verticalLayout.addWidget(self.add_question)

        self.question_add = QTextEdit(self.verticalLayoutWidget)
        self.question_add.setObjectName(u"question_add")

        self.verticalLayout.addWidget(self.question_add)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.answer_a_add = QLineEdit(self.verticalLayoutWidget)
        self.answer_a_add.setObjectName(u"answer_a_add")

        self.gridLayout_2.addWidget(self.answer_a_add, 0, 0, 1, 1)

        self.answer_d_add = QLineEdit(self.verticalLayoutWidget)
        self.answer_d_add.setObjectName(u"answer_d_add")

        self.gridLayout_2.addWidget(self.answer_d_add, 1, 1, 1, 1)

        self.answer_b_add = QLineEdit(self.verticalLayoutWidget)
        self.answer_b_add.setObjectName(u"answer_b_add")

        self.gridLayout_2.addWidget(self.answer_b_add, 0, 1, 1, 1)

        self.answer_c_add = QLineEdit(self.verticalLayoutWidget)
        self.answer_c_add.setObjectName(u"answer_c_add")

        self.gridLayout_2.addWidget(self.answer_c_add, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.confirm_add = QPushButton(self.verticalLayoutWidget)
        self.confirm_add.setObjectName(u"confirm_add")

        self.verticalLayout.addWidget(self.confirm_add)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(60, 10, 721, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.current_score = QLabel(self.horizontalLayoutWidget_2)
        self.current_score.setObjectName(u"current_score")
        self.current_score.setFrameShape(QFrame.Panel)
        self.current_score.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.current_score)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.current_lives = QLabel(self.horizontalLayoutWidget_2)
        self.current_lives.setObjectName(u"current_lives")

        self.horizontalLayout.addWidget(self.current_lives)

        self.live_counter = QLCDNumber(self.horizontalLayoutWidget_2)
        self.live_counter.setObjectName(u"live_counter")

        self.horizontalLayout.addWidget(self.live_counter)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.high_score = QLabel(self.horizontalLayoutWidget_2)
        self.high_score.setObjectName(u"high_score")
        self.high_score.setFrameShape(QFrame.Panel)
        self.high_score.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.high_score)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 70, 541, 471))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main_question = QLabel(self.verticalLayoutWidget_3)
        self.main_question.setWordWrap(True)
        self.main_question.setObjectName(u"main_question")
        self.main_question.setFrameShape(QFrame.WinPanel)
        self.main_question.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.main_question)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.answer_c = QCheckBox(self.verticalLayoutWidget_3)
        self.answer_c.setObjectName(u"answer_c")

        self.gridLayout.addWidget(self.answer_c, 1, 0, 1, 1)

        self.answer_d = QCheckBox(self.verticalLayoutWidget_3)
        self.answer_d.setObjectName(u"answer_d")

        self.gridLayout.addWidget(self.answer_d, 1, 1, 1, 1)

        self.answer_b = QCheckBox(self.verticalLayoutWidget_3)
        self.answer_b.setObjectName(u"answer_b")

        self.gridLayout.addWidget(self.answer_b, 0, 1, 1, 1)

        self.answer_a = QCheckBox(self.verticalLayoutWidget_3)
        self.answer_a.setObjectName(u"answer_a")

        self.gridLayout.addWidget(self.answer_a, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.next = QPushButton(self.verticalLayoutWidget_3)
        self.next.setObjectName(u"next")

        self.horizontalLayout_4.addWidget(self.next)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 560, 841, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.exit = QPushButton(self.horizontalLayoutWidget_3)
        self.exit.setObjectName(u"exit")

        self.horizontalLayout_3.addWidget(self.exit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.clear_screen = QPushButton(self.horizontalLayoutWidget_3)
        self.clear_screen.setObjectName(u"clear_screen")

        self.horizontalLayout_3.addWidget(self.clear_screen)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_quiz.setText(QCoreApplication.translate("MainWindow", u"Start Quiz", None))
        self.add_question.setText(QCoreApplication.translate("MainWindow", u"Add question", None))
        self.confirm_add.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.current_score.setText(QCoreApplication.translate("MainWindow", u"Current score: 100", None))
        self.current_lives.setText(QCoreApplication.translate("MainWindow", u"Current lives ", None))
        self.high_score.setText(QCoreApplication.translate("MainWindow", u"High score: 100", None))
        self.main_question.setText(QCoreApplication.translate("MainWindow", u"Question", None))
        self.answer_c.setText(QCoreApplication.translate("MainWindow", u"Answer C", None))
        self.answer_d.setText(QCoreApplication.translate("MainWindow", u"Answer D", None))
        self.answer_b.setText(QCoreApplication.translate("MainWindow", u"Answer B", None))
        self.answer_a.setText(QCoreApplication.translate("MainWindow", u"Answer A", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"Exit quiz", None))
        self.clear_screen.setText(QCoreApplication.translate("MainWindow", u"Clear screen", None))
    # retranslateUi

