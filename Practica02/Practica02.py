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
                if self.transicion in numeros:
                    self.estado="auxDec"
                elif self.transicion=='+' or self.transicion=='-':
                    self.estado="signo" 
                elif self.transicion=='0':
                    self.estado="Cero"  
                elif self.transicion=='/':
                    self.estado="com"      
                elif self.transicion.isalpha()  or self.transicion=='_' or self.transicion=='$':
                    self.estado="Alpha"                      
                else:
                    return False

            ##Estado 'auxDec'    
            elif self.estado =="auxDec": 
                if self.transicion == '.':
                  self.estado='puntoE'    
                elif str.isdigit(self.transicion):
                  self.estado='Decimal' 
                else: 
                    return False
                
            ##Estado 'puntoD'    
            elif self.estado =="puntoD": 
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE' 
                else: 
                    return False

        
            ##Estado 'Decimal'    
            elif self.estado =="Decimal": 
                if self.transicion == '.':
                  self.estado='puntoD'  
                elif str.isdigit(self.transicion):
                  self.estado='Decimal' 
                else: 
                    return False
                
            ##Estado 'puntoE'    
            elif self.estado =='puntoE':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE2'      
                else: 
                    return False

            
            ##Estado 'DecimalsE'    
            elif self.estado =='DecimalsE':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE' 
                else: 
                    return False   
                
            ##Estado 'DecimalsE2'    
            elif self.estado =='DecimalsE2':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE2' 
                elif self.transicion=='E':
                  self.estado='E'                   
                else: 
                    return False                   
                
            ##Estado 'signo'    
            elif self.estado =='signo':
                if self.transicion in numeros:
                  self.estado='auxDec'
                elif self.transicion == '0':
                  self.estado='Cero'   
                else: 
                    return False    
                
            ##Estado 'aux'    
            elif self.estado =='aux':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE0'  
                else: 
                    return False   
                
            ##Estado 'DecimalsE0'    
            elif self.estado =='DecimalsE0':
                if str.isdigit(self.transicion):
                  self.estado='DecimalsE0' 
                elif self.transicion=='E':
                  self.estado='E'                    
                else: 
                    return False   

                
            ##Estado 'cero'    
            elif self.estado =='Cero':
                if self.transicion =='.':
                  self.estado='aux' 
                elif self.transicion in octa_list:
                  self.estado='Octal'  
                elif self.transicion=='X'or self.transicion=='x':
                  self.estado='0X'                    
                else: 
                    return False 
                
             ##Estado 'E'
            elif self.estado =='E':
                if self.transicion=='+' or self.transicion=='-':   
                    self.estado='Signo2'
                elif str.isdigit(self.transicion):
                    self.estado='digitE'
                else: 
                    return False  
                
            ##Estado 'Octal'  
            elif  self.estado=='Octal':
                if self.transicion in octa_list:
                    self.estado='Octal'
                else :
                    return False
                
             ##Estado 'digitE'
            elif self.estado =='digitE':
                if str.isdigit(self.transicion):
                    self.estado='DecimalExp'
                else: 
                    return False
                
              ##Estado 'Signo2'
            elif self.estado =='Signo2':              
                if str.isdigit(self.transicion):
                    self.estado='digitE'
                else: 
                    return False

            ##Estado 'cero-x'    
            elif self.estado =='0X':
                if str.isdigit(self.transicion) or self.transicion in hexa:
                  self.estado='Hexadecimal'                     
                else:
                  return False

            ##Estado 'Hexadecimal'          
            elif self.estado =='Hexadecimal':
                if str.isdigit(self.transicion) or self.transicion in hexa:
                  self.estado='Hexadecimal' 
                else:
                 return False

            ##Estado 'com'          
            elif self.estado =='com':
                if self.transicion=='*':
                    self.estado='*'
                elif self.transicion=='/':
                   self.estado='Comentario'
                else: 
                    return False
                
            ##Estado '*'          
            elif self.estado =='*':
                if self.transicion=='*':
                    self.estado='com2'
                else: 
                    self.estado='*'
                
            ##Estado 'com2'          
            elif self.estado =='com2':
                if self.transicion=='/':
                    self.estado='ComentarioAs'
                else: 
                    return False

            elif self.estado =='Comentario':  
                return True

            
            ##Estado 'Alpha'          
            elif self.estado =='Alpha':
                if self.transicion.isalnum() or self.transicion=='_' or self.transicion=='$':
                    self.estado='Alpha'
         
                else: 
                   return False

           
            else:
              return False          
        
        if self.estado=="DecimalsE":
            return True
        elif self.estado=="DecimalsE2":
            return True    
        elif self.estado=="DecimalsE0":
            return True        
        elif self.estado=="Decimal":
            return True
        elif self.estado=="Octal":
            return True
        elif self.estado=="DecimalExp":
            return True               
    
        elif self.estado=="Hexadecimal":
            return True 
        elif self.estado=="Comentario":
            return True
        elif self.estado=="ComentarioAs":
            return True 
        elif self.estado=="auxDec":
            return True 
        elif self.estado=="Alpha":
            return True         
        elif self.estado=="*":
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


                        