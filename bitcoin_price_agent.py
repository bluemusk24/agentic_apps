import requests
import datetime

# Define the Bitcoin Price Agent class
class BitcoinPriceAgent:
    def __init__(self, api_url):
        """
        An agent that will get the current price of Bitcoin.
        Args:
            self: initialize the Bitcoin price agent
            api_url: URL of the API to fetch the Bitcoin price data.
        """
        self.api_url = api_url

    
    def get_bitcoin_price(self):
        """
        Get the current price of Bitcoin in USD from the API and display it along with current time
        """
        try:
            # Get request from the API
            response = requests.get(self.api_url)       
            
            # Get current time
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # check if response was a success and extract the bitcoin price from the parsed JSON data
            if response.status_code == 200:
                data = response.json()
                bitcoin_price = data['bitcoin']['usd']

                print(f"Current price of Bitcoin in USD : ${bitcoin_price}")
                print(f"Timestamp: {current_time}")
            else:
                print("Failed to get current Bitcoin price. Check the API")
                print(f"Attempted at: {current_time}")

        except Exception as e:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"An error occurred at {current_time}: {e}")


def main():
    # the API URL for the CoinDesk Bitcoin Price using CoinGecko's API instead.
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    # create an instance of the BitcoinPrice Agent with the API URL and execute task (get_bitcoin_price)
    agent = BitcoinPriceAgent(api_url=api_url)
    agent.get_bitcoin_price()

if __name__ == "__main__":
    main()