# 90) Write python program that user to enter only odd numbers, else 
# will raise an exception.

try:
    num = int(input("Enter an odd number: "))

    if num % 2 == 0:
        raise Exception("Even number allowed nahi hai!")

    print("Valid odd number:", num)

except ValueError:
    print("Sirf number daalo, text nahi!")

except Exception as e:
    print("Exception:", e)

finally:
    print("Program end ho gaya.")
