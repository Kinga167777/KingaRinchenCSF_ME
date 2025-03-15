import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum(start, end):
    """Calculate the sum of all prime numbers in a given range."""
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

def length_converter(value, direction):
    """Convert meters to feet or feet to meters."""
    if direction == 'M':
        return round(value * 3.28084, 2)  # Meters to feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # Feet to meters
    else:
        return "Invalid direction. Please use 'M' for meters to feet or 'F' for feet to meters."

def consonant_count(text):
    """Count the consonants in a string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count

def min_max_finder(numbers):
    """Find the smallest and largest number from the list."""
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

def is_palindrome(text):
    """Check if a string is a palindrome."""
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

def display_menu():
    """Display the menu of available functions."""
    print("\nSelect a function:")
    print("1. Prime Number Sum Calculator")
    print("2. Length Unit Converter")
    print("3. Consonant Counter")
    print("4. Min-Max Number Finder")
    print("5. Palindrome Checker")
    print("6. Exit")

def main():
    """Main function to handle user interaction."""
    while True:
        display_menu()

        # Get user's choice
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            start = int(input("Enter the starting range: "))
            end = int(input("Enter the ending range: "))
            result = prime_sum(start, end)
            print(f"The sum of prime numbers between {start} and {end} is: {result}")

        elif choice == '2':
            value = float(input("Enter the length value: "))
            direction = input("Enter conversion direction ('M' for meters to feet, 'F' for feet to meters): ")
            result = length_converter(value, direction)
            print(f"Converted value: {result}")

        elif choice == '3':
            text = input("Enter a string: ")
            result = consonant_count(text)
            print(f"The number of consonants is: {result}")

        elif choice == '4':
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            smallest, largest = min_max_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")

        elif choice == '5':
            text = input("Enter a string: ")
            result = is_palindrome(text)
            print(f"Is the string a palindrome? {result}")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please select a number between 1 and 6.")

        continue_choice = input("Do you want to perform another operation? (y/n): ").lower()
        if continue_choice != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()


        


  
