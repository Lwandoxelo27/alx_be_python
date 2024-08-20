def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        return numerator / denominator
        return result
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero.."
    

import sys
from robust_division_calculator import safe_divide

def main():
    print("Robust Division Calculator")
    print("-------------------------")
    while True:
        numerator = input("Enter the numerator: ")
        denominator = input("Enter the denominator: ")
        result = rdc.safe_divide(numerator, denominator)
        print(result)
        again = input("Do you want to calculate again? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()