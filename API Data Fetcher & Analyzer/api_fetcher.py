import requests
import json

def fetch_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[❌] API Request Error: {e}")
        return None

def extract_prices(data, keyword=None):
    extracted = {}
    if "bpi" in data:
        for code, info in data["bpi"].items():
            currency = info["code"]
            rate = info["rate"]
            if not keyword or keyword.lower() in currency.lower():
                extracted[currency] = rate
    return extracted

def print_report(prices):
    print("\n📊 Bitcoin Price Report")
    print("-" * 30)
    for currency, price in prices.items():
        print(f"{currency}: {price}")

def save_report(prices, filename="btc_price_report.txt"):
    with open(filename, "w") as f:
        f.write("📊 Bitcoin Price Report\n")
        f.write("-" * 30 + "\n")
        for currency, price in prices.items():
            f.write(f"{currency}: {price}\n")
    print(f"\n✅ Report saved to {filename}")

def main():
    default_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    user_url = input(f"Enter API URL or press Enter to use default [{default_url}]: ").strip()
    api_url = user_url if user_url else default_url

    keyword = input("Optional: Filter currency by keyword (e.g., USD, EUR): ").strip()

    data = fetch_api_data(api_url)
    if data:
        prices = extract_prices(data, keyword)
        if prices:
            print_report(prices)
            save_report(prices)
        else:
            print("[⚠️] No currencies matched the keyword.")
    else:
        print("[❌] Failed to fetch or parse API data.")

if __name__ == "__main__":
    main()
