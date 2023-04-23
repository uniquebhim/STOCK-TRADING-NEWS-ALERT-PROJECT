# **Stock Trading News Alert Project**

This is a Python-based project that monitors the stock market and sends SMS alerts when a stock's value changes by a certain percentage. It also provides the latest news about the company whose stock is being monitored.

## **Description**

The Stock Trading News Alert Project retrieves the latest stock prices from Alpha Vantage's API and calculates the difference between the current day's closing price and the previous day's closing price. If the difference is more than 1%, the project retrieves the latest news articles related to the company from NewsAPI's API and sends an SMS alert to the user with the stock's name, the percentage increase or decrease, the headline of the top three articles, and a brief description of each article.

## **Prerequisites**

Before running this project, make sure that you have:

- Python 3.x installed on your computer
- A free Alpha Vantage API key
- A free NewsAPI API key
- A free Twilio account with an available phone number

## **Installation**

1. Clone this repository using Git or download the zip file and extract the contents.
2. Navigate to the project's root directory.
3. Install the required dependencies using pip:

```

pip install -r requirements.txt

```

1. Rename the **`.env_sample`** file to **`.env`** and update the values of the environment variables with your API keys and Twilio account details.

## **Usage**

1. Run the project using the following command:

```

python main.py

```

1. The project will retrieve the latest stock prices and news articles, and send an SMS alert if the stock's value changes by more than 1%.

## **Contributing**

If you find any issues with this project or want to suggest new features, feel free to submit an issue or a pull request.

## **License**

This project is licensed under the MIT License. See the **`LICENSE`** file for more information.

## **Acknowledgements**

- Alpha Vantage API - **[https://www.alphavantage.co/](https://www.alphavantage.co/)**
- NewsAPI - **[https://newsapi.org/](https://newsapi.org/)**
- Twilio API - **[https://www.twilio.com/](https://www.twilio.com/)**
