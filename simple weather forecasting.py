import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
        else:
            print("City not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter a city: ")
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    get_weather(city, api_key)


#### Code Explanation

The provided Python script is designed to retrieve weather information for a specified city using the OpenWeatherMap API.

It starts by importing the requests library to make HTTP requests to the API.

The get_weather function is the core of the code. It constructs a request to the OpenWeatherMap API with the city name and your API key. The API key is necessary and can be obtained by signing up on the OpenWeatherMap website.

The API query is set up with parameters for the city, API key, and the units for temperature (default is Celsius; change to "imperial" for Fahrenheit).

Upon making the API request, the script attempts to retrieve the weather data and convert it to a JSON format.

If the API request is successful (HTTP status code 200), it displays the weather information for the specified city, including the temperature in Celsius and a brief weather description.

If the city is not found, it prints "City not found."

In case of any other errors during the request, the script displays an error message.

The if __name__ == "__main__": block is the entry point of the program. It prompts the user to input a city name and the OpenWeatherMap API key.

By running the script, you can initiate the weather forecasting process, which showcases the power of using external APIs to gather real-time data.

