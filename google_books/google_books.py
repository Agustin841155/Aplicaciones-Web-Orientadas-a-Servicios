import requests
import json

result = requests.get('http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6')
print(result.status_code)
print(result.text)

books = result.json()
print(type(books))

items = books[("items")]

coded = json.dumps(items)
decoded = json.loads(coded)

print(decoded[0])