import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_test, predictions):
    cm = confusion_matrix(y_test, predictions)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.savefig("MaintenanceSystem/AI-Powered-predictive-Maintenance-System/images/confusion_matrix.png")
    plt.show()


def plot_feature_importance(model, X):
    import pandas as pd

    importance = model.feature_importances_
    features = X.columns

    df = pd.DataFrame({
        'Feature': features,
        'Importance': importance
    }).sort_values(by='Importance', ascending=False)

    plt.figure()
    sns.barplot(x='Importance', y='Feature', data=df)

    plt.title("Feature Importance")
    plt.savefig("MaintenanceSystem/AI-Powered-predictive-Maintenance-System/images/feature_importance.png")
    plt.show()