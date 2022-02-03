#integer_number = 2129
#print(integer_number%10,integer_number//10)
#while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10
integer_number = 2576875
i = len(str(integer_number))
while integer_number>0:
     i -= 1
     print(integer_number//10**i)
     integer_number = integer_number%10**i

