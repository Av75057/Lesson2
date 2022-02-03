integer_number = 212976
num = 0
while integer_number>0:
     num += integer_number%10
     integer_number = integer_number//10
print(num)