peso = float(input("Deme su peso: "))
altura = float(input("Deme su altura: "))
imc = peso/(altura**2)
imc=round(imc,2)
print("Tu índice de masa corporal es "+str(imc))