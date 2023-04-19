ahorros = input("¿Cuánto dinero tienes en la cuenta? ")
ahorros = float(ahorros)
intereses = input("¿Cuánto interes tiene en la cuenta? ")
intereses = float(intereses)
intereses = intereses / 100
primer_ano = (ahorros * intereses)+ahorros
segundo_ano = ahorros + (ahorros + primer_ano) * intereses
tercer_ano = ahorros + (ahorros + segundo_ano) * intereses
primer_ano = round(primer_ano, 2)
segundo_ano = round(segundo_ano, 2)
tercer_ano = round(tercer_ano, 2)
print("En el primer año tendrás", primer_ano, "euros")
print("En el segundo año tendrás", segundo_ano, "euros")
print("En el tercer año tendrás", tercer_ano, "euros")