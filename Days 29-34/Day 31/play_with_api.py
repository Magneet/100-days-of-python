import requests

result = response = requests.get("https://api.kanye.rest")
print(dir(result))
print(type(result.text))
result_json = result.json()
print(type(result_json))
print(result_json)