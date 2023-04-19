bien = input("Dime cuantas tienes bien: ")
mal = input("Dime las que tiene mal: ")
resultado = (int(bien)-(int(mal)/2))*(10/55)
if resultado < 5:
    print("Has suspendido")
else : 
    print("Has aprobado")

