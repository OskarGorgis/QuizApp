import none
import requests


def get_questions(amount):
    url = f"https://opentdb.com/api.php?amount={amount}&category=9&type=multiple"
    response = requests.get(url)
    data = response.json()
    if data["response_code"] == 0:
        return data["results"]
    else:
        return ImportError
