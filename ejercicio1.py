# codigo de python ejercicio numero #1



# codigo!
#!/usr/bin/env python3

# imports
import sys
import time
import os
import math


# funciones de las operadores de la calculadora
def devolverOperacion(p):
    opcOperacion = str(input("Quiere regresar a menu si o no: "))
    if( opcOperacion == "si" ):
        return calculadora()
    elif( opcOperacion == "no" ):
        if(p == "suma"):
            return suma()
        elif(p == "resta"):
            return resta()
        elif(p == "multiplicacion"):
            return multiplicacion()
        elif(p == "division"):
            return division()
        elif(p == "raiz"):
            return raiz()
        elif(p == "potenciacion"):
            return potenciacion()
        elif(p == "logaritmo"):
            return logaritmo()
        elif(p == "sin"):
            return sin()
        elif(p == "cos"):
            return cos()
        elif(p == "tan"):
            return tan()
        elif(p == "tm"):
            return tm()
        elif(p == "td"):
            return td()
    else:
        print("opcion incorecta vuelva intentar...")    

def suma():
    num1 = float(input("numero 1: ")) 
    num2 = float(input("numero 1: "))
    suma = num1 + num2
    print("resultado: " + str(suma))
    p = "suma"
    devolverOperacion(p)
def resta():
    num1 = float(input("numero 1: ")) 
    num2 = float(input("numero 1: "))
    resta = num1 - num2
    print("resultado: " + str(resta))
    p = "resta"
    devolverOperacion(p)
def multiplicacion(): 
    num1 = float(input("numero 1: ")) 
    num2 = float(input("numero 1: "))
    multiplicacion = num1 * num2
    print("resultado: " + str(multiplicacion))
    p = "multiplicacion"
    devolverOperacion(p)
def division():
    num1 = float(input("numero 1: ")) 
    num2 = float(input("numero 1: "))
    division = num1 / num2
    print("resultado: " + str(division))    
    p = "division"
    devolverOperacion(p)
def raiz():
    num1 = float(input("Ingrese numero: "))
    raiz = math.sqrt(num1)
    print("resultado: " + str(raiz))
    p = "raiz"
    devolverOperacion(p)
def exponente():
    # numero al que vas a elevar 
    num1 = float(input("Ingrese numero base: "))
    num2 = float(input("Ingrese numero exponente: "))
    potenciacion = num1 ** num2
    print("resultado: " + str(potenciacion))
    p = "exponente"
    devolverOperacion(p)
def log():
    num1 = float(input("Ingrese numero: "))
    log = math.log10(num1)
    print("resultado: " + str(log))   
    p = "log"
    devolverOperacion(p) 
def sin():
    num1 = float(input("Ingrese numero: "))
    sin = math.sin(num1)
    print("resultado: " + str(sin))   
    p = "sin"
    devolverOperacion(p)
def cos():
    num1 = float(input("Ingrese numero: "))
    cos = math.cos(num1)
    print("resultado: " + str(cos))   
    p = "cos"
    devolverOperacion(p)
def tan():
    num1 = float(input("Ingrese numero: "))
    tan = math.tan(num1)
    print("resultado: " + str(tan))   
    p = "tan"
    devolverOperacion(p)
def tm():
    # numero a multiplicaar
    num = float(input("Ingrese numero a multiplicaar: "))
    # cantidad a multiplicar
    cant = int(input("Ingrese numero de cantidad: "))
    for i in range(1, cant + 1):
        print( str(num) + " x " + str(i) + " = " + str(num * i))
    p = "tm"
    devolverOperacion(p)
def td():
    # numero a multiplicaar
    num = float(input("Ingrese numero a multiplicaar: "))
    # cantidad a multiplicar
    cant = int(input("Ingrese numero de cantidad: "))
    for i in range(1, cant + 1):
        print( str(num) + " x " + str(i) + " = " + str(num / i))
    p = "td"
    devolverOperacion(p)
def opcIncorrecto():
    print("Opcion Incorrecto...")      




# x va a representar una variable global que declare falso y verdadero en el bucle
def calculadora():
    x = True
    while x == True:
        # opciones a imprimir
        infoCalculadora = """
        ########################################## 
                        calculadora 
        ##########################################


        Opciones calculadora:

        1. suma
        2. resta
        2. multiplicacion
        4. division
        5. raiz
        6. potenciacion
        7. logaritmo
        8. sin
        9. cos
        10. tan
        11. tablas de mutiplicacion 
        12. tablas de division


        Enter para salir...
        """
        print(infoCalculadora)
        # llamada de opcion
        opc = str(input("Seleccione Opcione: "))
        # sentencias    
        if(opc == "1"):
            suma()
        elif(opc == "2"):
            resta()
        elif(opc == "3"):
            multiplicacion()
        elif(opc == "4"):
            division()
        elif(opc == "5"):
            raiz()
        elif(opc == "6"):
            exponente()
        elif(opc == "7"):
            log()
        elif(opc == "8"):
            sin()
        elif(opc == "9"):
            cos()
        elif(opc == "10"):
            tan()
        elif(opc == "11"):
            tm()
        elif(opc == "12"):
            td()
        elif (opc == "salir"): 
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S")
            print(time_string)
            time.sleep(3)
            os.system('cls')
            sys.exit()
        else:
            opcIncorrecto()
calculadora()