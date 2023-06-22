### Práctica 3. Gramáticas independientes del contexto  ###
### Farrera Mendez Emmanuel Sinai ###
### Teoria Computacional ####

#Estrutura del Automata de Pila
class automata_pila: 

    def __init__(self, cadena):
        self.cadena = cadena #self hace referencia a un objeto
        self.pila= [] #Arreglo del Automata de Pila

#Elementos de la Gramatica
    def gramatica(self):
        operadores= ['+', '-', '*', '/', '%'] 
        masomenos = ['+', '-'] 
        self.estado = 'q0' #Estado inicial 

        for i in range(0, len(self.cadena)): #Recorre la cadena a validar
            #Recorre cada simbolo de la cadena para cambiara de transicion de acuerdo a la funcion de transferencia
            self.transicion = self.cadena[i]

            #Estado q0
            if self.estado == 'q0': #Simbolo inicial de la Pila
                if self.transicion.isalpha(): #Comprueba si el símbolo es alfanumérico
                    self.estado = 'q1' # Cambia al estado q1
                else:
                    break #Sale del bucle si el símbolo no cumple con las condiciones anteriores

            #Estado q1
            elif self.estado == 'q1': #Estado Inicial
                # Funciones de Transferencia de q1
                if self.transicion.isalnum(): # Comprueba si el símbolo es alfanumérico
                    self.estado = 'q1' #se mantiene en el estado q1
                elif self.transicion == '=': #Comprueba si el símbolo es un signo igual
                    self.estado = 'q2' #Cambia al estado q2
                else:
                    break #Sale del bucle si el símbolo no cumple con las condiciones anteriores

            #Estado q2
            elif self.estado == 'q2':
                # Funciones de Transferencia de q2
                if self.transicion == '(': # Comprueba si el símbolo es un paréntesis abierto
                    self.pila.append('(')  # Agrega el paréntesis a la pila
                    self.estado = 'q2' # Se mantiene en el estado q2
                elif self.transicion.isalpha(): # Comprueba si el símbolo es una letra
                    self.estado = 'q3' # Cambia al estado q3
                elif self.transicion.isdigit(): # Comprueba si el símbolo es un dígito
                    self.estado = 'q4' # Cambia al estado q4
                elif self.transicion in masomenos:# Comprueba si el símbolo es un símbolo de más o menos
                    self.estado = 'q3' # Cambia al estado q3
                else:
                    break # Sale del bucle si el símbolo no cumple con las condiciones anteriores

            #Estado q3
            elif self.estado == 'q3':
                # Funciones de Transferencia de q3
                if self.transicion.isalnum(): # Comprueba si el símbolo es alfanumérico
                    self.estado = 'q3' # Se mantiene en el estado q3
                elif self.transicion == '(': # Comprueba si el símbolo es un paréntesis abierto
                    self.pila.append('(') # Agrega el paréntesis a la pila
                    self.estado = 'q3' # Se mantiene en el estado q3
                elif self.transicion == ';': # Comprueba si el símbolo es un punto y coma
                    self.estado = 'q6' # Estado de Aceptación
                elif self.transicion == ')': # Comprueba si el símbolo es un paréntesis cerrado
                    self.pila.pop() # Elimina el paréntesis de la pila
                    self.estado = 'q5' # Cambia al estado q5
                elif self.transicion in operadores:# Comprueba si el símbolo es uno de los operadores definidos
                    self.estado = 'q2' # Cambia al estado q2
                else:
                    break # Sale del bucle si el símbolo no cumple con las condiciones anteriores


            #Estado q4
            elif self.estado == 'q4':
                # Funciones de Transferencia de q4
                if self.transicion.isdigit(): # Comprueba si el símbolo es un dígito
                    self.estado = 'q4' # Se mantiene en el estado q4
                elif self.transicion in operadores: # Comprueba si el símbolo es uno de los operadores definidos
                    self.estado = 'q2' # Cambia al estado q2
                elif self.transicion == ')': # Comprueba si el símbolo es un paréntesis cerrado
                    self.pila.pop() # Elimina el paréntesis de la pila
                    self.estado = 'q5' # Cambia al estado q5
                elif self.transicion == ';': # Comprueba si el símbolo es un punto y coma
                    self.estado = 'q6' #Estado de Aceptacion
                else:
                    break # Sale del bucle si el símbolo no cumple con las condiciones anteriores

            #Estado q5
            elif self.estado == 'q5':
                # Funciones de Transferencia de q5
                if self.transicion in operadores: # Comprueba si el símbolo es uno de los operadores definidos
                    self.estado = 'q2' # Cambia al estado q2
                elif self.transicion == ')': # Comprueba si el símbolo es un paréntesis cerrado
                    self.pila.pop() # Elimina el paréntesis de la pila
                    self.estado = 'q5' # Se mantiene en el estado q5
                elif self.transicion == ';': # Comprueba si el símbolo es un punto y coma
                    self.estado = 'q6' # Estado de Aceptación
                else:
                    break # Sale del bucle si el símbolo no cumple con las condiciones anteriores

        if not self.pila and self.estado == 'q6': #verifica si la pila esta vacia y si estamos en el estado de aceptación. 
            return True



def main():
    print("Práctica 3. Gramáticas independientes del contexto")
    print("Gramatica independiente del contexto para validar expresiones del lenguaje de programación C")
    w = input("Introduzca la cadena para validar: ")#Se introduce la cadena a evaluar. 
    validar_cadena = automata_pila(w)  #Crea una instancia de la clase automataPila y pasa la cadena para validarla. 
    if validar_cadena.gramatica() == True: #Si el retorno es true, la cadena es valida. 
        print('Cadena Válida')
    else:
        print('Cadena No Válida') #Si no se cumple, la cadena no es valida. 

if __name__ == "__main__":  # Verifica si el archivo se está ejecutando directamente
    main()
    
    
    
'''
Gramatica = {ST, SNT, A, RP}
ST={a, b, c, d, e, f, g, h, i, j, k, l, m, n,o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, +, -, /, %, *, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, =, ;}

SNT={X1, X2, X3, X4} 
A = X1; 
RP={    X1 -> X3 = X2;
        X2 -> X3 | X4 | X2 + X2 | X2 - X2 | X2 / X2 | X2 * X2 | X2 % X2 | (X2)  
        X3 -> a | ... | z |  A | ... | Z | X3 X3 | X2 X4 |X2 X4 X2
        X4 -> 0|..|9 | X4 X4 }
'''
