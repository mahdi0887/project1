print("welcome to calculator")
print("Amalgarha:")
print("+")
print("-")
print("*")
print("/")

amalgar = input("amalgar movrede nazar ra entekhab kon:")
num1 = float(input("num1 ra vared kon:"))
num2 = float(input("num2 ra vared kon:"))
if amalgar == "+":
    natije = num1=num2
elif amalgar == "-":
    natije = num1-num2
elif amalgar == "*":
    natije = num1*num2
elif amalgar == "/":
    if num2 == 0:
        print("taghsim bar 0 momken nist")
        natije = None
    else:
        natije = num1/num2
if natije is not None:
    print("javab:",natije)
