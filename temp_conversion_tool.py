FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor for F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor for C to F

def convert_to_celsius(fahrenheit):
  """
  Converts a temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit (float): The temperature in Fahrenheit.

  Returns:
      float: The temperature converted to Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """
  Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius (float): The temperature in Celsius.

  Returns:
      float: The temperature converted to Fahrenheit.
  """
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
  """
  Prompts the user for temperature and unit, performs conversion, and displays the result.
  """
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
      break
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

  if unit == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature:.1f}°C is {converted_temp:.1f}°F")
  elif unit == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature:.1f}°F is {converted_temp:.1f}°C")
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
  main()