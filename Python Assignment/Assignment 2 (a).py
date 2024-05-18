def generate_list_and_tuple(numbers):
    num_list = numbers.split(',')
    num_tuple = tuple(num_list)
    return num_list, num_tuple

if __name__ == "__main__":
    input_numbers = input("Enter comma-separated numbers: ")
    numbers_list, numbers_tuple = generate_list_and_tuple(input_numbers)
    print("List:", numbers_list)
    print("Tuple:", numbers_tuple)
