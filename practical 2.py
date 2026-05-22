'''#reverse of number
num = int(input("enter a numbers: "))
reverse_num = 0
while num > 0:
    digits = num % 10
    reverse_num = reverse_num*10+digits
    num = num//10
print("the reverse of the number is: ",reverse_num)


#sum of digits
num = int(input("enter a numbers: "))
sum_of_digits = 0
while num > 0:
    digits = num % 10
    sum_of_digits += digits
    num = num//10
print("the sum of digits of the number is: ",sum_of_digits)


#factorial of number
num = int(input("enter a numbers: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("the factorial of the number is: ",factorial)


#10 consecutive odd number
num = 31
count = 0
total = 0
while count < 10:
    total += num
    num += 2
    count += 1
print("the sum of 10 consecutive odd number starting from 31 is: ", total)


#palindrome or not
num = int(input("enter a numbers: "))
original_num = num
reverse_num = 0
while num > 0:
    digits = num % 10
    reverse_num = reverse_num*10+digits
    num = num//10
if original_num == reverse_num:
    print(original_num,"is palindrome")
else:
    print(original_num,"is not a palindrome")


#armstrong or not
num = int(input("enter a numbers: "))
original_num = num
num_digits = len(str(num))
armstrong_sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp = temp//10
if original_num == armstrong_sum:
    print(original_num,"is armstrong")
else:
    print(original_num,"is not a armstrong")


#*  *   *  *  *
#*  *   *  *  *
#*  *   *  *  *
#*  *   *  *  *
#*  *   *  *  *

for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()'''

#multiplication of table from 10 to 15
for num in range(10, 16):
    print(f"\nMultiplication of table for {num}")
    for i in range(1, 11):
        print(f"{num}x{i}={num*i}")

