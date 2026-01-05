import requests

def get_exchange_rate(base="USD", target="INR"):
    """
    Fetch currency exchange rate
    """
    url = "https://api.frankfurter.app/latest"
    response = requests.get(url, params={"base": base})
    data = response.json()
    return data["rates"].get(target)
