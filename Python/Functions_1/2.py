def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Read Fahrenheit temperature from the user
fahrenheit_temperature = float(input())

# Convert Fahrenheit to Celsius
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Display the result
print(fahrenheit_temperature, "degrees Fahrenheit is equal to", celsius_temperature, "degrees Celsius.")