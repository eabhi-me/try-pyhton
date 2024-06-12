# Function to find the count of vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # List of vowels
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Input: Take a string from the user
user_input = input("Enter a string: ")

# Call the function to count vowels
result = count_vowels(user_input)

# Output: Display the count of vowels in the string
print("Number of vowels in the string:", result)
