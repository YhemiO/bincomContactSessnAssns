# The Necessary Libraries are pandas numpy matplotlib scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("heart.csv")

#preview the data
print(data.head())

#dataset summary
print(data.info())

# cheking for missing value
print(data.isna().sum()) #No missing value

# Separating the DEPENDENT(X) from the INDEPENDENT(Y) variable
X = data[['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']] # Features Columns
y = data['output'] # Target Columns

# Spliting the data into Training and Testing sets
# from sklearn.model_selection import train_test_split (already imported above)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Build and Train the Linear Regression Model
# from sklearn.linear_model import LinearRegression

# create a linear regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Evaluating the model
# from sklearn.metrics import mean_squared_error, r2_score

# predict the target variable from the test set
y_pred = model.predict(X_test)

# calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate the R-squared value (how well model explains the variance in the data)
r2 =r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# VISUALIZING THE RESULT
# import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted')
plt.show()




