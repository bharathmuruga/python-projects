# checks for list of even number


def numbers():
  num_list=[]
  while True:
    try:
      total=int(input("enter total number: "))
      break
    except ValueError:
      print("ivalid number")
  while True:
    try:
        if len(num_list)<total:
          number=int(input("enter the number: "))
          num_list.append(number)
        else:
          break
    except ValueError:
      print("invaild number ")
  return num_list



num_list=numbers()

print(num_list)

even_numbers=list(filter(lambda a:a%2==0,num_list))

n=set(even_numbers)
even_number_onduplicate=list(n)

print(f"even numbers are{even_numbers}")
print(even_number_onduplicate)