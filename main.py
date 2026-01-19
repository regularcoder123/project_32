user_num = input("Please input your number:")
user_int = int(user_num)
user_str = str(user_num)
n = len(user_str)
armstrong_calc = 0
for digit in user_str:
    armstrong_calc = int(digit) ** n

if armstrong_calc == user_int:
    print("You have an armstrong number")
else:
    print("You dont have an armstrong number")