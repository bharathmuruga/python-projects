
def add_person():

  name=input("enter the name: ")
  while True:
    try:
      age=int(input("enter the age: "))

      break

    except :
      print("invaild age ")

  email=input("enter the email: ")
  person={"name":name,"age":age,"email":email}
  return person
def search_person():
  pass
def delete_person():
  pass
  
print("HI WELCOME TO CONTACT MANAGEMENT LIST")
print()
people=[]

command=input("You can 'ADD' ,'SEARCH','DELETE', person: ").lower()
if command=="add":
  person=add_person()
  persons.append(person)
elif command=="search":
  pass
elif command=="delete":
  pass
else:
  print("invalid input!!!")



print(persons)