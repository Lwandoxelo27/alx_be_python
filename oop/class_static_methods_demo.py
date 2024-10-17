class Calculator:
    calculation_type = "Arithmetic Operations"

    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers."""
        print(f"Performing {cls.calculation_type}...")
        return a * b

# Testing the Calculator class
if __name__ == "__main__":
    print("Static Method Example:")
    result = Calculator.add(5, 3)
    print(f"Sum: {result}")

    print("\nClass Method Example:")
    result = Calculator.multiply(5, 3)
    print(f"Product: {result}")
``)
