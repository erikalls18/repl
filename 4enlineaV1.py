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
          print('columna incorrecta , vuele a intentarlo') 

def verificacion ():
   
    enLinea=False
    for j in range(8):
       for i in range (8):
          
        
          if i >0 and i<7:
              try:
               
              
                if tablero[j][i]==tablero[j][i-1]==tablero [j][i+1]==tablero [j][i+2]:
                  if tablero[j][i]!='_':
                    print ('ganaste ')
                    enLinea=True # horizontal d
              except:
                pass
                if  tablero[j][i]==tablero[j][i-1]==tablero [j][i-2]==tablero [j][i+1]:
                    if tablero[j][i]!='_':
                      print ('ganaste ')
                      enLinea=True # horizontal izquierda-derecha
                      
                      
            
       
          if i==0:
              if tablero[j][i]==tablero[j][i+1]==tablero [j][i+2]==tablero [j][i+3]:
                 if tablero[j][i]!='_':
                  print ('ganaste ')
                  enLinea=True # horizontal derecho
                 

          
          if i==7:
              if tablero[j][i]==tablero[j][i-1]==tablero [j][i-2]==tablero [j][i-3]:
                if tablero[j][i]!='_':
                  print ('ganaste ')
                  enLinea=True # horizontal izquierda
                 
          
         
              
       
          if j>=0 and j<=7:
            try: 
              if tablero[j][i]==tablero[j-1][i]==tablero [j-2][i]==tablero [j-3][i]:
                if tablero[j][i]!='_':
                  print('ganaste')
                  enLinea=True # vertical
            except:
              pass
               
       
          if i==0 and j <=7:
            try:
            
              if tablero[j][i]==tablero[j+1][i+1]==tablero [j+2][i+2]==tablero [j+3][i+3]:
                if tablero[j][i]!='_': 
                  print ('ganaste ')
                  enLinea=True # diagonal (0) hacia arriba
            except:
              pass
                 

        
          if i>0 and i<=7 and j>0 and j<=7: 
              if tablero[j][i]==tablero[j-1][i-1]==tablero [j-2][i-2]==tablero [j-3][i-3]:
                  if tablero[j][i]!='_':
                    print ('ganaste ')
                    enLinea=True # diagonal(0) reversa abajo
                   
          
          
          if i==7 and j<=7:
            try:
              if tablero[j][i]==tablero[j+1][i-1]==tablero [j+2][i-2]==tablero [j+3][i-3]:
                if tablero[j][i]!='_': 
                  print ('ganaste ')
                  enLinea=True #diagonal (7 )arriba
            except:
              pass

              
 
          if i>0 and i<=7 and j>0 and j<=7: 
            try: 
              if tablero[j][i]==tablero[j-1][i+1]==tablero [j-2][i+2]==tablero [j-3][i+3]:
                if tablero[j][i]!='_': 
                  print ('ganaste ')
                  enLinea=True # diagonal arriba derecha 


            #condiciones intercaladas

              elif tablero[j][i]==tablero[j-1][i-1]==tablero [j+1][i+1]==tablero [j+2][i+2]:
                if tablero[j][i]!='_': 
                  print ('ganaste ')
                  enLinea=True 
          
              elif tablero[j][i]==tablero[j-1][i-1]==tablero [j-2][i-2]==tablero [j+1][i+1]:
                if tablero[j][i]!='_': 
                  print ('ganaste ')
                  enLinea=True

              elif tablero[j][i]==tablero[j-1][i+1]==tablero [j+1][i-1]==tablero [j+2][i-2]:
                if tablero[j][i]!='_': 
                  print ('ganaste ')
                  enLinea=True

              elif tablero[j][i]==tablero[j-1][i+1]==tablero [j-2][i+2]==tablero [j+1][i-1]:
                if tablero[j][i]!='_': 
                  print ('ganaste ')
                  enLinea=True
            except:
              pass
    return enLinea             

      


jugador1='x'
jugador2='o'

imprimir()
turno(jugador1)
imprimir()
turno(jugador2)
imprimir()
turno(jugador1)
imprimir()
turno(jugador2)
imprimir()
turno(jugador1)
imprimir()
turno(jugador2)
imprimir()
turno(jugador1)
imprimir
turno(jugador2)
imprimir()
if not verificacion():
    turno(jugador1)
    imprimir()
    if not verificacion():
      turno(jugador2)
      imprimir()
      if not verificacion():
        turno(jugador1)
        imprimir()
        if not verificacion():
          turno(jugador2)
          imprimir()
          if not verificacion():
            turno(jugador1)
            imprimir()
            if not verificacion():
              turno(jugador2)
              imprimir()
              if not verificacion():
                turno(jugador1)
                imprimir()
                if not verificacion():
                  turno(jugador2)
                  imprimir()
                  if not verificacion():
                    turno(jugador1)
                    imprimir()
                  else:
                    print('
