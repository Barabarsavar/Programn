num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Which type of divison would you like to perform?")
ch = input("Enter // for integer division \n Enter / for float division ")

result = 0
if ch == '//':
    result = int (num1 / num2)
elif ch == '/':
    result = float (num1 / num2) 
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)