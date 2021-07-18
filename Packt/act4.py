x, y = 24,36
counting = True
i = 1
while counting: 
  if i%x==0 and i%y==0:
    break
  else:
    i += 1
print("The Least Common Multiple of",x,"and",y,"is",i,".")
    
# textbook answer
while counting: 
  if i%x==0 and i%y==0:
    print("The Least Common Multiple of",x,"and",y,"is",i,".")
    break
  i += 1

# Find first number greater than 100 and divisible by 17.
x = 100
while x >= 100:
  if x % 17 == 0:
    print(f"{x} is the first number greater than 100 that is divisible by 17.")
    break
  x += 1


