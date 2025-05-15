import pandas as pd

# import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


class FraudDetector:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, data: pd.DataFrame):
        X = data.drop("is_fraud", axis=1)
        y = data["is_fraud"]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.3, random_state=42
        )

        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict(self, data: pd.DataFrame):
        return self.model.predict(data)
