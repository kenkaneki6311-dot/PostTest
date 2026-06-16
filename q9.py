import requests
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

# print(f"Name:{user['name']}")
# print(f"Email:{user['email']}")
# print(f"Phone:{user['phone']}")

for user in data:
    print(f"Name: {user['name']} - Email: {user['email']} Phone:{user['phone']}")

print(f"Total number of users: {len(data)}")