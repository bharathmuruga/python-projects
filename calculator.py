def get_number():
    while True:
      try:
        num=input("enter the number: ")
        num=float(num)
        break 
      except:
        print("invalid number try ,again")
    return num
  
def get_sign():
  while True:
    sign=input("enter the sign: ")
    if sign=="+" or sign=="-" or sign=="*" or sign=="/":
      return sign
    else:
      print("invalid sign")


def main():
  num1=get_number()
  num2=get_number()
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

