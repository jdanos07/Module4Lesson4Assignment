class Weather_Forecast:
    def __init__(self, city, temperature, condition, humidity):
        self.__city = city
        self.__temperature = temperature
        self.__condition = condition
        self.__humidity = humidity


    def get_city(self):
        return self.__city

    def get_temperature(self):
        return self.__temperature
    
    def get_condition(self):
        return self.__condition
    
    def get_humidity(self):
        return self.__humidity
    
    def detailed_data(self):
        return (f'{self.__city} is currently {self.__temperature}°F and the conditions are {self.__condition} with {self.__humidity}% humidity.')
    def simple_data(self):
        return (f'{self.__city} is currently {self.__temperature}°F.')
    
weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }    

while True:
    print('\nCities with available weather data: ')
    for city in weather_data.keys():
        print(f'    {city}')

    city = input("\nEnter the city to get the weather forecast, or 'exit' to quit: ").title()

    if city == 'Exit':
        break

    if city in weather_data:
        data = weather_data[city]
        forecast = Weather_Forecast(city, data["temperature"], data["condition"], data["humidity"])
        detailed = input("Do you want a detailed forecast? Yes/No: ").lower()
    
        if detailed == 'yes':
            print('')
            print(forecast.detailed_data())
        else:
            print('')
            print(forecast.simple_data())
    else:
        print('Input city either has no current data or does not exist.')

