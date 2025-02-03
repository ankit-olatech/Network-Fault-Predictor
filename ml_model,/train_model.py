import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load sample dataset
data = pd.read_csv("sample_network_data.csv")  # Assume CSV file has latency, packet_loss, jitter, label

# Preprocess
X = data[['latency', 'packet_loss', 'jitter']]
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'ml_model/network_fault_model.pkl')
print("Model trained and saved!")
