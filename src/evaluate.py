from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def evaluate_model(model,X_test,Y_test):
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(Y_test , predictions))
    print("Classification Report:", classification_report(Y_test , predictions))
    print("Confusion Matrix:", confusion_matrix(Y_test , predictions))
    return predictions
