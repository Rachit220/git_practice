import requests

# Make a GET request to a public API
response = requests.get('https://api.github.com')

# Check if the request was successful (Status Code 200)
if response.status_code == 200:
    print("Success!")
    # Parse the data as JSON
    data = response.json()
    print(data['repository_url'])
else:
    print(f"Failed with status code: {response.status_code}")