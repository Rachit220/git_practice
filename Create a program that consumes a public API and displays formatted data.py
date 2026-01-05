import requests
API_URL = "https://jsonplaceholder.typicode.com/users"
def fetch_users():
    """
    Fetch user data from public REST API
    """
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()   
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def display_users(users):
    """
    Display formatted user data
    """
    if not users:
        print("No user data available.")
        return

    print("USER LIST")
    print("-" * 50)

    for user in users:
        print(f"ID      : {user['id']}")
        print(f"Name    : {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email   : {user['email']}")
        print(f"City    : {user['address']['city']}")
        print(f"Company : {user['company']['name']}")
        print("-" * 50)

def main():
    users = fetch_users()
    display_users(users)
if __name__ == "__main__":
    main()
