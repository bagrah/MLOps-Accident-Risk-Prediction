import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data():
    file_path = "data/processed/los_angeles_accidents.csv"
    df = pd.read_csv(file_path)
    return df

def preprocess(df):
    features = [
        'Temperature(F)', 
        'Humidity(%)', 
        'Visibility(mi)', 
        'Wind_Speed(mph)'
    ]
    
    df = df.dropna(subset=features + ['Severity'])
    
    X = df[features]
    y = df['Severity']
    
    return X, y

def train(n_estimators=100):
    df = load_data()
    X, y = preprocess(df)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    with mlflow.start_run():
        
        model = RandomForestClassifier(n_estimators=n_estimators)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        # 🔥 Logging
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Accuracy: {acc}")

if __name__ == "__main__":
    train(n_estimators=50)
    train(n_estimators=100)
    train(n_estimators=200)
    train(n_estimators=300)
