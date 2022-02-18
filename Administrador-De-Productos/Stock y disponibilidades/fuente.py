import os
import platform
# FUNCIONES EXTERNAS A UTILIZAR.
def limpiar():
    if(platform.system()=="Windows"):
        os.system("cls")
    else:
        os.system("clear")
def inicioSesion():
    clavesHabilitadas=["090807","3232","1029","123321"]
    claveIngresada=input("Contraseña de acceso: ")
    accesoGarantizado=bool()
    for passw in clavesHabilitadas:
        if(passw==claveIngresada):
            accesoGarantizado=True
            break
        else:
            accesoGarantizado=False
    return accesoGarantizado
def cantidadDisponible():
    lineas=[]
    sellos=[]
    cantidades=[]
    j=0
    archivoLectura=open("C:/Users/franc/OneDrive/Escritorio/Programas para vender/Stock y disponibilidades/lista.txt","r")
    while(True):
        lectura=archivoLectura.readline()
        if(lectura==''):
            break
        else:
            lineas.append(lectura.strip("\n"))
    while(j!=len(lineas)):
        sellos.append(lineas[0+j])
        j=j+4
    for i in range(len(sellos)):
        print(str(i+1)+". "+str(sellos[i]).upper())
    numeroSello=int(input("Ingresa el numero del producto que queres conocer la cantidad: "))
    j=0
    while(j!=len(lineas)):
        cantidades.append(lineas[1+j])
        j=j+4
    limpiar()
    print("Cantidad disponible: "+str(cantidades[numeroSello-1]))
    archivoLectura.close()
def precios():
    lineas=[]
    preciosVenta=[]
    preciosCosto=[]
    sellos=[]
    j=0
    archivoLectura=open("C:/Users/franc/OneDrive/Escritorio/Programas para vender/Stock y disponibilidades/lista.txt","r")
    while(True):
        lectura=archivoLectura.readline()
        if(lectura==''):
            break
        else:
            lineas.append(lectura.strip("\n"))
    while(j!=len(lineas)):
        sellos.append(lineas[0+j])
        preciosVenta.append(lineas[2+j])
        preciosCosto.append(lineas[3+j])
        j=j+4
    for i in range(len(sellos)):
        print(str(i+1)+". "+str(sellos[i]).upper())
    numeroSello=int(input("Ingresa el numero del producto que queres conocer la cantidad: "))
    limpiar()
    print("Precio de venta: "+preciosVenta[numeroSello-1])
    print("Precio de costo: "+preciosCosto[numeroSello-1])
    archivoLectura.close()
def agregarSello():
    lineas=[]
    archivoLectura=open("C:/Users/franc/OneDrive/Escritorio/Programas para vender/Stock y disponibilidades/lista.txt","r")
    while(True):
        lectura=archivoLectura.readline()
        if(lectura==''):
            break
        else:
            lineas.append(lectura.strip("\n"))
    selloNuevo=input("Nombre: ")
    cant=int(input("Cantidad disponible: "))
    precioVenta=float(input("Precio de venta: "))
    precioCosto=float(input("Precio de costo: "))
    lineas.append(selloNuevo)
    lineas.append(cant)
    lineas.append(precioVenta)
    lineas.append(precioCosto)
    archivoEscritura=open("C:/Users/franc/OneDrive/Escritorio/Programas para vender/Stock y disponibilidades/lista.txt","w")
    for i in range(len(lineas)):
        dato=lineas[i]
        archivoEscritura.write(str(dato))
        archivoEscritura.write("\n")
    limpiar()
    print("Producto agregado correctamente!")
    archivoLectura.close()
    archivoEscritura.close()
def sellosEnFalta():
    lineas=[]
    sellosFaltantes=[]
    j=0
    archivoLectura=open("C:/Users/franc/OneDrive/Escritorio/Programas para vender/Stock y disponibilidades/lista.txt","r")
    while(True):
        lectura=archivoLectura.readline()
        if(lectura==''):
            break
        else:
            lineas.append(lectura.strip("\n"))
    while(j!=len(lineas)):
        if(lineas[1+j]=="0"):
            sellosFaltantes.append(lineas[j].upper())
        j=j+4
    if(len(sellosFaltantes)==0):
        print("No hay ningun producto en falta...")
    else:
        limpiar()
        print("PRODUCTOS EN FALTA: ")
        for i in range(len(sellosFaltantes)):
            print("- "+sellosFaltantes[i])
def modificarCant():
    lineas=[]
    sellos=[]
    j=0
    i=1
    archivoLectura=open("C:/Users/franc/OneDrive/Escritorio/Programas para vender/Stock y disponibilidades/lista.txt","r")
    while(True):
        lectura=archivoLectura.readline()
        if(lectura==''):
            break
        else:
            lineas.append(lectura.strip("\n"))
    print(
"""1. Cambiar cantidad
2. Cambiar precio de venta
3. Cambiar precio de costo
"""      )
    op=int(input("Ingresa la opcion elegida: "))
    limpiar()
    while(j!=len(lineas)):
        print(str(i)+". "+str(lineas[0+j].upper()))
        sellos.append(lineas[0+j])
        j=j+4
        i=i+1
    numSello=int(input("Ingresa el numero del producto elegido: "))
    limpiar()
    if(op==1):
        nuevaCantidad=int(input("Cantidad nueva del producto en cuestion: "))
        for i in range(len(lineas)):
            if(lineas[i]==sellos[numSello-1]):
                lineas[i+1]=nuevaCantidad
                break
        limpiar()
        print("Producto "+str(sellos[numSello-1].upper())+" cambiado correctamente")
    if(op==2):
        nuevoPV=int(input("Precio de venta nuevo del producto en cuestion: "))
        for i in range(len(lineas)):
            if(lineas[i]==sellos[numSello-1]):
                lineas[i+2]=nuevoPV
                break
        limpiar()
        print("Producto "+str(sellos[numSello-1].upper())+" cambiado correctamente")
    if(op==3):
        nuevoPC=int(input("Precio de costo nuevo del producto en cuestion: "))
        for i in range(len(lineas)):
            if(lineas[i]==sellos[numSello-1]):
                lineas[i+3]=nuevoPC
                break
        limpiar()
        print("Producto "+str(sellos[numSello-1].upper())+" cambiado correctamente")
    archivoEscritura=open("C:/Users/franc/OneDrive/Escritorio/Programas para vender/Stock y disponibilidades/lista.txt","w")
    for i in range(len(lineas)):
        dato=lineas[i]
        archivoEscritura.write(str(dato))
        archivoEscritura.write("\n")
# FUNCION PRINCIPAL DE TRABAJO Y DE INICIO DE SESION.
condiccion=inicioSesion()
while(condiccion==False):
    limpiar()
    print("Clave incorrecta...")
    condiccion=inicioSesion()
limpiar()
def main():
    print(
"""---MENU DE OPCIONES---
1. Ver cantidades disponibles de un producto
2. Ver precios de un producto
3. Agregar un producto a la lista
4. Modificar un producto
5. Ver productos en falta
6. Salir del programa
"""     )
    op=int(input("Ingresa la opcion que elegiste: "))
    if(op==1):
        limpiar()
        cantidadDisponible()
    if(op==2):
        limpiar()
        precios()
    if(op==3):
        limpiar()
        agregarSello()
    if(op==4):
        limpiar()
        modificarCant()
    if(op==5):
        limpiar()
        sellosEnFalta()
    if(op==6):
        exit(1)
main()
while(True):
    op=int(input("Ingresa 1 para volver al menu de opciones, o 2 para salir del programa: "))
    limpiar()
    if(op==1):
        main()
    else:
        exit(1)