# Ask user for an input. Find the biggest number.

# pseudocode
# number = input("input a number")
print("Enter the first number:")
first_number_float = float(input())
first_number_whole = round(first_number_float)

print("Enter the second number:")
second_number_float = float(input())
second_number_whole = round(second_number_float)

if second_number_whole > first_number_whole:
  biggest_number = second_number_whole
else:
  biggest_number = first_number_whole

print("Enter the third number:")
third_number_float = float(input())
third_number_whole = round(third_number_float)

if third_number_whole > biggest_number:
  biggest_number = third_number_whole

print("Enter the fourth number:")
fourth_number_float = float(input())
fourth_number_whole = round(fourth_number_float)

if fourth_number_whole > biggest_number:
  biggest_number = fourth_number_whole

print("Enter the fifth number:")
fifth_number_float = float(input())
fifth_number_whole = round(fifth_number_float)

if fifth_number_whole > biggest_number:
  biggest_number = fifth_number_whole

print("The biggest whole number is:", biggest_number)



 
    
