import random 
piezas={'peon': 1,'torre':5, 'alfil':3, 'caballo':3, 'reina':9, 'rey':4 }

pun_blanco=0
pun_negro=0
cont_blancas=0
cont_negras=0

tablero=[]
lista = []

def imprimir():
    for i in range (8):
        print(tablero[i])
 
tablero = [['__', '__', '__', '__', '__', '__', '__', '__'] for count in range(8)]

#peones negros 
def piezas_negras(cant, pieza, simbolo):  
    global pun_negro
    cantidad=random.randint(0,cant)
    valor=piezas[pieza]
    puntaje=valor*cantidad
    pun_negro=pun_negro+puntaje

    for i in range (cantidad):
        vertical=random.randint(0,7)
        horizontal=random.randint(0,7)
        while True:
            if tablero[vertical][horizontal] =='__':
                tablero[vertical][horizontal]=simbolo
                break
            else:
                vertical=random.randint(0,7)
                horizontal=random.randint(0,7)

def piezas_blancas(cant, pieza, simbolo):  
    global pun_blanco
    cantidad=random.randint(0,cant)
    valor=piezas[pieza]
    puntaje=valor*cantidad
    pun_blanco=pun_blanco+puntaje

    for i in range (cantidad):
        vertical=random.randint(0,7)
        horizontal=random.randint(0,7)
        while True:
            if tablero[vertical][horizontal] =='__':
                tablero[vertical][horizontal]=simbolo
                break
            else:
                vertical=random.randint(0,7)
                horizontal=random.randint(0,7)


def jaque(rey):
    color=rey[1]
    cont_piezas=0
    for i in range (8):#recorro el tablero en indice i (vertical)
      for j in range(8):# recorroel tablero en indice j (horizontal)
        if tablero[i] [j]==rey:# busco si el  rey esta en los indices
          if i>0 and j>0:
            if tablero[i-1][j-1]!='__':
              if tablero[i-1][j-1][1]!=color:
                cont_piezas=cont_piezas+1
          if i>0:  
            if  tablero[i-1][j]!='__':
              if tablero [i-1][j][1]!=color:
                cont_piezas=cont_piezas+1
          if i>0 and j<7:
            if tablero[i-1][j+1]!='__':
              if tablero [i-1][j+1][1]!=color:
                cont_piezas=cont_piezas+1
          
          if j>0:
            if tablero[i][j-1]!='__':
              if tablero[i][j-1][1]!=color:
                cont_piezas=cont_piezas+1
          if j<7:
            if tablero[i][j+1]!='__':
              if tablero [i][j+1][1]!=color:
                cont_piezas=cont_piezas+1
          if i<7 and j>0:
            if tablero[i+1][j-1]!='__':
              if tablero[i+1][j-1][1]!=color:
                cont_piezas=cont_piezas+1
          if i<7:
            if  tablero[i+1][j]!='__':
              if tablero [i+1][j][1]!=color:
                cont_piezas=cont_piezas+1
          if i<7 and j<7:
            if tablero[i+1][j+1]!='__':
              if tablero[i+1][j+1][1]!=color:
                cont_piezas=cont_piezas+1

          if cont_piezas>1:
            print('El rey %s está en jaque' % rey)
          
          
                  
#peones blancos
piezas_negras(8,'peon', 'pN')
piezas_negras(2,'torre', 'tN')
piezas_negras(2,'caballo', 'cN')
piezas_negras(2,'alfil', 'aN')
piezas_negras(1,'reina', 'rN')
piezas_negras(1,'rey', 'RN')

piezas_blancas(8,'peon', 'pB')
piezas_blancas(2,'torre', 'tB')
piezas_blancas(2,'caballo', 'cB')
piezas_blancas(2,'alfil', 'aB')
piezas_blancas(1,'reina', 'rB')
piezas_blancas(1,'rey', 'RB')

imprimir()
jaque('RB')
jaque('RN')

print ('El puntaje del jugador con piezas blancas es '+ str(pun_blanco))
print('El puntaje del jugador con piezas negras es  '+ str(pun_negro))



