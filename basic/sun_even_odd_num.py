# Function to calculate the sum of even and odd numbers
def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

# Input: Number of digits
n = int(input("enter the no of element in list: "))

# Input: List of numbers
numbers = []
for i in range(n):
    num = int(input("enter the number: "))
    numbers.append(num)

# Call the function to calculate the sum of even and odd numbers
even_sum, odd_sum = sum_even_odd(numbers)

# Output: Display the sum of even and odd numbers
print("the sum of even number is", even_sum)
print("the sum of odd number is", odd_sum)
