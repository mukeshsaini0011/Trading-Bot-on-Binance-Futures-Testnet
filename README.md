Binance Futures Testnet Trading Bot
Overview

This project is a Python CLI-based trading bot that places orders on Binance USDT-M Futures Testnet.

It supports:

MARKET orders

LIMIT orders

BUY and SELL sides

CLI-based input

Structured logging

Error handling and validation

The project follows a modular design separating API logic, order handling, validation, and CLI interface.


Prerequisites

Python 3.9+

Binance Futures Testnet account

API Key and Secret (Futures Testnet)

Testnet URL:

https://testnet.binancefuture.com/fapi

Setup Instructions
1️⃣ Clone Repository
git clone 


2️⃣ Create Virtual Environment
python -m venv .venv

3️⃣ Activate Virtual Environment
Windows (PowerShell)
.\.venv\Scripts\Activate.ps1


If execution policy error occurs:

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


Then activate again.

Windows (CMD)
.\.venv\Scripts\activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Configure Environment Variables

Create a .env file in the project root:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_SECRET_KEY=your_testnet_secret_key


Running the Bot

All commands must be run from the project root.

MARKET Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000


Note:

BUY LIMIT price must typically be below market price

SELL LIMIT price must typically be above market price

Output

The application prints:

Order request summary

Order ID

Order status

Executed quantity

Average price (if available)

Success or failure message

Logging

All API requests, responses, and errors are logged to:

logs/bot.log


Each log entry includes:

Timestamp

Log level

Request parameters

Full API response

Error details (if any)

Validation & Error Handling

The application handles:

Invalid order type

Invalid side

Missing required parameters

Negative quantity or price

API errors

Network failures

Exchange rule violations

Assumptions

Only USDT-M Futures supported

LIMIT orders use GTC (Good Till Cancel)

Leverage configuration is not implemented

Symbol precision rules are validated by Binance

Acceptance Criteria Coverage

✔ MARKET orders
✔ LIMIT orders
✔ BUY and SELL support
✔ CLI input handling
✔ Structured code separation
✔ Logging implemented
✔ Error handling implemented
✔ Clean, reusable structure

Author

Mukesh Saini
Python Developer