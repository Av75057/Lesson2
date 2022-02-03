integer_number = 21834137
max = integer_number % 10
while integer_number>0:
    if integer_number%10 > max:
        max = integer_number%10
    integer_number = integer_number//10
print(max)