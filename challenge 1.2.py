year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, "is a leap year.")
elif year % 100 == 0:
  print(year, "is not a leap year because it's divisable by 100 but not by 400.")
else :
  print(year, "is not a leap year.") 