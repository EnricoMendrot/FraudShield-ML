import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def test():
    df = pd.read_csv("data/processed/creditcard_processed.csv")

    X = df.drop('Class', axis=1)
    y = df['Class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    fr = joblib.load("models/random_forest.pkl")

    y_probs = fr.predict_proba(X_test)[:, 1]
    threshold = 0.6
    y_pred_custom = (y_probs >= threshold).astype(int)
    
    print(classification_report(y_test, y_pred_custom))
    print(confusion_matrix(y_test, y_pred_custom))

if __name__ == "__main__":
    test()
