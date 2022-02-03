integer_number = 213541535
i = 0
while integer_number>0:
    if integer_number%10 == 5:
       i += 1
    integer_number = integer_number//10
print(i)
