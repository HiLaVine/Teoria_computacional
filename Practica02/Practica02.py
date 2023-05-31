### Práctica 2. Analizador Lexico  ###
### Farrera Mendez Emmanuel Sinai ###
### Teoria Computacional ####

import shutil #Modulo usado para manipular archivos. 

def main(): #funcion principal 

    count = 0 #encargado de contar las lineas
    b=0 #bandera encargada de indicar cuando se encuentra un error. 
    
    archivos() #funcion encargada de tomar el archivo original y tranformarlo a un txt quitando los caracteres especiales. 
    
    with open('archivo_copia.txt','r') as file: #abre el archivo en modo lectura. 
        
     for line in file: #encargado de recorrer cada linea del archivo. 
         
        count=count+1 #incrementa el contador de las lienas. 
        
        for word in line.split(): #encargado de revisar cada palabra de cada linea. 
            
            if palabras_reservadas(word)==False : #verifica si la palabra es reservada, si no

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

class Automata: #automata encargado del analisis. 
        
    def __init__(self, texto): #Constructor de la clase Automata.
        
        self.texto = texto #parámetro texto que se utilizará para asignar un valor al atributo texto. 
        
    def analizador_lexico(self):
        numeros = ['1', '2', '3','4','5','6','7','8','9'] #decimales del 1 al 9
        octa_list = ['0','1','2', '3','4','5','6','7'] #octales del 0 al 7
        hexa = ['A','B','C', 'D','E','F']   #hexadecimales de la A a la F

        self.estado='inicio'  # Asigna el valor 'inicio' al atributo 'estado' de la instancia actual. 
        for i in range(0,len(self.texto)):
            self.transicion=self.texto[i] #Asigna el carácter en la posición i de 'texto' de la instancia actual (self) al atributo 'transicion'
            
            ##Estado inicial
            if self.estado == "inicio": #estado de inicio
                if self.transicion in numeros: #si recibe un numero del 1 al 9 va a entero. 
                    self.estado="entero"
                elif self.transicion=='+' or self.transicion=='-': #si recibe un signo + o - pasa a signo. 
                    self.estado="signo" 
                elif self.transicion=='0':#si recibe un 0 va a cero
                    self.estado="cero"  
                elif self.transicion=='/':#si recibe un / va a comen_0
                    self.estado="comen_0"      
                elif self.transicion.isalpha()  or self.transicion=='_' or self.transicion=='$': #si el carácter actual es una letra, '_' o '$', se va a est_1
                    self.estado="est_1"                      
                else:
                    return False  # Si el carácter actual no se encuentra en ninguna de las condiciones anteriores, se retorna False, indicando que hubo un error en el análisis léxico
                
             ##Estado 'comen_0'          
            elif self.estado =="comen_0": #estado comen_0
                if self.transicion=='*': #si recibe un * va a comen_1
                    self.estado='comen_1'
                elif self.transicion=='/':#si recibe un / vamos a comentario_s
                   self.estado='comentario_s' 
                else: 
                    return False # Si el carácter actual no es * ni / se retorna False indicando un error en el análisis léxico
                
            ##Estado 'comen_1'          
            elif self.estado =='comen_1': #estado comen_1
                if self.transicion=='*': #si recibe un * va a est_0
                    self.estado='est_0' 
                else: 
                    self.estado='comen_1'  # Si el carácter actual no es * se mantiene en el mismo estado comen_1
                
            ##Estado 'est_0'          
            elif self.estado =='est_0':
                if self.transicion=='/':
                    self.estado='comentasio_as'
                else: 
                    return False # Si el carácter actual no es / se retorna False indicando un error en el análisis léxico

            elif self.estado =='comentario_s':  
                return True  # Si el estado actual es 'comentario_s', se retorna True, indicando que se ha encontrado un comentario de línea
            
             ##Estado 'cero'    
            elif self.estado =='cero':
                if self.transicion =='.':# Si el carácter actual es . se cambia al estado est_2
                  self.estado='est_2' 
                elif self.transicion in octa_list:#Si el carácter actual es esta es del 0 al 7 se cambia al estado octal
                  self.estado='octal'  
                elif self.transicion=='X'or self.transicion=='x': #si recibe una X o una x va al estado hexa
                  self.estado='est_3'                    
                else: 
                    return False  # Si el carácter actual no es . ni un dígito octal, ni X ni x se retorna False indicando un error en el análisis léxico
                
            ##Estado 'octal'  
            elif  self.estado=='octal':
                if self.transicion in octa_list: #Si el carácter actual es esta es del 0 al 7 se cambia al estado octal
                    self.estado='octal'
                else :
                    return False # Si el carácter actual no pertenece a octa_list se retorna False indicando un error en el análisis léxico
                
             ##Estado 'est_3'    
            elif self.estado =='est_3':
                if str.isdigit(self.transicion) or self.transicion in hexa: #Si el carácter actual es esta es hexa o es un digito se cambia al estado hexadecimal
                  self.estado='Hexadecimal'                     
                else:
                  return False# Si el carácter actual no pertenece a hexa o no es un digito se retorna False indicando un error en el análisis léxico
              
            ##Estado 'Hexadecimal'          
            elif self.estado =='Hexadecimal':
                if str.isdigit(self.transicion) or self.transicion in hexa: #Si el carácter actual es esta es hexa o es un digito se mantiene en el estado Hexadecimal
                  self.estado='Hexadecimal' 
                else:
                 return False # Si el carácter actual no pertenece a hexa o no es un digito se retorna False indicando un error en el análisis léxico
             
            ##Estado 'signo'    
            elif self.estado =='signo':
                if self.transicion in numeros: #Si el carácter actual es esta en numeros pasa a entero.  
                  self.estado='entero'
                elif self.transicion == '0': #Si el carácter actual es un 0 para a cero. 
                  self.estado='cero'   
                else: 
                    return False  #si el carácter actual no está en la lista numeros ni es '0', se retorna False, indicando un error en el análisis léxico
                
             ##Estado 'decimal'    
            elif self.estado =="decimal": 
                if self.transicion == '.': # Si el carácter actual es . se cambia al estado 'dec_c_p'
                  self.estado='dec_c_p'  
                elif str.isdigit(self.transicion): #Si el carácter actual es esta es un digito se mantiene en el estado decimal
                  self.estado='decimal' 
                else: 
                    return False  # Si el carácter actual no es . ni un dígito se retorna False indicando un error en el análisis léxico
            
             ##Estado 'dec_c_p'    
            elif self.estado =="dec_c_p": 
                if str.isdigit(self.transicion): # Si el carácter actual es un dígito, se cambia al estado decimal_p
                  self.estado='decimal_p' 
                else: 
                    return False   # Si el carácter actual no es un dígito se retorna False indicando un error en el análisis léxico
                
            ##Estado 'dec_p_e'    
            elif self.estado =='dec_p_e':
                if str.isdigit(self.transicion): # Si el carácter actual es un dígito, se cambia al estado decimal_e1
                  self.estado='decimal_e1'      
                else: 
                    return False # Si el carácter actual no es un dígito se retorna False indicando un error en el análisis léxico
                
             ##Estado 'decimal_e1'    
            elif self.estado =='decimal_e1':
                if str.isdigit(self.transicion): # Si el carácter actual es un dígito, se mantiene al estado decimal_e1
                  self.estado='decimal_e1' 
                elif self.transicion=='E': # Si el carácter actual es una E va al estado E_0
                  self.estado='E_0'                   
                else: 
                    return False   #Si el carácter actual no es un dígito o una E se retorna False indicando un error en el análisis léxico
            
            ##Estado 'entero'    
            elif self.estado =="entero": 
                if self.transicion == '.': # Si el carácter actual es un . va al estado dec_p_e
                  self.estado='dec_p_e'    
                elif str.isdigit(self.transicion): # Si el carácter actual es un dígito, se cambia al estado decimal
                  self.estado='decimal' 
                else: 
                    return False #Si el carácter actual no es un . o un digito se retorna False indicando un error en el análisis léxico
            
            ##Estado 'decimal_p'    
            elif self.estado =='decimal_p':
                if str.isdigit(self.transicion):   # Si el carácter actual es un dígito, se mantiene en el estado 'decimal_p'
                  self.estado='decimal_p' 
                else: 
                    return False    # Si el carácter actual no es un dígito, se retorna False, indicando un error en el análisis léxico
                
            ##Estado 'E'
            elif self.estado =='E':
                if self.transicion=='+' or self.transicion=='-':   # Si el carácter actual es un + o -, se va al estado signo_1
                    self.estado='Signo2'
                elif str.isdigit(self.transicion): # Si el carácter actual es un dígito, se cambia al estado E_1
                    self.estado='E_1'
                else: 
                    return False  #Si el carácter actual no es un +, - o un digito se retorna False indicando un error en el análisis léxico
                
             ##Estado 'E_1'
            elif self.estado =='E_1':
                if str.isdigit(self.transicion): # Si el carácter actual es un dígito, se cambia al estado decimal_e
                    self.estado='decimal_e'
                else: 
                    return False #Si el carácter actual no es un digito se retorna False indicando un error en el análisis léxico
                
              ##Estado 'Signo_1'
            elif self.estado =='Signo_1':              
                if str.isdigit(self.transicion): # Si el carácter actual es un dígito, se cambia al estado decimal_e
                    self.estado='decimal_e'
                else: 
                    return False #Si el carácter actual no es un digito se retorna False indicando un error en el análisis léxico
                
            ##Estado 'est_2'    
            elif self.estado =='est_2':
                if str.isdigit(self.transicion): # Si el carácter actual es un dígito, se cambia al estado decimal_e
                  self.estado='decimal_e0'  
                else: 
                    return False   #Si el carácter actual no es un digito se retorna False indicando un error en el análisis léxico
                
            ##Estado 'decimal_e0'    
            elif self.estado =='decimal_e0':
                if str.isdigit(self.transicion): # Si el carácter actual es un dígito, se queda en el estado decimal_e0
                  self.estado='decimal_e0' 
                elif self.transicion=='E': # Si el carácter actual es una E se va al estado E
                  self.estado='E'                    
                else: 
                    return False  #Si el carácter actual no es una E o un digito se retorna False indicando un error en el análisis léxico
            
             ##Estado 'est_1'          
            elif self.estado =='est_1':
                if self.transicion.isalnum() or self.transicion=='_' or self.transicion=='$': # Si el carácter actual es alfanumérico, '_', o '$' se queda en el estado est_1
                    self.estado='est_1'
         
                else: 
                   return False #Si el carácter actual no es alfanumérico, '_', ni '$', se retorna False, indicando un error en el análisis léxico
               
            else:
              return False          
        
        if self.estado=="decimal_p":
            return True
        elif self.estado=="decimal_e1":
            return True    
        elif self.estado=="decimal_e0":
            return True        
        elif self.estado=="decimal":
            return True
        elif self.estado=="octal":
            return True
        elif self.estado=="decimal_e":
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
        elif self.estado=="*":
            return False 


if __name__ == "__main__":
    main()      


               
                
            

            