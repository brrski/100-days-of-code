myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input("What percent tip do you want to leave: 15, 18, 20 percent? "))

answer = (myBill * (1+(tip / 100))) / numberOfPeople
answer = round(answer, 2)

print("You all owe", answer)

