num1=float(input("enter the number1: "))
num2=float(input("enter the number2: "))
result=0
sign=input("enter the sign: ")

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
else:
  print("invalid sign")

print(result)
