import mlflow.pyfunc
import pandas as pd

# Load model dari MLflow (Production)
model = mlflow.pyfunc.load_model("models:/accident-severity-model@production")

print("Model loaded successfully!")

# Dummy data (sesuaikan fitur kamu)
data = pd.DataFrame([{
    "Temperature(F)": 70,
    "Humidity(%)": 60,
    "Visibility(mi)": 10,
    "Wind_Speed(mph)": 5
}])

# Prediksi
pred = model.predict(data)

print("Prediction:", pred)
