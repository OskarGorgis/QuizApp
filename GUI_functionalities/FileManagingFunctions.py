import json
import os
import random

high_score_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Data_files", "high_scores"))
questions_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Data_files",
                                                   "custom_questions.json"))


def read_highest_score():
    highest_score = 0
    line_with_highest_score = ""
    with open(high_score_file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
        for line in lines:
            score = int(line.split(" ")[0])
            if score > highest_score:
                line_with_highest_score = line
                highest_score = score

    return line_with_highest_score


def save_score_in_file(line_to_save):
    with open(high_score_file_path, 'a') as file:
        file.write("\n"+line_to_save)


def get_question_from_file():
    with open(questions_file_path, 'r') as file:
        try:
            questions_list = json.load(file)
            question_number = random.randint(0, len(questions_list)-1)
            return questions_list[question_number]
        except EOFError:
            return -1


def save_question_to_file(question, correct_answer, incorrect_answers):
    new_question = {"question": question,
                    "correct_answer": correct_answer,
                    "incorrect_answers": incorrect_answers}
    try:
        with open(questions_file_path, 'r') as file:
            questions_list = json.load(file)
    except json.JSONDecodeError:
        questions_list = []

    questions_list.append(new_question)

    with open(questions_file_path, 'w') as file:
        json.dump(questions_list, file, indent=4)
