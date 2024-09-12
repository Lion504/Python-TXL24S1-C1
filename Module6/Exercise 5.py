def first(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
        nums_update = [num for num in nums if (num % 2) == 0]
    print(nums)
    print(nums_update)
    return nums_update

sum_num = sum(first(11))
print(f'Sum of those integers is:{sum_num}')


