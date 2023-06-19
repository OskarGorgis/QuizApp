def read_highest_score(file_name):
    highest_score = 0
    line_with_highest_score = ""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
        for line in lines:
            score = int(line.split(" ")[0])
            if score > highest_score:
                line_with_highest_score = line
                highest_score = score

    return line_with_highest_score


def save_line_in_file(file_name, line_to_save):
    with open(file_name, 'a') as file:
        file.write(line_to_save)
