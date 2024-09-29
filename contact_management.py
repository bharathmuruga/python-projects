
def display(people):
  for i ,person, in enumerate(people):
    print(i+1,"-",person["name"],"|",person["age"],"|",person["email"])


def add_person():
  name=input("enter the name: ").lower()
  while True:
    try:
      age=int(input("enter the age: "))
      if age<=0 or age>=110:
        print("invalid age")
      else:
        break

    except :
      print("invaild age ")

  email=input("enter the email: ")
  person={"name":name,"age":age,"email":email}
  return person


def search_person(people):
  search_name=input("enter the name: ").lower()
  result=[person for person in people if search_name in person["name"]]
  if result:
    display(result)
  else:
    print("not found")

def total_contact(people):
  print(f"number of contact: {len(people)}")

  
def delete_person(people):
  if not people:
    print("contact is empty!!!")
    return
  display(people)
  while True:
    try:
        dele=int(input("enter the number :"))
        if dele!=0 and dele<=len(people):
          people.pop(dele-1)
          print(" deleted successfully!!!")
          break
        else:
          print("number does not exist!!!")
    except:
        print("invalid input!!!")

  
print("HI WELCOME TO CONTACT MANAGEMENT LIST")
print()
people=[]



def main():
  while True:
    command=input("You can 'ADD' ,'SEARCH','DELETE' and 'Q' for quit: ").lower()
    if command=="add":
      person=add_person()
      people.append(person)
      print("person add successfully")
      total_contact(people)
    elif command=="search":
      search_person(people)
    elif command=="delete":
      delete_person(people)
      total_contact(people)
    elif command=="q":
      print("your exiting the application!!!")
      break
    else:
      print("invalid input!!!")


if __name__=="__main__":
   main()
