import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
from alpha_vantage.fundamentaldata import FundamentalData
import streamlit as st
# Setting your API key
key = "6F52R6LXSFBMDURY"

# Creating a FundamentalData object
fd = FundamentalData(key)

symbol = st.sidebar.text_input("Enter stock symbol (e.g. AAPL):", "AAPL")
start_date = st.sidebar.date_input("Select start date:", pd.to_datetime("2010-01-01"))
end_date = datetime.now().date()  # Use today's date as end date

st.write('Income Statement')
financials, meta_data = fd.get_income_statement_annual(symbol)
ICTR = (financials[financials.columns[:]]) 
ICT= ICTR.T
ICT.columns = ICT.iloc[0] #make top row as column index
IC = ICT.reindex(columns=ICT.columns[::-1]) #reverse the new column index
st.write(IC)

# Change Data object to float
NI = IC.loc["netIncome"].astype(float)
plt.plot(NI)
plt.xlabel('Date')
plt.ylabel('Price in millions')
plt.title('Net Income in Yearly')
plt.show()
st.pyplot()

st.write('Balance Sheet')
balance_sheet, meta_data = fd.get_balance_sheet_annual("AAPL")
#BS = balance_sheet.iloc[:,::-1] # Reverse Column
BSIR = (balance_sheet[balance_sheet.columns[:]]) 
BSR= BSIR.T
BSR.columns = BSR.iloc[0] #make top row as column index
BS = BSR.reindex(columns=BSR.columns[::-1]) #reverse the new column index
BS = BS.fillna(value=np.nan)
BS

st.write('CashFlow')
cash_flow, meta_data = fd.get_cash_flow_annual("AAPL")
CFTR = (cash_flow[cash_flow.columns[:]]) 
CFT= CFTR.T
CFT.columns = CFT.iloc[0] #make top row as column index
CF = CFT.reindex(columns=CFT.columns[::-1]) #reverse the new column index
CF = CF.fillna(value=np.nan)
CF
st.write("Current Ratio = CurrentAssets/Current Liabilities")
CR = BS.loc['totalCurrentAssets'].astype(int) / BS.loc['totalCurrentLiabilities'].astype(int)
CR
st.write("Quick Ratio")
QR = (BS.loc['totalCurrentAssets'].astype(int) - BS.loc['inventory'].astype(int)) / BS.loc['totalCurrentLiabilities'].astype(int) # (Total Current Assets-Inventory)/Total Current Liabilities
QR
st.write('CashR')
CashR = (BS.loc['cashAndCashEquivalentsAtCarryingValue'].astype(int) - BS.loc['shortTermInvestments'].astype(int)) / BS.loc['totalCurrentLiabilities'].astype(int) # (Cash + Short Term Investments + Intangible Assets)/ Total Current Liabilities)
CashR
st.write('Networking Capital to Current Liabilities')
NCCL = (BS.loc['totalCurrentAssets'].astype(int) - BS.loc['totalCurrentLiabilities'].astype(int)) / BS.loc['totalCurrentLiabilities'].astype(int) # (Total Current Assets - Total Current Liabilities)/Total Current Liabilities)
NCCL
# ### Asset Utilization or Turnover ratios
st.write('Asset Utilization or Turnover ratios')
st.write('-'*40)
st.write('Average Collection Period')
ACP = BS.loc['currentNetReceivables'].astype(int) / (IC.loc['totalRevenue'].astype(int)/360) # Net Receivables/(Total Revenue/360)
ACP
st.write('Inventory Turnover Ratios')
ITR = IC.loc['totalRevenue'].astype(int) / BS.loc['inventory'].astype(int)# Total Revenue / Inventory
ITR                                             
st.write('Receivable Turnover')
RT = IC.loc['totalRevenue'].astype(int)/BS.loc['currentNetReceivables'].astype(int) # Total Revenue / Net Receivables
RT                                                     
st.write('Fixed Asset Turnover')
FAT = IC.loc['totalRevenue'].astype(int)/BS.loc['currentNetReceivables'].astype(int) # Total Revenue / Property, plant and equipment
FAT
st.write('Total Asset Turnover')                                             
TAT = IC.loc['totalRevenue'].astype(int)/BS.loc['totalAssets'].astype(int)# Total Revenue / Total Assets
TAT                                               
# ### Financial Leverage ratios
st.write('Financial Leverage ratios')
st.write('-'*40)
st.write('Total Debt Ratio')
TDR = BS.loc['totalLiabilities'].astype(int) / BS.loc['totalAssets'].astype(int) # Total Liabilities / Total Assets
TDR
st.write('Debt/Equity')
DE = BS.loc['totalLiabilities'].astype(int) / BS.loc["totalShareholderEquity"].astype(int) # Total Liabilities / Total stockholders' equity
DE
st.write('Equity Ratio')
ER = BS.loc["totalShareholderEquity"].astype(int) / BS.loc['totalAssets'].astype(int) # Total stockholders' equity / Total Assets
ER
st.write('Long-term Debt Ratio')
LTDR = BS.loc['longTermDebt'].astype(int) / BS.loc['totalAssets'].astype(int) # Long Term Debt / Total Assets
LTDR
st.write('Times Interest Earned Ratio')
TIER = IC.loc['ebit'].astype(int) / IC.loc['interestAndDebtExpense'].astype(int) # Earnings Before Interest and Taxes / Interest Expense
TIER
# ### Profitability ratios
st.write('Profitability ratios')
st.write('-'*40)
st.write('Gross Profit Margin')
GPM = IC.loc['grossProfit'].astype(int) / IC.loc['totalRevenue'].astype(int) # Gross Profit / Total Revenue
GPM
st.write('Net Profit Margin')
NPM = IC.loc['netIncomeFromContinuingOperations'].astype(int) / IC.loc['totalRevenue'].astype(int) # Net Income / Total Revenue
NPM
st.write('Return on Assets (ROA)')
ROA = IC.loc['netIncomeFromContinuingOperations'].astype(int) / BS.loc['totalAssets'].astype(int) # Net Income / Total Assets
ROA
st.write('Return on Equity (ROE)')
ROE = IC.loc['netIncomeFromContinuingOperations'].astype(int) / BS.loc['totalShareholderEquity'].astype(int) # Net Income / Total Equity
ROE

# Fetching stock financials for Yahoo

stock = yf.Ticker(symbol)
df = yf.download(symbol, start=start_date, end=end_date)
st.write('First Five Records of Dowloaded Data from 2010 to Today')
st.write(df.head())
st.write('Last Five Records of Dowloaded Data from 2010 to Today')
st.write(df.tail())
st.write('General Stock Information Summary from Yahoo')
stock.info
