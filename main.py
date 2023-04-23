import requests
from twilio.rest import Client

# Stock parameters for Alpha Vantage API
STOCK = "TSLA"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": "api_key"
}

# Stock endpoint for Alpha Vantage API
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

# Retrieve daily stock data from Alpha Vantage API
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)

# Check for any errors in the response
stock_response.raise_for_status()

# Extract daily stock data from the response
stock_data = stock_response.json()["Time Series (Daily)"]

# Print the daily stock data
print(stock_data)
print('\n')

# Convert daily stock data to a list for easier processing
stock_data_list = [value for (key, value) in stock_data.items()]

# Print the list of daily stock data
print(stock_data_list)
print('\n')

# Calculate the closing price difference between yesterday and the day before yesterday
yesterday_data = stock_data_list[0]
yesterday_data_closing_price = float(yesterday_data['4. close'])

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_data_closing_price = float(
    day_before_yesterday_data['4. close'])

difference = yesterday_data_closing_price - \
    day_before_yesterday_data_closing_price
difference_percentage = abs(difference / yesterday_data_closing_price * 100)

# Print the closing price difference and percentage
print(f"{difference}:  {difference_percentage}")

# If the percentage difference is greater than 1%, retrieve news articles related to the stock from News API
if difference_percentage > 1:
    news_parameters = {
        "q": STOCK,
        "apiKey": "api_key"
    }

    # News endpoint for News API
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    # Retrieve news articles from News API
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)

    # Check for any errors in the response
    news_response.raise_for_status()

    # Extract news articles from the response
    articles = news_response.json()['articles']

    # Print the news articles
    print(articles)

    # Select the top three news articles
    three_articles = articles[:3]

    # Print the top three news articles
    print(three_articles)

# API credentials for Twilio API
account_sid = "account_sid"
auth_token = "auth_token"

# Determine whether the stock price has gone up or down and format the news articles for SMS
up_down = None
if difference_percentage > 1:
    up_down = "🔺"
else:
    up_down = "🔻"
formatted_articles = [
    f"\n{STOCK}: {up_down}{difference_percentage}%\n\nHeadline: {article['title']}. \n\nBrief: {article['description']}" for article in three_articles]

for article in formatted_articles:
    # Send the formatted news articles via SMS using Twilio API
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=article,
        from_='+16000000002',
        to='+918000000001'
    )
# Print a success message after the SMS is sent
print("SMS sent successfully.")
