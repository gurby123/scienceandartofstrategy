import pandas as pd 
import numpy as np 
import statsmodels.api as sm 

# Load data 
data = pd.read_csv('business_data.csv') 

# Define variables according to your own study
X = data[['Advertising, 'Price, 'Quality]] 
y = data['Sales'] 

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# Add constant to X 
X = sm.add_constant(X) 
# Fit multiple regression model 
model = sm.OLS(y, X).fit() 
# Print summary of model results 
print(model.summary())
