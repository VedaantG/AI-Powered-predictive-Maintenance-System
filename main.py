import pandas as pd

from src.preprocess import preprocess_data
from src.features import create_features
from src.model import train_model
from src.evaluate import evaluate_model
from src.visualize import plot_confusion_matrix, plot_feature_importance

# Load dataset
df = pd.read_csv("data/ai4i2020.csv")

print("🔹 Raw Data Shape:", df.shape)

# Preprocess
df = preprocess_data(df)
print("🔹 After Preprocessing:", df.shape)

# Features
X, y = create_features(df)
print("🔹 Features Shape:", X.shape)

# Train model
model, X_test, y_test = train_model(X, y)

# Evaluate
predictions = evaluate_model(model, X_test, y_test)

# Visualizations
plot_confusion_matrix(y_test, predictions)
plot_feature_importance(model, X)