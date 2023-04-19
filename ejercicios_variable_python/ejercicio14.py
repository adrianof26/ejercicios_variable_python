pan = input("¿Cuanto pan fresco quieres comprar? ")
pan = float(pan)
pan_no_fresco = input("¿Cuanto pan no fresco quieres comprar? ")
pan_no_fresco = float(pan_no_fresco)
pan =pan * 3.49
pan_no_fresco = pan_no_fresco * 3.49 * 0.60
total = pan + pan_no_fresco
total = round(total, 2)
print("El precio habitual del pan es de 3.49 euros y el descuento que se le hace por no ser fresco es del 60%, el precio total de su compra es " +str(total)+ " euros")