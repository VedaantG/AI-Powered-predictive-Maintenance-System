from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluate_model(model, X_test, y_test):
    probs = model.predict_proba(X_test)[:, 1]
    predictions = (probs > 0.2).astype(int) #custom threshold
    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))

    return predictions