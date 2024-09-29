def get_number(number):
    while True:
      try:
        num=input(f"enter the number{number} : ")
        num=float(num)
        return num
      except:
        print("invalid number try ,again")
    
  
def get_sign():
  while True:
    sign=input("enter the sign: ")
    if sign=="+" or sign=="-" or sign=="*" or sign=="/":
      return sign
    else:
      print("invalid sign")


def main():
  num1=get_number(1)
  num2=get_number(2)
  sign=get_sign()
 
  result=0
  if sign=="+":
      result=num1+num2
  elif sign=="-":
      result=num1-num2
  elif sign=="*":
          result=num1*num2
  elif sign=="/":
        if num2!=0:
          result=num1/num2
        else:
          print("zero division")


  print(result)

if __name__=="__main__":
  main()

