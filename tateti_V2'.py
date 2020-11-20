import os
tablero=[]
def imprimir():
    os.system('clear')
    for i in range (3):
        print(tablero[i])
 
tablero = [['_', '_', '_', ] 
for count in range(3)]# esto es como decir tablero por tres veces


def turno (jugador): # se declaran primero que todo las variables globales 
  
  while True:
      posicion=int(input('ingrese posición '))  

      if posicion>=1 and posicion<=9:
        if posicion==1:
          if tablero[0][0]=='_':
             tablero[0][0]=jugador
          
          else:
            print('la posicion ya se encuentra ocupada') 
            continue
          
        elif posicion==2:
          if tablero[0][1]=='_':
            tablero[0][1]=jugador     
          else:
            print('la posicion ya se encuentra ocupada ')
            continue
           
        elif posicion==3:
          if tablero[0][2]=='_':
            tablero[0][2]=jugador
          else:
            print('la posicion ya se encuentra ocupada ')
            continue

        elif posicion==4:
          if tablero[1][0]=='_':
            tablero[1][0]=jugador     
          else:
            print('la posicion ya se encuentra ocupada ')
            continue

        elif posicion==5:
          if tablero[1][1]=='_':
            tablero[1][1]=jugador     
          else:
            print('la posicion ya se encuentra ocupada ')
            continue

        elif posicion==6:
          if tablero[1][2]=='_':
            tablero[1][2]=jugador     
          else:
            print('la posicion ya se encuentra ocupada ') 
            continue

        elif posicion==7:
          if tablero[2][0]=='_':
            tablero[2][0]=jugador     
          else:
            print('la posicion ya se encuentra ocupada ') 
            continue

        elif posicion==8:
          if tablero[2][1]=='_':
            tablero[2][1]=jugador     
          else:
            print('la posicion ya se encuentra ocupada ')
            continue

        elif posicion==9:
          if tablero[2][2]=='_':
            tablero[2][2]=jugador     
          else:
            print('la posicion ya se encuentra ocupada ')    
            continue
        break
      else:
        print('posición no valida')    
         

print(tablero)

def verificacion():
  tateti=False
  for i in range (3):
      
    if tablero[i][0]==tablero[i][1]==tablero[i][2]:
      if tablero[i][0]!='_':
        print('Ganaste')
        tateti=True
     
  for j in range(3):
    if tablero[0][j]==tablero[1][j]==tablero[2][j]:
      if tablero[0][j]!='_':
        print ('Ganaste')
        tateti=True
  if tablero[0][2]==tablero[1][1]==tablero[2][0]:
      if tablero[0][2]!='_':
        print ('Ganaste')   
        tateti= True 
  if tablero[0][0]==tablero[1][1]==tablero[2][2]:
      if tablero[0][0]!='_':
        print ('Ganaste')   
        tateti=True
  return tateti
    



jugadorA='x'
jugadorB='o'

imprimir()
turno(jugadorA)
imprimir()
turno(jugadorB)
imprimir()
turno(jugadorA)
imprimir()
turno(jugadorB)
imprimir()
turno(jugadorA)
imprimir()
if not verificacion():# si no hay tateti
  turno(jugadorB)
  imprimir()
  if not verificacion():
    turno(jugadorA)
    imprimir()
    if not verificacion():
      turno(jugadorB)
      imprimir()
      if not verificacion():
        turno(jugadorA)
        imprimir()
        if not verificacion():
          print('No hay ganadores')
