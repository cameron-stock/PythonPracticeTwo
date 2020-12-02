def weather_condition(temperature):
    if temperature > 90:
        return "Hot"
    elif 89 > temperature >= 60:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter Temperature:"))
print(weather_condition(user_input))