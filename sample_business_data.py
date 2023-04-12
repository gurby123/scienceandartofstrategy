import random
import csv

# Set seed for reproducibility
random.seed(123)

# Generate data
data = []
for i in range(1000):
    advertising = round(random.uniform(10, 100), 2)
    price = round(random.uniform(1, 10), 2)
    quality = round(random.uniform(1, 5), 2)
    sales = round((advertising * 2) + (price * 3) + (quality * 5) + random.normalvariate(0, 10), 2)
    data.append([advertising, price, quality, sales])

# Write data to CSV file
with open("sample_business_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Advertising", "Price", "Quality", "Sales"])
    writer.writerows(data)