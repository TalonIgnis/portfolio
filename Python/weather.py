user_name = input("what is your name: \n")

print("welcome " +user_name+ ".")

user_city =input("What city do you come from? \n")

print (f"as you are from {user_city}, lets get your weather report.")


weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
"New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, 
"Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
"Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
"Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} } 

def weather(user_city):
    city = user_city.title()
    try:
        temp = weather_data[city]["temperature"]
        conditions = weather_data[city]["conditions"]
        wind = weather_data[city]["wind_speed"]
        humid = weather_data[city]["humidity"]
        print(f"in {city} the weather is: \nTemperature:{temp}\nConditions:{conditions}\nWind speed: {wind} \n and finally the humidity is: {humid}\n")
    except KeyError:
        print("We do not have data on that city please try a captial city.")

weather(user_city)