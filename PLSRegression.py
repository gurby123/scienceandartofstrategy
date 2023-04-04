from sklearn.cross_decomposition import PLSRegression
import pandas as pd
import numpy as np

from sklearn.cross_decomposition import PLSRegression
import pandas as pd
import numpy as np

# Load the Boston Housing dataset
data_url = "https://raw.githubusercontent.com/gurby123/SEM/main/housing.csv"
raw_df = pd.read_csv(data_url, sep="\s+", header=None)

data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
np.savetxt("my_data2.csv", data, delimiter=",")
np.savetxt("my_target2.csv", target, delimiter=",")
#X = data
#y = target

# Create a PLS model with 10 components
pls = PLSRegression()

# Fit the PLS model
pls.fit(data, target)

# Print the R-squared value
print("R-squared:", pls.score(data, target))

# Get the coefficients for each variable
coefficients = np.squeeze(pls.coef_[:13])

# Rank order the coefficients based on their absolute values
sorted_indices = sorted(range(len(coefficients)), key=lambda i: abs(coefficients[i]), reverse=True)

# Print the rank-ordered coefficients
for i in sorted_indices:
    print(f"Variable {i+1}: ranked_coefficient = {coefficients[i]}")
