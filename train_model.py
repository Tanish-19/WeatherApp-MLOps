import mlflow
import bentoml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor # Simulating our AutoML winner
import numpy as np

# 1. Start MLflow tracking
mlflow.set_experiment("Weather_Prediction_AutoML")

with mlflow.start_run():
    # 2. Mock Data (Humidity, Wind Speed) -> Target (Temperature)
    X = np.random.rand(100, 2) 
    y = np.random.rand(100) * 35 
    
    # 3. Simulate AutoML training the best model
    # In a real scenario, you'd use a library like FLAML or TPOT here
    print("AutoML searching for best model...")
    best_model = RandomForestRegressor(n_estimators=10)
    best_model.fit(X, y)
    
    # 4. Log the parameters to MLflow
    mlflow.log_param("model_type", "RandomForest (AutoML Winner)")
    mlflow.log_metric("dummy_accuracy", 0.85)
    
    # 5. Save the winning model directly to BentoML
    saved_model = bentoml.sklearn.save_model("weather_automl_model", best_model)
    print(f"Model saved to BentoML: {saved_model.tag}")