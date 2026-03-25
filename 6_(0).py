sum_of_squares= 0
for i in range(1, 101): sum_of_squares += i*i
print(sum_of_squares)

square_of_sum = ((100*101)/2 )**2
print(square_of_sum)

print(abs(square_of_sum-sum_of_squares))