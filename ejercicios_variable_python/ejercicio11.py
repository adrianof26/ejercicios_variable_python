cantidad = float(input("Cantidad que va a invertir: "))
interes = float(input("Introduzca el interés anual: "))
años = int(input("Cuantos años quieres: "))
capital = cantidad * (interes/100+1) ** años #Es la formula que encontré en internet
print("Capital final: " + str(capital))