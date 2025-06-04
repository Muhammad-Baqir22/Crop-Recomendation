# Crop-Recomendation
Crop Recommendation System
--------------------------
Description:
This is a desktop application built with Python and Tkinter that recommends suitable crops based on weather data (using OpenWeatherMap API) and soil conditions. It helps farmers choose the best crops by considering factors such as temperature, soil type, and budget for pesticides and fertilizers.

Features:
- Fetches real-time weather data using OpenWeatherMap API.
- Maintains a crop database with soil, temperature, pesticide, and fertilizer info.
- Recommends crops suitable for current conditions.
- Suggests pesticides and fertilizers based on budget.
- Estimates expected crop yield.
- User-friendly GUI for easy data input and recommendations.

Setup Instructions:
1. Install Python 3.x from https://www.python.org/downloads/
2. Install required packages:
   Run `pip install -r requirements.txt`
3. Get an API key from OpenWeatherMap (https://openweathermap.org/api).
4. Replace the placeholder API key in the Python script with your own.
5. Run the Python script to launch the app:
   `python crop_recommendation.py`

Usage:
- Enter your location to fetch weather data.
- Input soil type and budget.
- Click "Get Recommendation" to see crop suggestions and related info.

Files:
- crop_recommendation.py  : Main Python application code.
- requirements.txt        : Required Python libraries.

Notes:
- Requires internet connection for weather API.
- Designed for educational and small-scale use.

Author:
Muhammad Baqir
Date: 2025

