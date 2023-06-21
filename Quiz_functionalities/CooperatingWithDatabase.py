import requests


def get_questions(amount, difficulty):
    url = f"https://opentdb.com/api.php?amount={amount}&category=9&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    data = response.json()
    if data["response_code"] == 0:
        return data["results"]
    else:
        return ImportError
