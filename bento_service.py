import bentoml
import numpy as np

# 1. In modern BentoML, we use a class with a decorator instead of a variable
@bentoml.service(
    name="weather_prediction_service"
)
class WeatherService:
    
    # 2. Reference the model we saved in script 1
    bento_model = bentoml.models.get("weather_automl_model:latest")

    def __init__(self):
        # 3. Load the actual Scikit-Learn model into memory when the server boots
        self.model = bentoml.sklearn.load_model(self.bento_model)

    # 4. Create the API endpoint (BentoML now reads the type hints automatically!)
    @bentoml.api
    def predict(self, input_data: np.ndarray) -> np.ndarray:
        return self.model.predict(input_data)