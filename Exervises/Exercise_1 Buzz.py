# Adevanced Code
# for i in range(100):
#     print(int(i % 3 / 2) * 'Fizz' + int(i % 5 / 4) * 'Buzz' or -~i)

# Using For loop
for i in range(1,101):
    if i%15 == 0: # if the number % 15 is equal to 0 means it could be devided by 3 and 5.
        print("FizzBuzz")
    else:
        if i%3 == 0: # if the number % 3 is equal to 0.
            print("Fizz")
        elif i%5 == 0: # if the number % 5 is equal to 0.
            print("Buzz")
        else: # The conditions aboe are not true then print the number.
            print (i)