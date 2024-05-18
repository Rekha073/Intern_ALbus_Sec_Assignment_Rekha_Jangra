class Calculator:
    @staticmethod
    def square(num):
        return num ** 2

    @staticmethod
    def cube(num):
        return num ** 3

# Example usage:
calculator = Calculator()
number = 5
square_result = calculator.square(number)
cube_result = calculator.cube(number)
print(f"Square of {number} is: {square_result}")
print(f"Cube of {number} is: {cube_result}")
