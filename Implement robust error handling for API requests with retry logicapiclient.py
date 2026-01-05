import requests
import time
class APIClient:
    def __init__(self, base_url, retries=3, timeout=5):
        self.base_url = base_url
        self.retries = retries
        self.timeout = timeout
    def get(self, endpoint):
        attempt = 0
        while attempt < self.retries:
            try:
                print(f"Attempt {attempt + 1} → Fetching data...")
                response = requests.get(
                    self.base_url + endpoint,
                    timeout=self.timeout
                )
                if response.status_code >= 500:
                    raise requests.exceptions.HTTPError(
                        f"Server error: {response.status_code}"
                    )
                if response.status_code >= 400:
                    print(f"Client error: {response.status_code}")
                    return None
                return response.json()
            except requests.exceptions.Timeout:
                print("Timeout occurred")
            except requests.exceptions.ConnectionError:
                print("Connection error")
            except requests.exceptions.HTTPError as e:
                print(e)
            except ValueError:
                print("Invalid JSON response")
                return None
            attempt += 1
            wait_time = 2 ** attempt
            print(f"Retrying in {wait_time} seconds...\n")
            time.sleep(wait_time)
        print("Failed after maximum retries")
        return None
