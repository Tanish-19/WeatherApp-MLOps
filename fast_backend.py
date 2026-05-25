from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Define the expected input
class WeatherData(BaseModel):
    humidity: float
    wind_speed: float

@app.post("/api/predict")
def get_prediction(data: WeatherData):
    # Format data for BentoML (it expects a 2D array)
    formatted_data = [[data.humidity, data.wind_speed]]
    
    # Send the data to the BentoML service
    bento_response = requests.post(
        "http://bento_server:3000/predict",
        json={"input_data": formatted_data}
    )
    
    # Extract the number from the response
    prediction = bento_response.json()[0]
    
    return {
        "status": "success",
        "predicted_temperature": round(prediction, 2)
    }