# functions.py
def temperature_conversion(temperature, conversion_type):
    if conversion_type == 'celsius to fahrenheit':
        return temperature * 9 / 5 + 32
    elif conversion_type == 'fahrenheit to celsius':
        return (temperature - 32) * 5 / 9
    return None

conversion_type = input("Enter the conversion type (Celsius to Fahrenheit or Fahrenheit to Celsius): ").strip().lower()
temperature_input = float(input("Input the temperature value: "))
converted_temperature = temperature_conversion(temperature_input, conversion_type)

if converted_temperature is not None:
    print(f"Converted temperature: {converted_temperature:.2f}")
else:
    print("Invalid conversion type selected.")


