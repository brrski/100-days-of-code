print("Welcome to your grading system")
print("Please follow the instructions as they appear")

testName = input("What is the name of the test taken? ")
maxScore = int(input("What is the maximum score you can receive or " \
"how many questions are on the test? "))
userScore = int(input("What score did you receive? "))
userPercentage = round(userScore / maxScore, 2)

if userPercentage >= 0.9:
  print("You got an A+ on the", testName, "test!💃🏻💫 Nice!")

elif userPercentage >= 0.8:
  print("OK OK I see you big A!!🤩🥳")

elif userPercentage >= 0.7:
  print("Let's go B! Next time you'll see an A in", testName, "😎")

elif userPercentage >= 0.6:
  print("You got a C", testName, "might need more library time😕")

elif userPercentage >= 0.5:
  print("Wow really fam a D on the", testName, "test🦉")

else:
  print("Fucked around got an F in", testName, "dumbass😭😭😭")  
