import yfinance as yf
# Download historical data for a stock
AMD = yf.Ticker("AMD")
AMD_info = AMD.info
# print(AMD_info)
AMD_sector = AMD_info['sector']
# print(AMD_sector)
AMD_price = AMD_info['currentPrice']
print(AMD_price)