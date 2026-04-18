from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state=42)
    #Model
    model = RandomForestClassifier(n_estimators=100,random_state=42)
    model.fit(X_train,Y_train)
    #saving model
    joblib.dump(model,"MaintenanceSystem/AI-Powered-predictive-Maintenance-System/models/model.pkl")
    return model, X_test, Y_test