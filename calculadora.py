num = float(input("Ingrese el primer numero :"))
operador = input("Ingrese el simbolo matematico para hacer el calculo ")
num2 = float(input("Ingrese el segundo numero para hacer el calculo  :"))

if operador == "+" :
    numTotal = num + num2
    print(numTotal)
elif operador == "-":
    numTotal = num - num2
    print(numTotal)
elif operador == "x":
    numTotal = num * num2
    print(numTotal)
elif operador == "/":
    numTotal = num / num2
    print(numTotal)
elif operador == "*":
    numTotal = num ** num2
    print(numTotal)
elif operador == "Mod":
    numTotal = num % num2
    print(numTotal)
else:
    print("Error en la introduccion de los datos.")


    
