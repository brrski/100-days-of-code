print("Lets figure out how many seconds are in a year")

year = float(input("What year is it? "))
if year % 4 == 0:
  print("It is a leap year")
  print("There are", 60*60*24*366, "seconds in a leap year")

else:
  print("There are", 60*60*24*365, "seconds in a year")
  
  
