# Load your data as a NumPy array
data = np.genfromtxt('business_performance.csv', delimiter=',', names=True)

#convert to dataFrame
df = pd.DataFrame(data)

# Define your SEM model
model = '''
    # Define the latent variables
    performance =~ x1 + x2 + x3
    entrepreneurship =~ x4 + x5 + x6 + x7
    innovation =~ x8 + x9 + x10 + x11
    strategy =~ x12 + x13 + x14 + x15

    # Define the structural relationships
    performance ~ entrepreneurship + innovation + strategy
    entrepreneurship ~ innovation + strategy
    innovation ~ strategy
'''
model_fit = semopy.Model(model)
model_fit.load_dataset(df)

# Fit model to data
model_fit.fit(df)

opt = Optimizer(model_fit)
result = inspect(opt)
print(result)

#calculate statistics for goodness of fit
stats = calc_stats(model_fit)
print(stats)

g = semopy.semplot(model_fit, "sie.png")
