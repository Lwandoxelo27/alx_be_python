# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Impliment conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is the temperature in Celcius or Fahrenheit? (C/F): ")
            if unit == "C":
                print(f"{temperature}C is equal to {convert_to_fahrenheit(temperature)}F")
            elif unit == "F":
                print(f"{temperature}F is equal to {convert_to_celsius(temperature)}C")
            else:
                print("Invalid unit. Please enter C or F.")
        except ValueError:
            print("Invalit temperature. Please enter a numerical value.")

if __name__ == "__main__":
    main()