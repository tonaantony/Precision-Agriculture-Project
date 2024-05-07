import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

# Load the dataset
data = pd.read_csv("yield.csv")

# Define categorical columns
categorical_cols = ['Area', 'Item']

# Preprocess the data
preprocessor = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Split the data into features (X) and target (y)
X = data.drop("hg/ha_yield", axis=1)
y = data["hg/ha_yield"]

# Apply the transformation to the entire dataset
X_encoded = preprocessor.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)

# test the model
accuracy = rf_model.score(X_test, y_test)
print("Accuracy:", accuracy)

def analyze(Item, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp):
    # Define default values
    default_area = "India"
    default_year = datetime.now().year

    # Create sample data with default values for Area and Year
    sample_data = pd.DataFrame([[default_area, Item, default_year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp]], columns=X.columns)
    sample_encoded = preprocessor.transform(sample_data)

    # Make prediction for the sample data using Random Forest
    predicted_yield = rf_model.predict(sample_encoded)[0]
    print("Random Forest Yield Prediction:", predicted_yield)

    accuracy = rf_model.score(X_test, y_test)
    print("Accuracy:", accuracy)

    return predicted_yield