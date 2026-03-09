**# Binance Futures Testnet Trading Bot**



**A simplified Python trading bot that places orders on Binance Futures Testnet.**



**## Features**



**- Market orders**

**- Limit orders**

**- Stop orders (bonus)**

**- CLI interface**

**- Input validation**

**- Logging to file**

**- Error handling**

**- Clean modular structure**



**## Setup**



**1 Clone repository**



**git clone https://github.com/yourname/binance-trading-bot**



**2 Install dependencies**



**pip install -r requirements.txt**



**3 Configure environment**



**Rename .env.example to .env**



**Add your Binance Testnet keys.**



**## Running**



**Market Order**



**python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001**



**Limit Order**



**python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000**



**Stop Order**



**python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.001 --price 58000**



**## Logs**



**Logs are stored in:**



**logs/bot.log**

