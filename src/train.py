import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import joblib
import os

def train():
    df = pd.read_csv("../data/processed/creditcard_processed.csv")

    X = df.drop('Class', axis=1)
    y = df['Class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

    fr = RandomForestClassifier(
        n_estimators=150,
        max_depth=None, 
        min_samples_split=5, 
        min_samples_leaf=5, 
        class_weight="balanced",
        random_state=42
    )

    fr.fit(X_train_res, y_train_res)

    y_pred = fr.predict(X_test)
    print(classification_report(y_test, y_pred))

    joblib.dump(fr, "models/random_forest.pkl")

    print("Modelo salvo com sucesso em models/random_forest.pkl")

if __name__ == "__main__":
    train()
