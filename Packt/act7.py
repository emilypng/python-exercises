# exercise: adding matrices 
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[10,11,12],[13,14,15],[16,17,18]]

# Initialize a result placeholder
result = [[0,0,0], 
         [0,0,0], 
        [0,0,0]] 

# iterate through rows
for i in range(len(X)):  
# iterate through columns 
  for j in range(len(X[0])): 
    result[i][j] = X[i][j] + Y[i][j] 
    
print(result)

# activity 17: Storing Company Employee Table Data Using a List and a Dictionary

employees = [
  {
    'name': "John",
    'age': 38,
    'department': "sales"
  },
  {
    'name':"Lisa",
    'age':29,
    'department':'marketing'
  },
  {
    'name':"Sujan",
    'age':38,
    'department':"HR"
  }
]

print(employees)

for employee in employees: 
  print("Name:",employee['name'])
  print("Age:",employee['age'])
  print("Department:",employee['department'])
  print('-'*20)


#Print the details of all employees in a presentable format.
#rint only the details of Sujan Patel. You should get the following output:
