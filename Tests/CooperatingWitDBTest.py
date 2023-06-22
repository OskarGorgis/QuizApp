import pytest
from Quiz_functionalities.CooperatingWithDatabase import get_questions


@pytest.mark.parametrize("amount, difficulty", [
    (1, "easy"),
    (1, "medium"),
    (1, "hard")
])
def test_get_questions(amount, difficulty):
    questions = get_questions(amount, difficulty)
    assert isinstance(questions, list)
    assert len(questions) == amount

    for question in questions:
        assert "category" in question
        assert "question" in question
        assert "correct_answer" in question
        assert "incorrect_answers" in question

        assert isinstance(question["incorrect_answers"], list)
        assert len(question["incorrect_answers"]) == 3

        assert question["correct_answer"] not in question["incorrect_answers"]

        if question["difficulty"] == "easy":
            assert difficulty == "easy"

        if question["difficulty"] == "medium":
            assert difficulty == "medium"        

        if question["difficulty"] == "medium":
            assert difficulty == "medium"


