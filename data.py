import requests

parameters = {
    "amount":10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php",params=parameters)

question_bank = response.json()["results"]