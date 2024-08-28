#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
n = 1
n_list = []
while n <= 1000:
    if n % 3 == 0:
        n_list.append(n)
    n += 1
print(n_list)

