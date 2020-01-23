number = input("Please, enter positive number: ")
i = 0
max_number = 0
while i != len(number):
    if int(number[i]) > max_number:
        max_number = int(number[i])
    i += 1

print(f"Maximum numeric in your number is: {max_number}")