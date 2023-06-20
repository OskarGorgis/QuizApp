import os


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
            question = file.readline()
            return question
        except EOFError:
            return -1
