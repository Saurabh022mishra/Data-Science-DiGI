def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

# read the number of test cases
num_test_cases = int(input())
b=[]

# iterate over the test cases
for i in range(num_test_cases):
    n = int(input())
    b.append(sum_of_digits(n))
for i in range(len(b)):
    print(b[i])
