### Práctica 1. Alfabetos, lenguajes y expresiones regulares  ###
### Farrera Mendez Emmanuel Sinai ###
### Teoria Computacional ####


import string
import random
import re

alfa1 = []
salidapow = []
invert = []


### 2. Comprobar elementos de el Alfabeto ###


def comprobar(w1, lista):
    cont = 0
    for i in range(len(w1)): #El ciclo se va a repetir un numero de veces igual a la longitud de W1. 
        for j in range(len(lista)): #El ciclo se va a repetir un numero de veces igual a la longitud de lista. 
            if (w1[i] == lista[j]): #verificamos que todos los elementos de w1 se encuentren en lista. 
                cont = cont + 1 #añade uno a cont cada vez que un caracter coincide. 
    if (cont == len(w1)): #solo si la longitud de w1 es igual al numero de coincidencias la cadena es valida. 
        # print(f'La cadena {w1} es válida')
        return True
    else:
        # print(f"La cadena {w1} es inválida")
        return False


### 3. Prefijo o sufijo (propio o no propio), o subcadena, o subsecuencia ###


def pre_sub(w1, w2):
    if ((w1 or w2) == '') or ((w1 and w2) == ''):
        print("Una o las dos cadenas estan vacías")  # Verifica si ambas o solo una cadena estan vacias. 
    elif w1 == w2: 
        print("Las 2 cadenas son iguales \n") #Valida si ambas cadenas estan vacias. 

    # Valida Existencia del elemento neutro
    # Al principio
    if w1[0] == 'λ': #primera posicion de la lista es el elemento λ
        if (w2 == (w1[1:])) == True:
            print("Las cadenas son iguales\n")
    # Al final
    elif w1[-1] == 'λ': #ultima posicion de la lista es el elemento λ
        if (w2 == (w1[:-1])) == True:
            print("Las cadenas son iguales\n")

    # Valida que este dentro de la otra cadena (Subcadena Propia)
    if w1 != w2: #Verifica que las cadenas no sean iguales. 
        if (w1 in w2) and ((w1 and w2) != ''): #verifica que w1 este en w2 y que no sean vacias. 
            print("La cadena 1 es subcadena propia de la cadena 2\n")

    # Valida que este dentro de la otra cadena incluyendo λ (Subcadena)
    if ((w1[0] == 'λ') or (w1 in w2)) and ((w1 and w2) != ''): 
        print("La cadena 1 es subcadena no propia de la cadena 2\n")

    # Valida si comienza la cadena 2 igual que la cadena 1 (Prefijo)
    if (w2.startswith(w1) == True) and ((w1 and w2) != ''): 
        print("La cadena 1 es prefijo no propio de la cadena 2\n")

    # Valida si termina la cadena 2 igual que la cadena 1 (Sufijo)
    if (w2.endswith(w1) == True) and ((w1 and w2) != ''): #Verifica que w2 termine con w1 y que no sean vacias.
        print("La cadena 1 es sufijo no propio de la cadena 2\n")

    # Valida si alfa se encuentra en la posicion[0] y omite esta (Prefijo)
    if w1[0] == 'λ':
        if w2.startswith(w1[1:]) == True: #Verifica que w2 empize con w1. 
            print("La cadena 1 es prefijo no propio de la cadena 2\n")

    # Valida si alfa se encuentra y omite esta que esta al ultimo (Sufijo)
    if w1[-1] == 'λ':
        if w2.endswith(w1[:-1]) == True:
            print("La cadena 1 es sufijo no propio de la cadena 2\n")

    # Valida si comienza la cadena 2 igual que la cadena 1 (Prefijo propio misma palabra)
    if w1 != w2:
        if w1[0] != 'λ':
            if (w2.startswith(w1) == True) and ((w1 and w2) != ''):
                print("La cadena 1 es prefijo propio de la cadena 2\n")

    # Valida si termina la cadena 2 igual que la cadena 1 (Sufijo propio misma palabra)
    if w1 != w2:
        if w1[-1] != 'λ':
            if (w2.endswith(w1) == True) and ((w1 and w2) != ''):
                print("La cadena 1 es sufijo propio de la cadena 2\n")

    # Funcion iterativa para verificar si una cadena es subsecuencia de otra cadena
    def subsecuencia(w1, w2):
        # Indica la cantidad de caracteres en la cadena
        m = len(w1)
        n = len(w2)

        # Iniciamos j e i en 0
        j = 0  # Index of str1
        i = 0  # Index of str2

        """
        Atraviesa tanto la cadena 1 como la cadena 2
        Compara el carácter actual de la cadena 2 con primer carácter de la de cadena 1
        Si coincide, entonces avanza en la cadena 1
        """
        while j < m and i < n:
            if w1[j] == w2[i]:
                j = j + 1
            i = i + 1

        # Si todos los caracteres de la cadena 1 coinciden, entonces j es igual a m
        return j == m

    if subsecuencia(w1, w2):
        print("La cadena 1 es subsecuencia de la cadena 2")


### 4. Generacion de Lenguajes y 5. Diferencia de lenguajes ###


def generar_lenguajes(alfa1):
    print("\nGeneración de los Lenguaje L1 y L2")

    L1 = []
    palabras = int(input("\nIngrese el número de palabras a ser generados (Lenguaje L1): "))  # Numero de palabras a ingresar L1

    longitud = int((input("Ingrese la longitud de la palabra generada: (Lenguaje L1): ")))  # Longitud de las palabras L1

    # Bucle for para recorrer mediante la funcion range la cantidad de palabras a generar
    for i in range(palabras):
        # Metodo join para unir los elementos de alfa 1 en una sol cadena
        # Metodo randomchoice. nos devuelve elemntos de la lista(Alfabeto) al azar
        L1.append(''.join(random.choice(alfa1) for i in range(longitud)))  # Bucle For para ver cuando termina la palabra

    print("\nLenguaje L1: ")
    print(L1)  # Y continua con la siguiente

    L2 = []

    palabras2 = int(input("\nIngrese el número de palabras a ser generados(Lenguaje L2): "))  # Numero de palabras a ingresar L2
    longitud2 = int((input("Ingrese la longitud de la palabra generada(Lenguaje L2): ")))  # Longitud de las palabras L2

    # Bucle for para recorrer mediante la funcion range la cantidad de palabras a generar
    for n in range(palabras2):
        # Metodo join para unir los elementos de alfa 1 en una sol cadena
        # Metodo randomchoice. nos devuelve elementos de la lista(Alfabeto) al azar
        L2.append(''.join(random.choice(alfa1) for _ in range(longitud2)))  # Bucle For para ver cuando termina la palabra
        # Y continua con la siguiente

    print("\nLenguaje L2:")
    print(L2)

    LD1 = []
    LD2 = []

    # Bucle For que va recorrer la lista L1
    for i in L1:
        if i not in L2:  # Verifica que el elementos no esten en la liata L2
            LD1.append(i)  # Agrega los elementos que no estan a la lista L2
    print("\nLa Diferencia de los Lenguajes L1-L2 es: ")
    print(LD1)

    # Bucle For que va recorrer la lista L2
    for i in L2:
        if i not in L1:  # Verifica que el elementos no esten en la liata L1
            LD2.append(i)  # Agrega los elementos que no estan a la lista L1
    print("\nLa Diferencia de los lenguajes L2-L1 es:")
    print(LD2)


### 6. Potencia del alfabeto ###


def potencia_alfabeto(alfa1):
    print("\nEl valor de la potencia es un número entero (rango: -5 a 5)")
    pow = int(input("\nIngrese la potencia del Alfabeto ∑1: "))

    if pow == 0:
        return set(['λ'])

    # Si la potencia es mayor a 0, generar el conjunto de cadenas
    elif 1<= pow <=5:
        result = set(['']) #Creamos una cadena vacia 
        for i in range(pow):#ciclo que se ejecuta pow veces 
            new_result = set() #en cada iteracion crea un conjunto vacio que vamos a rellenar con las cadenas generadas en esa iteracion.  
            for s in result: #Agrega todas las posibles combinaciones de alfa1 
                for c in alfa1:
                    new_result.add(s + c) #concatena las cadenas a la cadena new_result generada en ese momento.  
            result = new_result #actualiza result con todas las cadenas que se han ido guardando en new_result. 
        return result
    
    elif pow < 0 and pow >= -5:
        pow1 = abs(pow)
        result = set([''])
        for i in range(pow1):
            new_result = set()
            for s in result:
                for c in alfa1: 
                    new_result.add(c + s) # Invierte la cadena concatenando el nuevo carácter al principio
            result = new_result          
        return result
    
    else: print("\n\nIngrese un valor correcto")
    
###-------7. Expresiones regulares----------###
    
def eval_string(x:str):
    return re.match('^\d+$', x) is not None #verifica que la cadena esta formada por 1 o mas digitos. 

def expresiones_regulares():
    print("B) Todas las cadenas de dígitos que tengan por lo menos un dígito repetido. Los dígitos no tienen que estar en orden") 
    palabra=str(input("Escriba una palabra a analizar "))
    if eval_string(palabra):
        result = re.findall(r'(.)(?=.+\1)', palabra) #verifica que se encuentra un digito repetido.  
        if len(result)>0:   #verifica que el resultado sea valido y tenga al menos un digito repetido. 
                print("Palabra correcta") 
        else:
                print("Palabra incorrecta")
    else:
            print("Palabra incorrecta")

###-------1. Funcion principal----------###

while True:
    datos = input('\r\nIndica como vas a ingresar datos en el alfabeto: \r\n1.-Individual \r\n2.-Rango\r\n3.-Expresion\r\n4.-Si quiere terminar con el programa escriba "Salir"\r\n') #Como se van a introducir los caracteres del alfabeto. 
    
    if (datos == "Individual") or (datos == "individual") or (datos == "1"): #Se introducen los datos manera indivudual. 
        elementos = int(input('Ingresa cuantos elementos contendra el alfabeto: '))

        for i in range(elementos):
            x = input('Ingresa elementos: ') #concatena los datos en la lista alfa1
            alfa1.append(x)

        simbolo = all(len(alfa1) >= 1 for x in alfa1) #verifica que la lista tenga al menos un elemento. 

        if simbolo:
            print(f'\r\nUsted ingreso el numero de simbolos indicados') #Confirmacion de exito en la cadena. 
            print(f'\r\nUsted ingreso {len(alfa1)} elementos')#Cuantos elementos tiene la cadena
            print(f'Alfabeto: E={alfa1}')#alfabeto

            cadena1 = input('Ingresa la primera cadena: \r\n')#ingresamos la cadena uno y dos. 
            cadena2 = input('Ingresa la segunda cadena: \r\n')

            while True:
                if comprobar(cadena1, alfa1) == False and comprobar(cadena2, alfa1) == True: #Caso donde la cadena 1 es incorrecta y la vuelve a pedir 
                    cadena1 = input('Ingresa la primera cadena: ')
                elif comprobar(cadena1, alfa1) == True and comprobar(cadena2, alfa1) == False: #Caso donde la cadena 2 es incorrecta y la vuelve a pedir
                    print("Cadena incorrecta, vuele a ingresar la cadena 2")
                    cadena2 = input('Ingresa la segunda cadena: ')
                elif comprobar(cadena1, alfa1) == False and comprobar(cadena2, alfa1) == False: #Caso donde ambas cadenas con incorrectas y las vuelve a pedir.
                    print("Cadenas incorrectas, vuele a ingresar la cadena 1 y 2") 
                    cadena1 = input('Ingresa la primera cadena: \r\n')#ingresamos de nuevo la cadena uno y dos. 
                    cadena2 = input('Ingresa la segunda cadena: \r\n')
                elif comprobar(cadena1, alfa1) == True and comprobar(cadena2, alfa1) == True: #acepta las cadenas si no hay ningun problema. 
                    print("Cadenas aceptadas.")
                    print("Cadena 1: " + cadena1)
                    print("Cadena 2: " + cadena2)
                    pre_sub(cadena1, cadena2) #Llamamos a la funcion 3 que se encarga de definir si 1 es un prefijo o sufijo (propio o no propio), o subcadena, o subsecuencia de 2
                    generar_lenguajes(alfa1) #Funcion que genera los lenguajes y calcula las diferencias entre ellos 4 y 5. 
                    print(potencia_alfabeto(alfa1)) #Calcula la potencia del alfabeto.  
                    alfa1.clear()
                    break
        else:
            print(f'Usted no ingreso el numero de simbolos indicados')
            print(alfa1)
            exit

    if (datos == "Rango") or (datos == "rango") or (datos == "2"):
        # Entrada de los simbolos por rangos
        x = input("Introduzca el  primer  símbolo  del  alfabeto  a  definir: ")
        y = input("Introduzca el  ultimo símbolo  del  alfabeto  a  definir: ")

        # Funcion Ord recibe un caracter y devuelve su representación como codigo ASCII
        inicio = ord(x)

        # Ciclo for para recorrer la cantidad de elementos a agregar
        for i in range(ord(y) - inicio + 1):  # Range marca el inicio y el final de los caracteres a insertar
            alfa1.append(chr(inicio + i))  # Función chr recibe un número y devuelve su representación como carácter.

        print(f'Alfabeto en rango es: {alfa1}')  # Imprime el alfabeto en rango

        # Ingreso de las cadenas
        cadena1 = input('Ingresa la primera cadena: \r\n')
        cadena2 = input('Ingresa la segunda cadena: \r\n')
        while True:
            '2.-Validar cadenas'
            if comprobar(cadena1, alfa1) == False and comprobar(cadena2, alfa1) == True:
                print("Cadena incorrecta, vuele a ingresar la cadena 1")
                cadena1 = input('Ingresa la primera cadena: ')
            elif comprobar(cadena1, alfa1) == True and comprobar(cadena2, alfa1) == False:
                print("Cadena incorrecta, vuele a ingresar la cadena 2")
                cadena2 = input('Ingresa la segunda cadena: ')
            elif comprobar(cadena1, alfa1) == False and comprobar(cadena2, alfa1) == False: 
                    print("Cadenas incorrectas, vuele a ingresar la cadena 1 y 2") 
                    cadena1 = input('Ingresa la primera cadena: \r\n')
                    cadena2 = input('Ingresa la segunda cadena: \r\n')
            elif comprobar(cadena1, alfa1) == True and comprobar(cadena2, alfa1) == True:
                print("Cadenas aceptadas.")
                print("Cadena 1: " + cadena1)
                print("Cadena 2: " + cadena2)
                print('\n')
                pre_sub(cadena1, cadena2)
                generar_lenguajes(alfa1)
                print(potencia_alfabeto(alfa1))
                alfa1.clear()
                break
    if (datos == "Expresion") or (datos == "expresion") or (datos == "3"): 
        expresiones_regulares()

    if (datos != "Individual") and (datos != "Rango") and (datos != "individual") and (datos != "rango") and (datos != "Salir") and (datos != "salir") and (datos != "2") and (datos != "1") and (datos != "3") and (datos != "Expresion") and (datos != "expresion") and (datos != "4"):
        print("Vuelve intentarlo, escribe de manera correcta") # validar que la seleccion sea correcta. 
    if (datos == "Salir") or (datos == "salir") or (datos == "4"): #romper el ciclo una vez se seleccione salir
        break