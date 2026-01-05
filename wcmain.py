from weatherapi import get_weather
from currencyapi import get_exchange_rate

def main():
    city = "Kalol"
    base_currency = "USD"
    target_currency = "INR"      
    print("CITY INSIGHT DASHBOARD")
    print("-" * 40)
    temperature = get_weather(city)
    if temperature is not None:
        print(f"Weather in {city}: {temperature}°C")
    else:
        print("Weather data not available")
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        print(f"1 {base_currency} = {rate} {target_currency}")
    else:
        print("Currency data not available")
    print("-" * 40)
if __name__ == "__main__":
    main()
