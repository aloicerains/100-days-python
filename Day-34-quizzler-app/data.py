import requests

URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}
res = requests.get(url=URL, params=parameters)
res.raise_for_status()
question_data = res.json().get('results')

