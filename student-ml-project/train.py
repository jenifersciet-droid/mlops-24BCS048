import numpy as np
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate sample student data
np.random.seed(42)
n = 500

study_hours = np.random.uniform(0, 10, n)
attendance = np.random.uniform(40, 100, n)
internal_marks = np.random.uniform(0, 100, n)

# Create demonstration Pass/Fail labels
score = study_hours * 5 + attendance * 0.25 + internal_marks * 0.45
result = np.where(score >= 60, "Pass", "Fail")

data = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "internal_marks": internal_marks,
    "result": result,
})

X = data[["study_hours", "attendance", "internal_marks"]]
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions):.2%}")

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully as model.pkl")
