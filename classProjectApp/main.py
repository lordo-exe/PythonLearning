import requests
# Not done yet
# Obtaining the ZIP from the user through their manual input
zipCode = input("Enter a U.S ZIP code for weather results!: ")

# Making a variable for the API key from which we obtain data
# Includes .format that pulls 'zipCode' and inserts it into the string for relevant data
url = "https://api.openweathermap.org/data/2.5/weather?zip=68123," \
      "us&appid=7babd1ea47bae79c9d11902793e59399&units=imperial".format(zipCode)

# Requesting data from 'url' which is our API key weather data
res = requests.get(url)

# Converting that requested data from 'res' into json through the new variable 'data'
data = res.json()


weatherDesc = data['weather'][0]['description']
temp = data['main']['temp']
feelsLike = data['main']['feels_like']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
cityName = data['name']
windSpeed = data['wind']['speed']


def print_weather_results():
    # These prints show your ZIP codes relevant weather data in an organized manner
    print("\nHere are weather results for the", zipCode, "area. \n")

    print("Weather description:", weatherDesc.title())
    print("Current temperature:", temp, "°F")
    print("Temperature feels like:", feelsLike, "°F")
    print("Current humidity:", humidity, "%")
    print("Current pressure:", pressure)

print_weather_results()