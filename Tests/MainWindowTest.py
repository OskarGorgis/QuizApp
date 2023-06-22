import random
from GUI_functionalities.MainWindowClass import QuizMainWindow


def test_shuffle_answers():
    correct_answer = "A"
    incorrect_answers = ["B", "C", "D"]

    shuffled_answers, correct_answer_place = QuizMainWindow.shuffle_answers(correct_answer, incorrect_answers)

    assert correct_answer in shuffled_answers
    assert shuffled_answers.count(correct_answer) == 1
    assert correct_answer_place in [1, 2, 3, 4]

    for incorrect_answer in incorrect_answers:
        assert incorrect_answer in shuffled_answers
    assert len(shuffled_answers) == 4
    assert shuffled_answers != incorrect_answers + [correct_answer]

