from unittest.mock import patch, mock_open
from GUI_functionalities.FileManagingFunctions import read_highest_score, get_question_from_file
import json


def test_read_highest_score():
    mock_file_content = "100 Ola\n200 Oskar\n300 Boro"
    expected_result = "300 Boro"

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = read_highest_score()
        assert result == expected_result


def test_get_question_from_file():
    questions_list = [
        {'question': 'Question 1', 'answers': ['A', 'B', 'C'], 'correct_answer': 'A'},
        {'question': 'Question 2', 'answers': ['A', 'B', 'C'], 'correct_answer': 'B'},
    ]
    file_content = json.dumps(questions_list)

    with patch('builtins.open', mock_open(read_data=file_content)):
        question = get_question_from_file()

        assert question in questions_list


def test_get_question_from_file_empty_file():
    with patch('builtins.open', mock_open(read_data='')):
        question = get_question_from_file()
        assert question == -2
