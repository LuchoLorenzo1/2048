import random

TAMANO_GRILLA = 4 #Debe ser diferente de 0.
N_FINAL = 2048
VALORES_RANDOM = [2,4]
VACIO = 0

ARRIBA = 'w'
ABAJO = 's'
IZQUIERDA = 'a'
DERECHA = 'd'

def inicializar_juego():
    '''
    Crea y devuelve una matriz del juego de TAMANO_GRILLAxTAMANO_GRILLA.
    Añade un número random en la matriz.
    '''
    juego = []
    for i in range(TAMANO_GRILLA):
        fila = []
        for j in range(TAMANO_GRILLA):
            fila.append(VACIO)
        juego.append(fila)
    insertar_nuevo_random(juego)
    return juego

def mostrar_juego(juego):
    '''
    Imprime en consola la matriz del juego acompañada de separadores entre las columnas y filas, con cada celda alineada a la izquierda.
    '''
    espacios = len(str(N_FINAL))

    print('-'*TAMANO_GRILLA*espacios + (TAMANO_GRILLA+1)*'-')

    for i in range( TAMANO_GRILLA ):
        print('|',end='')
        for j in range(TAMANO_GRILLA):
            if juego[i][j] == 0:
                print(espacios*' ', end='|')
            else:
                n = juego[i][j]
                print(str(n) + (espacios-len(str(n)))*' ', end='|')
        print()
        print('-'*TAMANO_GRILLA*espacios + (TAMANO_GRILLA+1)*'-')

def juego_ganado(juego):
    '''
    Devuelve verdadero si el número objetivo (N_FINAL) esta en la matriz del juego
    '''
    for i in range(TAMANO_GRILLA):
        if N_FINAL in juego[i]:
            return True
    return False

def juego_perdido(juego):
    '''
    Devuelve verdadero si no se puede realizar ningun movimiento horizontal ni vertical. (Este último lo hace trasponiendo la matriz del juego)
    '''
    return hay_movimientos_horizontales(juego) and hay_movimientos_horizontales(trasponer_juego(juego))

def hay_movimientos_horizontales(matriz):
    '''
    Devuelve verdadero si no se puede realizar ningún movimiento horizontal en la matriz.
    Devuelve falso si hay al menos un cero, o si se puede realizar un movimiento.
    '''
    for fila in matriz:
        if not all(fila):
            return False
        for i in range(len(fila)-1):
                if fila[i] == fila[i+1]:
                    return False
    return True

def pedir_direccion(juego):
    '''
    Le pregunta al usuario cual sera su siguiente movimiento y lo devuelve.
    '''
    teclas = (ARRIBA,ABAJO,IZQUIERDA,DERECHA)

    print()
    direccion = input(f'Elegí una dirección {teclas}: ')
    while not direccion in teclas:
        direccion = input(f'Dirección invalida, Elegí una dirección entre estas {teclas}: ')
    print()
    return direccion

def actualizar_juego(juego,direccion):
    '''
    Recibe una dirección y una matriz del juego y devuelve una nueva matriz con todas sus filas combinadas en esa dirección.
    '''

    if direccion == IZQUIERDA:
        nuevo_juego = []
        for fila in juego:
            nuevo_juego.append(fila[:])
        return combinar_matriz(nuevo_juego)

    elif direccion == ARRIBA:
        nuevo_juego = trasponer_juego(juego)
        return trasponer_juego(combinar_matriz(nuevo_juego))

    elif direccion == DERECHA:
        juego_invertido = invertir_juego(juego)
        nuevo_juego = combinar_matriz(juego_invertido)
        return invertir_juego(nuevo_juego)

    elif direccion == ABAJO:
        juego_traspuesto_invertido = invertir_juego(trasponer_juego(juego))
        juego_combinado = combinar_matriz(juego_traspuesto_invertido)
        return trasponer_juego(invertir_juego(juego_combinado))

def insertar_nuevo_random(nuevo_juego):
    '''
    Recibe y devuelve el nuevo juego insertandole un número que este entre los VALORES_RANDOM en una columna y fila aleatoria.
    '''
    numero = random.choice(VALORES_RANDOM)

    while True:
        fila = random.randint(0,TAMANO_GRILLA-1)
        columna = random.randint(0,TAMANO_GRILLA-1)

        if nuevo_juego[fila][columna] == VACIO:
            nuevo_juego[fila][columna] = numero
            break

    return nuevo_juego

def combinar_matriz(juego):
    '''
    recibe el juego y devuelve un nuevo juego cuyas filas han sido todas combinadas hacia la izquierda con la función combinar_fila()
    '''
    nuevo_juego = []

    for fila in juego:
        nuevo_juego.append(combinar_fila(fila))

    return nuevo_juego

def combinar_fila(fila):
    '''
    Recibe una fila de la matriz del juego y devuelve una nueva fila combinada hacia la izquierda.
    '''
    nueva_fila = []

    for n in fila:
        if n != 0:
            nueva_fila.append(n)

    for i in range(len(nueva_fila)-1):
        if nueva_fila[i] == nueva_fila[i+1]:
            nueva_fila[i] *= 2
            nueva_fila.pop(i+1)
            nueva_fila.append(0)

    for i in range(TAMANO_GRILLA - len(nueva_fila)):
        nueva_fila.append(0)

    return nueva_fila

def invertir_juego(juego):
    '''
    Recibe la matriz del juego por parametro y devuelve una nueva matriz del juego con todas las filas invertidas.
    '''
    nuevo_juego = []
    for fila in juego:
        nuevo_juego.append(fila[::-1])
    return nuevo_juego

def trasponer_juego(juego):
    '''
    Recibe la matriz del juego por parametro y devuelve una nueva matriz del juego traspuesta (cambiando filas por columnas).
    '''
    nueva_matriz = []
    for j in range(TAMANO_GRILLA):
        nueva_fila = []
        for i in range(TAMANO_GRILLA):
            nueva_fila.append(juego[i][j])

        nueva_matriz.append(nueva_fila)

    return nueva_matriz
