def number_operations():
    numbers = []
    even_numbers = []
    odd_numbers = []
    total = 0
    above_average = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input(f"number[{i}]: "))  # แปลงเป็น int
        numbers.append(number)
        total += number
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    average = total / 10.0

    for i in range(10):
        if numbers[i] > average:
            above_average.append(numbers[i])
    
    # Display results
    print(f"Original numbers: {numbers}")
    print("even number list", even_numbers)
    print("odd number list", odd_numbers)
    print("sum:", total)
    print("average:", average)
    print("above average:", above_average)
    print("min:", min(numbers))
    print("max:", max(numbers))

if __name__ == "__main__":
    number_operations()
