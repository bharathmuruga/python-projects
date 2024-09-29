
names=[]
ages=[]
emails=[]


for i in range(3):
  print(i+1,"input")

  name=input("enter the name: ")
  while True:
    try:
      age=int(input("enter the age: "))

      break

    except :
      print("invaild age ")

  email=input("enter the email: ")
  names.append(name)
  ages.append(age)
  emails.append(email)

print(names,ages,emails)