# Write a program that prompts the user to input number of calls and calculate the monthly
# telephone bills as per the following rule:
# A:- Minimum Rs. 200 for up to 100 calls.
# B:- Rs. 0.60 per call for next 50 calls.
# C:- Plus Rs. 0.50 per call for next 50 calls.
# D:- Plus Rs. 0.40 per call for any call beyond 200 calls.

number_of_calls = int(input("Enter the number of calls in month: "))


def bill_calculator(number_of_calls):
    if 0 <= number_of_calls <= 100:
        return 200
    elif 100 < number_of_calls <= 150:
        return 200 + (number_of_calls - 100) * 0.60
    elif 150 < number_of_calls <= 200:
        return 200 + 50 * 0.60 + (number_of_calls - 150) * 0.50
    elif number_of_calls > 200:
        return 200 + 50 * 0.60 + 50 * 0.50 + (number_of_calls - 200) * 0.40
    else:
        print("Please enter valid number of calls.")


bill = bill_calculator(number_of_calls)
print(f"Monthly Bill is {bill} Rs only")

