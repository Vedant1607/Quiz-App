import requests

# parameters for the API request
parameters = {
    "amount":10,
    "type": "boolean"
}

# Send a GET request to the Open Trivia Database API to fetch quiz questions
response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status() # Raise an HTTPError if the request resulted in an unsuccessful status code

# Extract the 'results' key from the JSON response, which contains the question data
question_data = response.json()["results"]