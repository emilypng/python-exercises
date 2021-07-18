print("Rate your day on a scale of 1 to 10: ")
rate = input()
# f string
print(f"You rated your day as: {rate}")
# string cocatenation
print("You rated your day as: " + rate)
# string interpolation with comma separators
print("You rated your day as:", rate)
# string interpolation with format
print("You rated your day as: {}".format(rate))