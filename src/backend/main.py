import yfinance as yf
import numpy as np
import pandas as pd
import pyasx.data.companies
results = pyasx.data.companies.get_company_announcements('CBA')

df = pd.DataFrame(results)

# Show first 10 companies
print(df.head(10))


cba = yf.Ticker("CBA.AX")

# print(cba.info)  # general company info

# Get historical prices
hist = cba.history(period="1mo")
# print(hist)