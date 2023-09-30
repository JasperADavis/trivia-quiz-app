import requests

categories = {
    "general": 9,
    "television": 14,
    "video games": 15,
    "science & nature": 17,
    "computers": 18,
    "mythology": 20,
    "celebrities": 26,
    "animals": 27,
    "gadgets": 30,
}

parameters = {
    "amount": 20,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
