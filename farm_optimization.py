import requests
import tkinter as tk
from tkinter import ttk

# API key for weather data
api_key = 'eb0c364260b6523b8432f0b04ae816e5'

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(temp):
    return round(temp - 273.15, 2)

# Function to get real-time weather data
def get_weather_data(city):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = kelvin_to_celsius(data['main']['temp'])
        humidity = data['main']['humidity']
        return temperature, humidity
    except Exception as e:
        return None, None

# Function to get rainfall data for the next days
def get_rainfall_data(city):
    try:
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rainfall = sum(forecast['rain'].get('3h', 0) for forecast in data['list'] if 'rain' in forecast)
        return round(rainfall, 2)
    except Exception as e:
        return None

# Crop recommendations dictionary (same as before)
crop_recommendations = {
    'Wheat': {
                'soil_texture': 'clayey',
                'temperature_range': (0, 25),
                'pesticide': {'Budget Low': 'Cypermethrin', 'Budget Moderate': 'Diafenthiuron',
                              'Budget High': 'Furathiocarb'},
                'fertilizer': {'Budget Low': 'saphate', 'Budget Moderate': 'Bromicide MA', 'Budget High': 'Taophos'},
                'precautions': [
                    'Protect the crop from frost damage during colder temperatures.',
                    'Ensure proper irrigation to maintain soil moisture levels.',
                    'Monitor and control pests and diseases common in wheat crops.',
                    'Implement timely harvesting techniques to maximize yield.',
                    'Store harvested wheat properly to avoid spoilage.'
                ]
            },

            'Rice': {
                'soil_texture': 'loamy',
                'temperature_range': (20, 40),
                'pesticide': {'Budget Low': 'Tribenuron Methyl', 'Budget Moderate': 'Endosulfan',
                              'Budget High': 'Butachlor'},
                'fertilizer': {'Budget Low': 'polyram DF', 'Budget Moderate': 'Kinggo', 'Budget High': 'Saprofon'},
                'precautions': [
                    'Maintain proper water levels in the paddy fields.',
                    'Control weeds and manage pests to avoid crop damage.',
                    'Apply fertilizers in a balanced manner to promote healthy growth.',
                    'Monitor and prevent diseases common in rice crops.',
                    'Harvest the crop at the appropriate stage to ensure good quality.'
                ]
            },
            'Maize': {
                'soil_texture': 'sandy',
                'temperature_range': (25, 40),
                'pesticide': {'Budget Low': 'Fosetyl Aluminium ', 'Budget Moderate': 'Fury',
                              'Budget High': 'isoproturon+Diflufenican'},
                'fertilizer': {'Budget Low': 'Fezdion', 'Budget Moderate': 'Polyram DF ', 'Budget High': 'Tianzi '},
                'precautions': [
                    'Ensure proper irrigation to support maize growth.',
                    'Protect the crop from pests and diseases prevalent in maize fields.',
                    'Apply fertilizers based on soil nutrient requirements.',
                    'Harvest the maize at the optimal stage to achieve maximum yield.',
                    'Store harvested maize in appropriate conditions to maintain quality.'
                ]
            },
            'Tomato': {
                'soil_texture': 'loamy',
                'temperature_range': (18, 27),
                'pesticide': {'Budget Low': 'Fezdion', 'Budget Moderate': 'isoproturon+Diflufenican',
                              'Budget High': 'Saprofon'},
                'fertilizer': {'Budget Low': 'Cypermethrin', 'Budget Moderate': 'Polyram DF', 'Budget High': 'Tianzi '},
                'precautions': [
                    'Protect the plants from frost and extreme heat.',
                    'Provide proper irrigation and drainage to avoid waterlogging.',
                    'Control pests like tomato hornworms and aphids.',
                    'Ensure timely staking or caging of plants.',
                    'Harvest tomatoes when they are fully ripe for best flavor and quality.'
                ]
            },
            'Potato':
                {
                    'soil_texture': 'sandy',
                    'temperature_range': (10, 25),
                    'pesticide': {'Budget Low': 'Cypermethrin', 'Budget Moderate': 'Diafenthiuron',
                                  'Budget High': 'Furathiocarb'},
                    'fertilizer': {'Budget Low': 'Tianzi', 'Budget Moderate': 'Polyram DF', 'Budget High': 'Tianzi '},
                    'precautions': [
                        'Ensure proper hilling to cover tubers and prevent greening.',
                        'Control pests like potato beetles and nematodes.',
                        'Provide adequate irrigation but avoid waterlogging.',
                        'Monitor for diseases such as blight and scab.',
                        'Harvest potatoes carefully to avoid damaging the tubers.'
                    ]
                },

            'Corn': {
                'soil_texture': 'loamy',
                'temperature_range': (21, 30),
                'pesticide': {'Budget Low': 'Tribenuron Methyl', 'Budget Moderate': 'Endosulfan',
                              'Budget High': 'Butachlor'},
                'fertilizer': {'Budget Low': 'Tianzi', 'Budget Moderate': 'Polyram DF', 'Budget High': 'Tianzi '},
                'precautions': [
                    'Plant corn in blocks to ensure proper pollination.',
                    'Control weeds to reduce competition for nutrients.',
                    'Provide irrigation during dry spells.',
                    'Protect against common pests like corn earworms.',
                    'Harvest when the kernels are fully developed and milky.'
                ]
            },
            'Sugarcane': {
                'soil_texture': 'clayey',
                'temperature_range': (20, 45),
                'pesticide': {'Budget Low': 'Tribenuron Methyl', 'Budget Moderate': 'Endosulfan',
                              'Budget High': 'Butachlor'},
                'fertilizer': {'Budget Low': 'saphate', 'Budget Moderate': 'Bromicide MA', 'Budget High': 'Taophos'},
                'precautions': [
                    'Provide adequate irrigation to maintain moisture.',
                    'Control weeds and pests affecting sugarcane plants.',
                    'Harvest at the correct time to maximize sugar content.',
                    'Protect the crop from extreme drought conditions.',
                    'Fertilize appropriately based on soil testing.'
                ]
            },
            'Cotton': {
                'soil_texture': 'sandy',
                'temperature_range': (20, 40),
                'pesticide': {'Budget Low': 'PesticideCT1', 'Budget Moderate': 'PesticideCT2',
                              'Budget High': 'PesticideCT3'},
                'fertilizer': {'Budget Low': 'FertilizerCT1', 'Budget Moderate': 'FertilizerCT2',
                               'Budget High': 'FertilizerCT3'},
                'precautions': [
                    'Control pests such as bollworms and aphids.',
                    'Provide sufficient irrigation during dry periods.',
                    'Harvest cotton at maturity to ensure high-quality fibers.',
                    'Ensure timely application of fertilizers for better yield.',
                    'Prevent waterlogging to avoid root diseases.'
                ]
            },
            'Barley': {
                'soil_texture': 'loamy',
                'temperature_range': (5, 20),
                'pesticide': {'Budget Low': 'Tribenuron Methyl', 'Budget Moderate': 'Endosulfan',
                              'Budget High': 'Butachlor'},
                'fertilizer': {'Budget Low': 'polyram DF', 'Budget Moderate': 'Kinggo', 'Budget High': 'Saprofon'},
                'precautions': [
                    'Protect from frost and provide adequate irrigation.',
                    'Use high-yielding and disease-resistant varieties.',
                    'Harvest at the correct stage for best quality grains.',
                    'Apply fertilizers based on soil testing for optimal growth.'
                ]
            },
            'Onion': {
                'soil_texture': 'sandy',
                'temperature_range': (12, 25),
                'pesticide': {'Budget Low': 'PesticideO1', 'Budget Moderate': 'PesticideO2',
                              'Budget High': 'PesticideO3'},
                'fertilizer': {'Budget Low': 'FertilizerO1', 'Budget Moderate': 'FertilizerO2',
                               'Budget High': 'FertilizerO3'},
                'precautions': [
                    'Avoid waterlogging to prevent fungal diseases.',
                    'Irrigate regularly to maintain consistent soil moisture.',
                    'Protect from pests like thrips and mites.',
                    'Harvest at maturity to avoid storage losses.'
                ]
            },
            'Chilies': {
                'soil_texture': 'loamy',
                'temperature_range': (18, 32),
                'pesticide': {'Budget Low': 'Tribenuron Methyl', 'Budget Moderate': 'Endosulfan',
                              'Budget High': 'Butachlor'},
                'fertilizer': {'Budget Low': 'Tianzi', 'Budget Moderate': 'Polyram DF', 'Budget High': 'Tianzi '},
                'precautions': [
                    'Protect plants from excess moisture to prevent root rot.',
                    'Apply fertilizers to boost flowering and fruiting.',
                    'Control aphids and mites through timely pest management.',
                    'Harvest chilies when they reach the desired color and size.'
                ]
            },
            'Soybean': {
                'soil_texture': 'loamy',
                'temperature_range': (20, 30),
                'pesticide': {'Budget Low': 'Tribenuron Methyl', 'Budget Moderate': 'Endosulfan',
                              'Budget High': 'Butachlor'},
                'fertilizer': {'Budget Low': 'Tianzi', 'Budget Moderate': 'Polyram DF', 'Budget High': 'Tianzi '},
                'precautions': [
                    'Ensure proper spacing to reduce disease risk.',
                    'Monitor for pests like soybean aphids and whiteflies.',
                    'Provide adequate irrigation during pod development.',
                    'Harvest promptly to avoid pod shattering.'
                ]
            },
            'Groundnut': {
                'soil_texture': 'sandy',
                'temperature_range': (25, 35),
                'pesticide': {'Budget Low': 'Tribenuron Methyl', 'Budget Moderate': 'Endosulfan',
                              'Budget High': 'Butachlor'},
                'fertilizer': {'Budget Low': 'Cypermethrin', 'Budget Moderate': 'Polyram DF', 'Budget High': 'Tianzi '},
                'precautions': [
                    'Provide deep plowing to loosen the soil for better growth.',
                    'Control pests like aphids and leaf miners.',
                    'Apply gypsum to improve pod formation.',
                    'Harvest when the pods are mature but not overripe.'
                ]
            },
            'Sunflower': {
                'soil_texture': 'loamy',
                'temperature_range': (20, 30),
                'pesticide': {'Budget Low': 'polyram DF', 'Budget Moderate': 'Kinggo', 'Budget High': 'Saprofon'},
                'fertilizer': {'Budget Low': 'saphate', 'Budget Moderate': 'Bromicide MA', 'Budget High': 'Taophos'},
                'precautions': [
                    'Protect plants from bird damage during flowering.',
                    'Irrigate during dry spells to ensure good seed development.',
                    'Control pests like sunflower moth and aphids.',
                    'Harvest when the back of the flower head turns yellow.'
                ]
            },
            'Bajra': {
                'soil_texture': 'sandy',
                'temperature_range': (25, 35),
                'pesticide': {'Budget Low': 'polyram DF', 'Budget Moderate': 'Kinggo', 'Budget High': 'Saprofon'},
                'fertilizer': {'Budget Low': 'Fosetyl Aluminium ', 'Budget Moderate': 'Fury',
                               'Budget High': 'isoproturon+Diflufenican'},
                'precautions': [
                    'Provide proper weeding to ensure healthy growth.',
                    'Monitor for pests like stem borers.',
                    'Ensure timely sowing to maximize yield.',
                    'Harvest at the right stage to prevent seed shattering.'
                ]
            },
            'Garlic': {
                'soil_texture': 'loamy',
                'temperature_range': (12, 24),
                'pesticide': {'Budget Low': 'Fosetyl Aluminium ', 'Budget Moderate': 'Fury',
                              'Budget High': 'isoproturon+Diflufenican'},
                'fertilizer': {'Budget Low': 'Fezdion', 'Budget Moderate': 'Polyram DF ', 'Budget High': 'Tianzi '},
                'precautions': [
                    'Ensure proper spacing for bulb development.',
                    'Control fungal diseases through crop rotation.',
                    'Avoid waterlogging to prevent root rot.',
                    'Harvest when the leaves start drying.'
        ]
    }
    # Add more crops as needed
}

# Function to calculate recommendations and display in the GUI
def calculate_recommendations():
    city = city_entry.get()
    crop = crop_dropdown.get()
    soil_texture = soil_dropdown.get()
    area = area_entry.get()
    budget = budget_entry.get()

    try:
        area = float(area)
        budget = float(budget)
    except ValueError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Error: Area and Budget must be valid numbers.")
        output_text.config(state=tk.DISABLED)
        return

    # Validate crop and soil texture
    if crop not in crop_recommendations:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {crop} not found in recommendations.")
        output_text.config(state=tk.DISABLED)
        return

    if soil_texture != crop_recommendations[crop]['soil_texture']:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {crop} requires {crop_recommendations[crop]['soil_texture']} soil.")
        output_text.config(state=tk.DISABLED)
        return

    # Get real-time weather data
    temperature, humidity = get_weather_data(city)
    rainfall = get_rainfall_data(city)

    # Check temperature suitability
    temp_range = crop_recommendations[crop]['temperature_range']
    if temperature is None or not temp_range[0] <= temperature <= temp_range[1]:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: Temperature in {city} is unsuitable for {crop}.")
        output_text.config(state=tk.DISABLED)
        return

    # Budget calculation
    budget_per_acre = budget / area
    max_budget_per_acre = 40000  # Example max budget

    # Determine budget category
    if budget_per_acre < 20000:
        budget_category = 'Budget Low'
    elif budget_per_acre <= 30000:
        budget_category = 'Budget Moderate'
    else:
        budget_category = 'Budget High'

    # Get pesticide and fertilizer recommendations
    pesticide = crop_recommendations[crop]['pesticide'][budget_category]
    fertilizer = crop_recommendations[crop]['fertilizer'][budget_category]

    # Yield calculation
    max_yield = {'clayey': 40, 'loamy': 35, 'sandy': 24}[soil_texture]
    yield_per_acre = (budget_per_acre / max_budget_per_acre) * max_yield
    yield_per_acre = min(yield_per_acre, max_yield)
    total_yield = yield_per_acre * area

    # Display results
    output_message = f"City: {city}\nCrop: {crop}\nSoil Texture: {soil_texture}\n"
    output_message += f"Temperature: {temperature}°C\nHumidity: {humidity}%\nRainfall: {rainfall} mm\n\n"
    output_message += f"Pesticide Recommendation: {pesticide}\n"
    output_message += f"Fertilizer Recommendation: {fertilizer}\n\n"
    output_message += f"Yield per Acre: {yield_per_acre:.2f} maunds\nTotal Yield: {total_yield:.2f} maunds\n"
    output_message += "Precautions:\n"
    for precaution in crop_recommendations[crop].get('precautions', []):
        output_message += f"- {precaution}\n"

    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output_message)
    output_text.config(state=tk.DISABLED)

# GUI setup
window = tk.Tk()
window.title("Crop Recommendation System")
window.geometry("1000x700") 
window.config(bg="#1b5e20")  # Green background for the window

# Heading
heading_label = tk.Label(window, text="Crop Recommendation System", font=("Arial", 22), bg="#1b5e20", fg="#FFEB3B")
heading_label.pack(pady=8)

# Input Fields (Centered, above the display box)
input_frame = tk.Frame(window, bg="#1b5e20")
input_frame.pack(pady=8, fill="x", anchor="n")

# Column alignment and equal size setup

tk.Label(input_frame, text="City:", font=("Arial", 14), bg="#1b5e20", fg="#FFEB3B").grid(row=0, column=0, sticky="n", padx=8)
city_entry = tk.Entry(input_frame, font=("Arial", 14), width=24)
city_entry.grid(row=0, column=1, pady=8)

tk.Label(input_frame, text="Select Crop:", font=("Arial", 14), bg="#1b5e20", fg="#FFEB3B").grid(row=1, column=0, sticky="n", padx=8)
crop_dropdown = ttk.Combobox(input_frame, values=list(crop_recommendations.keys()), font=("Arial", 14), width=22)
crop_dropdown.grid(row=1, column=1, pady=8)

tk.Label(input_frame, text="Select Soil Texture:", font=("Arial", 14), bg="#1b5e20", fg="#FFEB3B").grid(row=2, column=0, sticky="n", padx=8)
soil_dropdown = ttk.Combobox(input_frame, values=['clayey', 'loamy', 'sandy'], font=("Arial", 14), width=22)
soil_dropdown.grid(row=2, column=1, pady=8)

tk.Label(input_frame, text="Area (acres):", font=("Arial", 14), bg="#1b5e20", fg="#FFEB3B").grid(row=3, column=0, sticky="n", padx=8)
area_entry = tk.Entry(input_frame, font=("Arial", 14), width=24)
area_entry.grid(row=3, column=1, pady=8)

tk.Label(input_frame, text="Budget:", font=("Arial", 14), bg="#1b5e20", fg="#FFEB3B").grid(row=4, column=0, sticky="n", padx=8)
budget_entry = tk.Entry(input_frame, font=("Arial", 14), width=24)
budget_entry.grid(row=4, column=1, pady=8)

# Calculate Button 
calculate_button = tk.Button(window, text="Calculate Recommendations", font=("Arial", 16), bg="#FFEB3B", fg="#1b5e20", command=calculate_recommendations)
calculate_button.pack(pady=20)

# Output Box 
output_text = tk.Text(window, height=12, width=80, font=("Arial", 14), wrap=tk.WORD, bg="#1b5e20", fg="white", bd=2, padx=8, pady=8)
output_text.pack(pady=8)
output_text.config(state=tk.DISABLED)

# Run the application
window.mainloop()
