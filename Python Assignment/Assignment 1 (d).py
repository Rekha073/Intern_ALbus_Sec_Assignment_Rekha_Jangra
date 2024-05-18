class Programmer:
    def __init__(self, name, employee_id, position, language):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.language = language

    def display_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Position:", self.position)
        print("Primary Programming Language:", self.language)
        print()

# Example usage:
programmer1 = Programmer("Alice", "M101", "Software Engineer", "Python")
programmer2 = Programmer("Bob", "M102", "Senior Software Engineer", "Java")
programmer3 = Programmer("Charlie", "M103", "Data Scientist", "R")

print("Programmer 1 Information:")
programmer1.display_info()

print("Programmer 2 Information:")
programmer2.display_info()

print("Programmer 3 Information:")
programmer3.display_info()
