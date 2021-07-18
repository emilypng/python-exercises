# first stupid voice chat bot
print("Are you a girl or boy?: ")
gender = input()
print("I am a",gender,"too!")

print("What is your name?")
name = input()
print("We're kindred spirits, "+name+". Talk later.")

# second stupid voice chat bot
print("How intelligent are you on a scale of 1-10? ")
intelligence = abs(int(input()))

if intelligence <=5:
  print("We all have different talents!")
else:
  print("Are you human? 10 is human, 0 is computer.")

yes_no = abs(int(input()))
if yes_no >=5:
  print("Nice to meet you!")
else:
  print("Hello friend.")
