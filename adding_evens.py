# find the sum of all even numbers between 1 and 100

total_even = 0
for num in range(1, 101):
    if num % 2 == 0:
        total_even += num

print(total_even)
