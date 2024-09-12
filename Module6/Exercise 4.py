'''def main():
    list_int = [1,2,3,4,5,6,7,8,9,10]
    #list_int = range(1,11)
    i = sum(list_int)
    print(i)

print('Sum of those integers is :')
main()'''
#from Module4.Exercise3 import number_s


def first(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_num = sum(first(11))
print(f'Sum of those integers is:{sum_num}')