### Práctica 2. Analizador Lexico  ###
### Farrera Mendez Emmanuel Sinai ###
### Teoria Computacional ####

import shutil #Modulo usado para manipular archivos. 
        
class Automata: #automata encargado del analisis. 

    def __init__(self,texto): #Constructor de la clase Automata.
        self.texto=texto #parámetro texto que se utilizará para asignar un valor al atributo texto. 
    def analizador_lexico(self):  
        numeros = ['1', '2', '3','4','5','6','7','8','9'] #decimales del 1 al 9
        octa_list = ['0','1','2', '3','4','5','6','7']  #octales del 0 al 7
        hexa = ['A','B','C', 'D','E','F']   #hexadecimales de la A a la F

        self.estado='inicio' # Asigna el valor 'inicio' al atributo 'estado' de la instancia actual. 
        for i in range(0,len(self.texto)):
            self.transicion=self.texto[i] #Asigna el carácter en la posición i de 'texto' de la instancia actual (self) al atributo 'transicion'
                
             ##Estado inicial
            if self.estado == "inicio":
                if self.transicion in numeros: # Si la transición es un número, el estado pasa a ser "entero"
                    self.estado="entero"
                elif self.transicion=='+' or self.transicion=='-': # Si la transición es "+" o "-", el estado pasa a ser "signo"
                    self.estado="signo" 
                elif self.transicion=='0':   # Si la transición es "0", el estado pasa a ser "Cero"
                    self.estado="Cero"  
                elif self.transicion=='/': # Si la transición es "/", el estado pasa a ser "comen_0"
                    self.estado="comen_0"      
                elif self.transicion.isalpha()  or self.transicion=='_' or self.transicion=='$': # Si la transición es alfabética, "_" o "$", el estado pasa a ser "est_1"
                    self.estado="est_1"                      
                else:
                    return False

            ##Estado 'entero'    
            elif self.estado =="entero": 
                if self.transicion == '.':   # Si la transición es ".", el estado pasa a ser 'dec_p_e'
                  self.estado='dec_p_e'    
                elif str.isdigit(self.transicion): # Si la transición es un dígito, el estado sigue siendo 'Decimal'
                  self.estado='Decimal' 
                else: 
                    return False # Si ninguna condición se cumple, se devuelve False (error léxico)
                
            ##Estado 'dec_c_p'    
            elif self.estado =="dec_c_p": 
                if str.isdigit(self.transicion): # Si la transición es un dígito, el estado pasa a ser 'decimal_p'
                  self.estado='decimal_p' 
                else: 
                    return False # Si ninguna condición se cumple, se devuelve False (error léxico)

        
            ##Estado 'Decimal'    
            elif self.estado =="Decimal": # Si la transición es ".", el estado pasa a ser 'dec_c_p'
                if self.transicion == '.':
                  self.estado='dec_c_p'  
                elif str.isdigit(self.transicion): # Si la transición es un dígito, el estado sigue siendo 'Decimal'
                  self.estado='Decimal' 
                else: 
                    return False
                
            ##Estado 'dec_p_e'    
            elif self.estado =='dec_p_e':  
                if str.isdigit(self.transicion):   # Si la transición es un dígito, el estado pasa a ser 'decimal_e1'
                  self.estado='decimal_e1'      
                else: 
                    return False # Si ninguna condición se cumple, se devuelve False (error léxico)

            
            ##Estado 'decimal_p'    
            elif self.estado =='decimal_p':   # Si la transición es un dígito, el estado sigue siendo 'decimal_p'
                if str.isdigit(self.transicion):
                  self.estado='decimal_p' 
                else: 
                    return False    # Si ninguna condición se cumple, se devuelve False (error léxico)
                
            ##Estado 'decimal_e1'    
            elif self.estado =='decimal_e1':  # Si la transición es un dígito, el estado sigue siendo 'decimal_e1'
                if str.isdigit(self.transicion): 
                  self.estado='decimal_e1' 
                elif self.transicion=='E':  # Si la transición es 'E', el estado pasa a ser 'E'
                  self.estado='E'                   
                else: 
                    return False # Si ninguna condición se cumple, se devuelve False (error léxico)          
                
            ##Estado 'signo'    
            elif self.estado =='signo':  # Si la transición es un número, el estado pasa a ser 'entero'
                if self.transicion in numeros:
                  self.estado='entero'
                elif self.transicion == '0':  # Si la transición es '0', el estado pasa a ser 'Cero'
                  self.estado='Cero'   
                elif self.transicion == 'i':  # Si la transición es 'i', el estado pasa a ser 'i_mas_menos'
                  self.estado='Cero'
                else: 
                    return False     # Si ninguna condición se cumple, se devuelve False (error léxico)
                
            ##Estado 'est_2'    
            elif self.estado =='est_2': # Si la transición es un dígito, el estado pasa a ser 'decimal_e0'
                if str.isdigit(self.transicion):
                  self.estado='decimal_e0'  
                else: 
                    return False    # Si ninguna condición se cumple, se devuelve False (error léxico)
                
            ##Estado 'decimal_e0'    
            elif self.estado =='decimal_e0': # Si la transición es un dígito, el estado sigue siendo 'decimal_e0'
                if str.isdigit(self.transicion):
                  self.estado='decimal_e0' 
                elif self.transicion=='E': # Si la transición es 'E', el estado pasa a ser 'E'
                  self.estado='E'                    
                else: 
                    return False    # Si ninguna condición se cumple, se devuelve False (error léxico)

                
            ##Estado 'cero'    
            elif self.estado =='Cero': 
                if self.transicion =='.': # Si la transición es '.', el estado pasa a ser 'est_2'
                  self.estado='est_2' 
                elif self.transicion in octa_list: # Si la transición es un dígito octal, el estado pasa a ser 'Octal'
                  self.estado='Octal'  
                elif self.transicion=='X'or self.transicion=='x': # Si la transición es 'X' o 'x', el estado pasa a ser 'est_3'
                  self.estado='est_3'                    
                else: 
                    return False   # Si ninguna condición se cumple, se devuelve False (error léxico)
                
             ##Estado 'E'
            elif self.estado =='E':
                if self.transicion=='+' or self.transicion=='-':      # Si la transición es '+' o '-', el estado pasa a ser 'signo_1'
                    self.estado='signo_1'
                elif str.isdigit(self.transicion):  # Si la transición es un dígito, el estado pasa a ser 'e_1'
                    self.estado='e_1'
                else: 
                    return False  # Si ninguna condición se cumple, se devuelve False (error léxico)
                
            ##Estado 'Octal'  
            elif  self.estado=='Octal':
                if self.transicion in octa_list: # Si la transición es un dígito octal, el estado sigue siendo 'Octal'
                    self.estado='Octal'
                else :
                    return False # Si la transición no es un dígito octal, se devuelve False (error léxico)
                
             ##Estado 'e_1'
            elif self.estado =='e_1':
                if str.isdigit(self.transicion): # Si la transición es un dígito, el estado pasa a ser 'decimal_p'
                    self.estado='decimal_p'
                else: 
                    return False # Si la transición no es un dígito, se devuelve False (error léxico)
                
              ##Estado 'signo_1'
            elif self.estado =='signo_1':              
                if str.isdigit(self.transicion):  # Si la transición es un dígito, el estado pasa a ser 'e_1'
                    self.estado='e_1'
                else: 
                    return False  # Si la transición no es un dígito, se devuelve False (error léxico)

            ##Estado 'est_3'    
            elif self.estado =='est_3':
                if str.isdigit(self.transicion) or self.transicion in hexa: # Si la transición es un dígito o está en el conjunto de caracteres hexadecimales, el estado pasa a ser 'Hexadecimal
                  self.estado='Hexadecimal'                     
                else:
                  return False # Si la transición no es un dígito ni está en el conjunto hexadecimal, se devuelve False (error léxico)

            ##Estado 'Hexadecimal'          
            elif self.estado =='Hexadecimal': # Si la transición es un dígito o está en el conjunto de caracteres hexadecimales, el estado sigue siendo 'Hexadecimal'
                if str.isdigit(self.transicion) or self.transicion in hexa:
                  self.estado='Hexadecimal' 
                else:
                 return False  # Si la transición no es un dígito ni está en el conjunto hexadecimal, se devuelve False (error léxico)

            ##Estado 'comen_0'          
            elif self.estado =='comen_0': # Si la transición es '*', el estado pasa a ser 'comen_1'
                if self.transicion=='*':
                    self.estado='comen_1' 
                elif self.transicion=='/': # Si la transición es '/', el estado pasa a ser 'comentario_s'
                   self.estado='comentario_s'
                else: 
                    return False # Si la transición no es '*' ni '/', se devuelve False (error léxico)
                
            ##Estado 'comen_1'          
            elif self.estado =='comen_1':  # Si la transición es '*', el estado pasa a ser 'est_0'
                if self.transicion=='*':
                    self.estado='est_0'
                else: 
                    self.estado='comen_1' # Si la transición no es '*', el estado sigue siendo 'comen_1'
                
            ##Estado 'est_0'          
            elif self.estado =='est_0':
                if self.transicion=='/':  # Si la transición es '/', el estado pasa a ser 'comentario_as'
                    self.estado='comentario_as' 
                else: 
                    return False  # Si la transición no es '/', se devuelve False (error léxico)
                
            ## Estado 'comentario_s'
            elif self.estado =='comentario_s':   # Si el estado es 'comentario_s', se devuelve True para indicar que es un comentario válido
                return True

            
            ##Estado 'est_1'          
            elif self.estado =='est_1':
                if self.transicion.isalnum() or self.transicion=='_' or self.transicion=='$':  # Si la transición es alfanumérica, '_', o '$', el estado se mantiene como 'est_1'
                    self.estado='est_1'
         
                else: 
                   return False  # Si la transición no cumple con las condiciones anteriores, se devuelve False (error léxico)
            
            ##Estado 'i_mas_menos'          
            elif self.estado =='i_mas_menos':  # Si la transición es '*', el estado pasa a ser 'est_0'
                    return True

           
            else:
              return False   # Si ninguna de las condiciones anteriores se cumple, se devuelve False (error léxico)       
        
        if self.estado=="decimal_p":
            return True
        elif self.estado=="decimal_e1":
            return True    
        elif self.estado=="decimal_e0":
            return True        
        elif self.estado=="Decimal":
            return True
        elif self.estado=="Octal":
            return True
        elif self.estado=="decimal_p":
            return True               
    
        elif self.estado=="Hexadecimal":
            return True 
        elif self.estado=="comentario_s":
            return True
        elif self.estado=="comentario_as":
            return True 
        elif self.estado=="entero":
            return True 
        elif self.estado=="est_1":
            return True         
        elif self.estado=="comen_1":
            return False             

def main(): #funcion principal 

    count = 0 #encargado de contar las lineas
    b=0 #bandera encargada de indicar cuando se encuentra un error. 
    
    archivos() #funcion encargada de tomar el archivo original y tranformarlo a un txt quitando los caracteres especiales. 
    
    with open('archivo_copia.txt','r') as file: #abre el archivo en modo lectura. 
        
     for line in file: #encargado de recorrer cada linea del archivo. 
         
        count=count+1 #incrementa el contador de las lienas. 
        
        for word in line.split(): #encargado de revisar cada palabra de cada linea. 
            
            if palabras_reservadas(word)==False : #verifica si la palabra es reservada

               AFD=Automata(word) #creamos una instancia en la clase automata para llevar a cabo el analisis con el automata. 
         
               if AFD.analizador_lexico() == False: #si el analzador lexico retorna un falso agrega uno a b. 
                b=1   
                print("Error en la linea " + str(count)) # Si b es igual a toma el numero de linea de count y lo hace un string para concatenarlo a Error en la linea.  
            
    if b!=1: #si b es diferente de uno significa que no encontro errores e imprime eso. 
     print("No se han encontrado errores gramaticales en el archivo")   
     
def archivos(): #funcion encargada de tomar el archivo original y tranformarlo a un txt quitando los caracteres especiales. 
    
    original = 'Ejemplo.java' #archivo original. 
    target = 'archivo_copia.txt' #archivvo donde se hace la copia. 

    shutil.copyfile(original, target) #funcion que hace la copia de los datos del original a la copia.  
    
    with open('archivo_copia.txt', 'r') as file :#abre el archivo en modo lectura. 
     filedata = file.read() #lee el contenido completo del archivo y lo almacena en la variable "filedata"
     
    filedata = filedata.replace(';',' ') #utiliza la funcion .replace para cambiar todos los caracteres especiales por espacios ya que no nos importan al momento de hacer el analisis lexico. 
    filedata = filedata.replace(',',' ')  
    filedata = filedata.replace(':',' ')  
    filedata = filedata.replace('=',' ')  
    filedata = filedata.replace('(',' ')  
    filedata = filedata.replace(')',' ')
    filedata = filedata.replace('{',' ')
    filedata = filedata.replace('>',' ') 
    filedata = filedata.replace('<',' ')   
    filedata = filedata.replace('}',' ') 
    filedata = filedata.replace('[',' ') 
    filedata = filedata.replace(']',' ')  
    filedata = filedata.replace('"',' ')          
    
    with open('archivo_copia.txt', 'w') as file: #abre el archivo en modo escritura. 
     file.write(filedata)    #ocupa la funcion .write para escribir en el archivo_copia todo lo que se guardo en filedata. 

def palabras_reservadas(word): #se encarga de revisar las palabras reservadas de java 
  with open('palabras_reservadas.txt') as file:  #abre el archivo palabras_reservadas como file  
    contents = file.read() #guarda en contents lo que hay con el archivo con la funcion file.read. 
  if word in contents: #verficica si word esta en lo que se guardo en contents y verifica si esta.
    return True  #devuelve True si la palabra es una palabra reservada
  else:
    return False  #devuelve False si la palabra no es una palabra reservada

if __name__ == "__main__":
    main()      


                        