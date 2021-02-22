
import random
import os 

lancha=1
corbeta=2 
fragata=3 
destructor=4 
esquema1={}
esquema2={}
jugador1='H'
jugador2='C'


tablero1 = [['_', '_', '_', '_', '_', '_', '_', '_' ] for count in 
range(8)]  
tablero2 = [['_', '_', '_', '_', '_', '_', '_', '_' ] for count in 
range(8)]
tablero3 = [['?', '?', '?', '?', '?', '?', '?', '?' ] for count in 
range(8)]
indice = '    0    1    2    3    4    5    6    7'


def imprimir():
  os.system('clear')
  print('HUMANO')
  print(indice)
  for i in range (7,-1,-1):
    print(i, tablero1[i])
  print('___________________________')
  print('MAQUINA')
  for i in range (7,-1,-1):
   # print(i, tablero2[i])
  print('___________________________')

  print(indice)
  for i in range (7,-1,-1):
    print(i, tablero3[i])

#BLOQUE DE CREACION DE TABLEROS
def crear_coordenadas ():

  horizontal=random.randint(0,7) 
  vertical=random.randint(0,7) 
  direccion=random.randint(0,3)

  return horizontal, vertical, direccion 

def verificacion_coordenadas (hor1, ver1, dire1,largo, tablero):
    
  aux=[]
  permitido=False
 
  if dire1==0:#norte  
    if hor1+largo <= 7:
      for i in range (largo):
        aux.append(tablero[hor1+i] [ver1])
        if aux.count('_')== largo:
          permitido=True             

  elif dire1==1:#este
    if  ver1+largo <=7:
      for i in range (largo):
        aux.append(tablero[hor1] [ver1+i])
        if aux.count('_')== largo: 
          permitido=True                   
  elif dire1==2:#sur    
    if hor1-largo>=0:
          for i in range (largo):
            aux.append(tablero[hor1-i] [ver1])
            if aux.count('_')== largo: 
              permitido=True                        
  else:
    dire1==3 #oeste
    if ver1-largo>=0:
      for i in range (largo):
        aux.append(tablero[hor1] [ver1-i])
        if aux.count('_')== largo: 
          permitido=True
  return permitido
   
def put_ships(hor, ver, dire,largo, letra, numero, cant=None):

  if numero == 1:

    for i in range (largo):
      if dire==0:#norte  
        tablero1[hor+i][ver]=letra
        if cant is None:
          esquema1.setdefault(letra + '_' + str(i), (hor+i,ver))
        else:
          esquema1.setdefault(letra + str(cant) + '_' + str(i), (hor+i,ver))
      elif dire==1:
        tablero1[hor][ver+i]=letra 
        if cant is None:
          esquema1.setdefault(letra + '_' + str(i), (hor,ver+i))
        else:
          esquema1.setdefault(letra + str(cant) + '_' + str(i), (hor,ver+i))    
      
      elif dire==2:          
        tablero1[hor-i][ver]=letra
        if cant is None:
          esquema1.setdefault(letra + '_' + str(i), (hor-i,ver))
        else:
          esquema1.setdefault(letra + str(cant) + '_' + str(i), (hor-i,ver))
      else:
        tablero1[hor][ver-i]=letra  
        if cant is None:
          esquema1.setdefault(letra + '_' + str(i), (hor,ver-i))
        else:
          esquema1.setdefault(letra + str(cant) + '_' + str(i), (hor,ver-i))
    if cant is None:
      esquema1.setdefault(letra + '_C', 0)
    else:
      esquema1.setdefault(letra + str(cant) + '_C', 0)

  else:
    
    for i in range (largo):
      if dire==0:#norte
        tablero2[hor+i][ver]=letra
        if cant is None:
          esquema2.setdefault(letra + '_' + str(i), (hor+i,ver))
        else:
          esquema2.setdefault(letra + str(cant) + '_' + str(i), (hor+i,ver))            
      elif dire==1:
        tablero2[hor][ver+i]=letra 
        if cant is None:
          esquema2.setdefault(letra + '_' + str(i), (hor,ver+i))
        else:
          esquema2.setdefault(letra + str(cant) + '_' + str(i), (hor,ver+i))    
      
      elif dire==2:          
        tablero2[hor-i][ver]=letra
        if cant is None:
          esquema2.setdefault(letra + '_' + str(i), (hor-i,ver))
        else:
          esquema2.setdefault(letra + str(cant) + '_' + str(i), (hor-i,ver))

      else:
        tablero2[hor][ver-i]=letra 
        if cant is None:
          esquema2.setdefault(letra + '_' + str(i), (hor,ver-i))
        else:
          esquema2.setdefault(letra + str(cant) + '_' + str(i), (hor,ver-i))
    if cant is None:
      esquema2.setdefault(letra + '_C', 0)
    else:
      esquema2.setdefault(letra + str(cant) + '_C', 0)

def generar_tablero(tableros, numero):
  #imprimir()
  resultado = False
  while not resultado:# es lo mismo que decir mientras el resultado sea false#
  #crear_coordenadas ()
    coordenada1, coordenada2, orientacion = crear_coordenadas()
    resultado = verificacion_coordenadas(coordenada1, coordenada2, orientacion, destructor, tableros)# guardo variable un valor booleano 
  put_ships(coordenada1, coordenada2, orientacion,destructor, 'D', numero)
  #imprimir()

  for i in range(2):
    resultado = False
    while not resultado:
      coordenada1, coordenada2, orientacion =crear_coordenadas()
      resultado = verificacion_coordenadas(coordenada1, coordenada2, orientacion, fragata, tableros)# guardo variable un valor booleano 
    put_ships(coordenada1, coordenada2, orientacion,fragata, 'F', numero , i)
    #imprimir()

  for i in range(3):
    resultado = False
    while not resultado:
      coordenada1, coordenada2, orientacion =crear_coordenadas()
      resultado = verificacion_coordenadas(coordenada1, coordenada2, orientacion, corbeta, tableros)# guardo variable un valor booleano 
    put_ships(coordenada1, coordenada2, orientacion,corbeta, 'C', numero , i)
    #imprimir()

  for i in range(4):
    resultado = False
    while not resultado:
      coordenada1, coordenada2, orientacion =crear_coordenadas()
      resultado = verificacion_coordenadas(coordenada1, coordenada2, orientacion, lancha, tableros)# guardo variable un valor booleano 
    put_ships(coordenada1, coordenada2, orientacion, lancha, 'L', numero, i )
    #imprimir()


#BLOQUE DE JUEGO
def check_ingreso_disparos (jugador):
  # con esta funcion hago la validacion del ingreso 
  if jugador=='H':
    valido=False
    while not valido:
      posicion1=int(input('ingrese coordenadas vertical  de 0 a 7: '))
      posicion2=int(input('ingrese coordenadas  horizontalde 0 a 7: '))
      if (posicion1>=0 and posicion1<=7) and (posicion2>=0 and posicion2<=7):
        if tablero3[posicion1][posicion2]=='G' or tablero3[posicion1][posicion2]== 'H' or tablero3[posicion1][posicion2]=='A':
          print('Ya se han realizado disparos en estas coordenadas')
        else:
          valido=True
      else:
        print('Las coordendas ingresadas se encuentra fuera de rango')
    # retorno los disparos  como una tupla   
    tupla=(posicion1, posicion2)
    return (tupla)
  else:
    posicion1=random.randint(0,7 ) 
    posicion2=random.randint(0,7 ) 
    while tablero1[posicion1][posicion2]=='G' or tablero1[posicion1][posicion2]== 'H' or tablero1[posicion1][posicion2]=='A':
      posicion1=random.randint(0,7 ) 
      posicion2=random.randint(0,7 ) 
    tupla=(posicion1, posicion2)
    return (tupla)
  
def get_key(val, esquema):
  #en esta parte verifico si los disparos se encuentran dentro del diccionario, en caso de que no lo esté, devuelve un valore none que significa que cayó al agua. 
    for key, value in esquema.items():
         if val == value:
             return key
    return None

def search_dict(clave, posiciones, jugador):
  
  (posicion1, posicion2) = posiciones 
  if jugador=='H':
    if 'D' in clave:
      tablero3[posicion1][posicion2]='G'
      esquema2['D_C']+=1
      if esquema2['D_C']==4:
        for i in range(4):
          clave = 'D_' + str(i)
          posicion1, posicion2 = esquema2[clave]
          tablero3[posicion1][posicion2] = 'H' 
    
  if 'F0' in clave:
    tablero3[posicion1][posicion2]='G'
    esquema2['F0_C']+=1
    if esquema2['F0_C']==3:
      for i in range(3):
        clave='F0'+'_'+ str(i)
        posicion1, posicion2 = esquema2[clave]
        tablero3[posicion1][posicion2] = 'H'
  elif  'F1'in clave:
      tablero3[posicion1][posicion2]='G'
      esquema2['F1_C']+=1
      if  esquema2['F1_C']==3:
        for j in range(3):
          clave='F1'+'_'+  str(j)
          posicion1, posicion2 = esquema2[clave]
          tablero3[posicion1][posicion2] = 'H'''

  if 'C0' in clave:
    tablero3[posicion1][posicion2]='G'
    esquema2['C0_C']+=1
    if esquema2['C0_C']==2:
      for i in range(2):
        clave='C0'+'_'+ str(i)
        posicion1, posicion2 = esquema2[clave]
        tablero3[posicion1][posicion2] = 'H'
  elif  'C1' in clave:
    tablero3[posicion1][posicion2]='G'
    esquema2['C1_C']+=1
    if esquema2['C1_C']==2:
      for i in range(2):
        clave='C1'+'_'+ str(i)
        posicion1, posicion2 = esquema2[clave]
        tablero3[posicion1][posicion2] = 'H'
  elif 'C2' in clave:
    tablero3[posicion1][posicion2]='G'
    esquema2['C2_C']+=1
    if esquema2['C2_C']==2:
      for i in range(2):
        clave='C2'+'_'+ str(i)
        posicion1, posicion2 = esquema2[clave]
        tablero3[posicion1][posicion2] = 'H'
  if 'L'in clave:
    tablero3[posicion1][posicion2] = 'H'
  
def search_dict2(clave, posiciones, jugador):
  (posicion1, posicion2) = posiciones 
  if jugador=='C':
    if 'D' in clave:
      tablero1[posicion1][posicion2]='G'
      esquema1['D_C']+=1
      if esquema1['D_C']==4:
        for i in range(4):
          clave = 'D_' + str(i)
          posicion1, posicion2 = esquema1[clave]
          tablero1[posicion1][posicion2] = 'H' 
    
    if 'F0' in clave:
      tablero1[posicion1][posicion2]='G'
      esquema1['F0_C']+=1
      if esquema1['F0_C']==3:
        for i in range(3):
          clave='F0'+'_'+ str(i)
          posicion1, posicion2 = esquema1[clave]
          tablero1[posicion1][posicion2] = 'H'
    elif  'F1'in clave:
      tablero1[posicion1][posicion2]='G'
      esquema1['F1_C']+=1
      if  esquema1['F1_C']==3:
        for j in range(3):
          clave='F1'+'_'+  str(j)
          posicion1, posicion2 = esquema1[clave]
          tablero1[posicion1][posicion2] = 'H'

    if 'C0' in clave:
      tablero1[posicion1][posicion2]='G'
      esquema1['C0_C']+=1
      if esquema1['C0_C']==2:
        for i in range(2):
          clave='C0'+'_'+ str(i)
          posicion1, posicion2 = esquema1[clave]
          tablero1[posicion1][posicion2] = 'H'
    elif  'C1' in clave:
      tablero1[posicion1][posicion2]='G'
      esquema1['C1_C']+=1
      if esquema1['C1_C']==2:
        for i in range(2):
          clave='C1'+'_'+ str(i)
          posicion1, posicion2 = esquema1[clave]
          tablero1[posicion1][posicion2] = 'H'
    elif 'C2' in clave:
      tablero1[posicion1][posicion2]='G'
      esquema1['C2_C']+=1
      if esquema1['C2_C']==2:
        for i in range(2):
          clave='C2'+'_'+ str(i)
          posicion1, posicion2 = esquema1[clave]
          tablero1[posicion1][posicion2] = 'H'
    if 'L'in clave:
      tablero1[posicion1][posicion2] = 'H'

generar_tablero(tablero1, 1)
generar_tablero(tablero2, 2)
imprimir()
victoria=False
while not victoria:
  ningen_count=0 # se requiere que en cada iteracion del while los contadores esten en 0
  fempu_count=0
  disparos=check_ingreso_disparos(jugador1)#jugador 1
  clave=get_key(disparos,esquema2)
  (posicion1, posicion2)=disparos
  if clave==None:
    if tablero2[posicion1][posicion2]=='_':
      tablero3[posicion1][posicion2]='A' 
  else:   
    #search_dict1(clave, esquema1,disparos)
      search_dict(clave, disparos, jugador1)
      for i in range(8):
        for j in range(8):
          if  tablero3[i][j]=='H':
            print(ningen_count)
            ningen_count+=1
            print(ningen_count)

  disparos=check_ingreso_disparos(jugador2)#jugador 2
  clave=get_key(disparos, esquema1)
  (posicion1, posicion2)=disparos
  print(disparos)
  if clave==None:
    if tablero1[posicion1][posicion2]=='_':
      tablero1[posicion1][posicion2]='A' 
  else:   
    search_dict2(clave, disparos, jugador2)
    for i in range(8):
        for j in range(8):
          if  tablero1[i][j]=='H':
            fempu_count+=1
  imprimir()
  if ningen_count==20:
    print ('Ningen  ha ganado la batalla ')
    victoria=True
  elif fempu_count ==20:
    print(' La femputadora ha ganado la batalla')
    victoria=True
