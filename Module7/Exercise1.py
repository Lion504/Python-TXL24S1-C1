month = {
    (3,4,5):'spring',
    (6,7,8):'summer',
    (9,10,11):'autumn',
    (1,2,12):'winter'
}
input_month = int(input("Enter a number of month: "))

for months, season in month.items():
    if input_month in months:
        print(f"month {input_month} is {season} season")
        break
else:
    print('Invalid input')