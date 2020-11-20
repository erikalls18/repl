cuadro1='_'
cuadro2='_'
cuadro3='_'
cuadro4='_'
cuadro5='_'
cuadro6='_'
cuadro7='_'
cuadro8='_'
cuadro9='_'

def turno (jugador):

  global cuadro1# la convierto en variable globalpara reescribir su valor 
  global cuadro2
  global cuadro3
  global cuadro4
  global cuadro5
  global cuadro6
  global cuadro7
  global cuadro8
  global cuadro9

  while True:
      
      posicion=int(input('ingrese la posicion que desea: '))
      if posicion >=1 and posicion<=9:
        if posicion==1:
          if cuadro1=='_':
              cuadro1=jugador      
          else:
            print('Posicion no valida') 
            continue  
        elif posicion==2:
          if cuadro2=='_':
              cuadro2=jugador     
          else:
            print('posicion no valida')
            continue
        elif posicion==3:
          if cuadro3=='_':
              cuadro3=jugador
          else:
            print('Posicion no valida')  
            continue
        elif posicion==4:
          if cuadro4=='_':
              cuadro4=jugador
          else:
            print('Posicion no valida')  
            continue  
        elif posicion==5:
          if cuadro5=='_':
              cuadro5=jugador
          else:
            print('Posicion no valida')  
            continue 
        elif posicion==6:
          if cuadro6=='_':
              cuadro6=jugador
          else:
            print('Posicion no valida')  
            continue 
        elif posicion==7:
          if cuadro7=='_':
              cuadro7=jugador
          else:
            print('Posicion no valida')  
            continue 
        elif posicion==8:
          if cuadro8=='_':
              cuadro8=jugador
          else:
            print('Posicion no valida')  
            continue 
        elif posicion==9:
          if cuadro9=='_':
              cuadro9=jugador
          else:
            print('Posicion no valida')  
            continue 
        break
      else:
        print('ingreso no valido')
      

def validacion(c1,c2,c3,c4,c5,c6,c7,c8,c9):
  
  
    if c1==c2==c3:
      if c1!='_':
        print('Ganaste!') 
        return True 
    elif c4==c5==c6:
      if c4!='_':
        print('Ganaste!')
        return True 
    elif c7==c8==c9:
      if c7!='_':
        print('Ganaste')
        return True 
    elif c1==c5==c9:
      if c1!='_':
        print('Ganaste!')
        return True 
    elif c3==c5==c7:
      if c3!='_':
        print('Ganaste!')
        return True 
    elif c1==c4==c7:
      if c1!='_':
        print ('Ganaste!')
        return True
    elif c2==c5==c8:
      if c2!='_':
        print ('Ganaste!')
        return True
    elif c3==c6==c9:
      if c3!='_':
        print ('Ganaste!')
        return True
    else:
      return False

def dibujar(c1,c2,c3,c4,c5,c6,c7,c8,c9):
  print(c1 +'|'+ c2+'|'+ c3+'|')
  print(c4 +'|'+ c5+'|'+ c6+'|')
  print (c7+'|'+ c8+'|'+ c9+'|') 

jugadorA='x'
jugadorB='o'

dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)

turno(jugadorA)
dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)

turno(jugadorB) 
dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)

turno(jugadorA)
dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)

turno(jugadorB)
dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)

turno(jugadorA)
if not validacion(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9): 
  dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)
  
  turno(jugadorB)
  if not validacion(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9):
    dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)
    
    turno(jugadorA)
    if not validacion(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9):
      dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)
      
      turno(jugadorB)
      if not validacion(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9):   
        dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)
        
        turno(jugadorA) 
        if not validacion(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9):
          print('No hay ganadores')
dibujar(cuadro1, cuadro2, cuadro3, cuadro4, cuadro5, cuadro6, cuadro7, cuadro8,cuadro9)


