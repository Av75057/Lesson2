integer_number = 23987
num = 1
while integer_number>0:
     num *= integer_number%10
     integer_number = integer_number//10
print(num)