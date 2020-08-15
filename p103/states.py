import requests

url = "https://covidtracking.com/api/states?state=ny"

response = requests.request("GET", url)

print(response.text)
