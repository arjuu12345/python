day=(input("Enter the date number :"))
month=(input("Enter the month in number:"))
year=int(input("Enter the year in number:"))
print(f"Entered date: {day}-{month}-{year}")
if(year %  4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is leap year.")
else:
    print(f"The year {year} is not leap year.")
