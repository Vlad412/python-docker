import requests

print("Good mroning")

res = 2 + 2

print(f"result is {res}")

r = requests.get("https://www.google.com")

print(r.encoding)
