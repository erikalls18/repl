import os
tablero=[]

    

def imprimir():
    os.system('clear')
    for i in range (7,-1,-1):
        
        print(tablero[i])
 
tablero = [['_', '_', '_', '_', '_', '_', '_', '_' ] for count in range(8)]

def turno (jugador):
    llena=False
    while True:

        columna=int(input('Ingrese la columna a ocupar: '))
        if columna>=0 and columna<=7:
          j=0

          ocupado=False
          while not ocupado:
            if tablero [j][columna]=='_':
              tablero[j][columna]=jugador
              ocupado=True
            else: 
                j=j+1
                if j==8:
                  print('La columa esta llena ')
                  llena=True
          break
        else:
          print('columna incorrecta , vuelve a intentarlo')
    return columna, j    
               
      
def verificacion(columna, j, jugador ):
   
    en_linea=False        
    # COMPROBACION HORIZONTAL\
    lineHor=[]  
    x=j # Horizontal izq
    y=columna-1
    
      
    if (x>=0 and x <=7) and (y>=0 and y <=7):
       
        if tablero [x][y]==tablero[j][columna]:
          lineHor.append(y)
          lineHor.append(x)
        
    x=j
    y=columna-2 
      
    if (x>=0 and x <=7) and (y>=0 and y <=7):
       
        if tablero [x][y]==tablero[j][columna]:
          lineHor.append(x)
          lineHor.append(y)        
         
    x=j
    y=columna-3 
      
    if (x>=0 and x <=7) and (y>=0 and y <=7) :
        igual=False
        if tablero [x][y]==tablero[j][columna]:
          lineHor.append(x)
          lineHor.append(y) 

    x= j #horizontal derecha  
    y=columna+1
    if (x>=0 and x <=7) and (y>=0 and y <=7):
     
      if tablero [x][y]==tablero[j][columna]:
          lineHor.append(x)
          lineHor.append(y) 
          
    x=j 
    y=columna+2
      
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        
        if tablero [x][y]==tablero[j][columna]:
         lineHor.append(x)
         lineHor.append(y) 
            
    x=j 
    y=columna+3
      
    if (x>=0 and x <=7) and (y>=0 and y <=7):
       
        if tablero [x][y]==tablero[j][columna]:
          lineHor.append(x)
          lineHor.append(y)        
    
    if len(lineHor)==6:
      if jugador=='x':
        print ('el ganador deljuego es jugador 1')
      else:
        print ('el ganador deljuego es jugador 2')

      #print(' El ganador del juego es: %s' % jugador)
     
      en_linea=True

      return en_linea

    
        
    #COMPROBACION DIAGONALES 
    diag_derecha=[]
    x= j+1# diagonal derecha arriba
    y=columna+1

    if (x>=0 and x <=7) and (y>=0 and y <=7):
        
        if tablero [x][y]==tablero[j][columna]:
         diag_derecha.append (x)
         diag_derecha.append (y)
              
    x=j+2
    y=columna+2

    if (x>=0 and x <=7) and (y>=0 and y <=7):
      
        if tablero [x][y]==tablero[j][columna]:
            diag_derecha.append (x)
            diag_derecha.append (y)
     
    x=j+3
    y=columna+3

    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
          diag_derecha.append (x)
          diag_derecha.append (y)
         
    x=j-1 # diagonal derecha abajo
    y=columna+1
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        igual=False
        if tablero [x][y]==tablero[j][columna]:
            diag_derecha.append (x)
            diag_derecha.append (y)

    x=j-2
    y=columna+2
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
          diag_derecha.append (x)
          diag_derecha.append (y)     

    x=j-3
    y=columna+3
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
            diag_derecha.append (x)
            diag_derecha.append (y)
           

    if len (diag_derecha)==6:
      if jugador=='x':
        print ('el ganador deljuego es jugador 1')
      else:
        print ('el ganador deljuego es jugador 2')
      #print(' El ganador del juego es: %s' % jugador)
      en_linea=True
      return en_linea
    
    
    
    diag_izquierda=[]
    x=j-1 # diagonal izquierda abajo
    y=columna-1
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        
        if tablero [x][y]==tablero[j][columna]:
          diag_izquierda.append (x)
          diag_izquierda.append (y)
          
    x=j-2 
    y=columna-2
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
            diag_izquierda.append (x)
            diag_izquierda.append (y)
            
    
    x=j-3
    y=columna-3
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
            diag_izquierda.append (x)
            diag_izquierda.append (y)
           

    x=j+1# diagona izquierda arriba
    y=columna-1
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
           diag_izquierda.append (x)
           diag_izquierda.append (y)
          
    x=j+2
    y=columna-2
    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
           diag_izquierda.append (x)
           diag_izquierda.append (y)

    x=j+3
    y=columna-3
    if (x>=0 and x <=7) and (y>=0 and y <=7):
       
        if tablero [x][y]==tablero[j][columna]:
            diag_izquierda.append (x)
            diag_izquierda.append (y)
     

    if len (diag_izquierda)==6:
      if jugador=='x':
        print ('el ganador deljuego es jugador 1')
      else:
        print ('el ganador deljuego es jugador 2')
        #print(' El ganador del juego es: %s' % jugador)
      en_linea=True
      return en_linea

 
    vertical=[]
    x=j-1 #vertical
    y=columna

    if (x>=0 and x <=7) and (y>=0 and y <=7):
    
        if tablero [x][y]==tablero[j][columna]:
          vertical.append(x)
          vertical.append(y)     
          
    x=j-2 #vertical
    y=columna

    if (x>=0 and x <=7) and (y>=0 and y <=7):
       
        if tablero [x][y]==tablero[j][columna]:
          vertical.append(x)
          vertical.append(y)
    
    x=j-3 #vertical
    y=columna

    if (x>=0 and x <=7) and (y>=0 and y <=7):
        if tablero [x][y]==tablero[j][columna]:
            vertical.append(x)
            vertical.append(y)
    
    if len(vertical)==6:
      if jugador=='x':
        print ('el ganador deljuego es jugador 1')
      else:
        print ('el ganador deljuego es jugador 2')
      #print(' El ganador del juego es: %s' % jugador)
      en_linea=True
      return en_linea

jugador1='x'
jugador2='o'

imprimir()
columna,j=turno(jugador1)
verificacion(columna,j, jugador1)
imprimir()
columna,j=turno(jugador2)
verificacion(columna,j, jugador2)
imprimir()
columna,j=turno(jugador1)
verificacion(columna,j, jugador1)
imprimir()
columna,j=turno(jugador2)
verificacion(columna,j, jugador2)
imprimir()
columna,j=turno(jugador1)

while True:
  if not verificacion(columna,j, jugador1):
    imprimir()
    columna,j=turno(jugador2)
  else:
    print('Juego terminado')
    break
    
  if not verificacion(columna,j, jugador2):
    imprimir()
    columna,j=turno(jugador1)
  else:
    print('Juego terminado')
    break
    

