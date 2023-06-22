from GUI_functionalities.FileManagingFunctions import read_highest_score
import pytest


def test_read_highest_score():
    assert read_highest_score() == "1000 Test score"
