""" INFORMACION
    Autores:
        97244 | Bencivenga, Carlos Martin   | 1k7
        97199 | Conte, Martin Eduardo       | 1k7
        97177 | Mendez, Octavio Benjamin    | 1k7

    Algoritmos y Estructuras de Datos - Universidad Tecnologica Nacional - Facultad Regional de Cordoba
    Abril de 2022
"""

import random

print("---------------------")
print("| TURNO DEL JUGADOR |")
print("---------------------")

# Cartas del jugador
n_carta1 = random.randint(2, 11); n_carta2 = random.randint(2, 11); n_carta3 = random.randint(2, 11)

# Cartas del Crupier
n_carta1_c = random.randint(2, 11); n_carta2_c = random.randint(2, 11); n_carta3_c = random.randint(2, 11)

p = ["♡", "♢", "♤", "♧"]
letra = ["10", "J", "Q", "K"]
palo_j = p[random.randint(0,3)]; palo_j2 = p[random.randint(0,3)]; palo_j3 = p[random.randint(0,3)]
palo_c = p[random.randint(0,3)]; palo_c2 = p[random.randint(0,3)]; palo_c3 = p[random.randint(0,3)]

# Figuras para cartas de valor 10 y AS del jugador
f_carta1 = " "; f_carta2 = " "; f_carta3 = " "

# Figuras para cartas de valor 10 y AS del crupier
f_carta1_c = " "; f_carta2_c = " "; f_carta3_c = " "

# Cantidad de Puntos
mano_jugador = n_carta1 + n_carta2
mano_crupier = n_carta1_c + n_carta2_c

# Logica de cartas del jugador
if n_carta1 == 10:  # Dar una figura a las cartas que valgan 10 puntos (J, Q y K)
    f_carta1 = letra[random.randint(0, 3)]
if n_carta2 == 10:
    f_carta2 = letra[random.randint(0, 3)]

if n_carta1 == 11:  # Dar figura al AS
    f_carta1 = "A"
if n_carta2 == 11:
    f_carta2 = "A"

if mano_jugador > 21:  # Definir si el AS vale 1 punto, cuando la mano supera 21
    if f_carta1 == "A" and f_carta2 != "A":
        mano_jugador -= 10
    elif f_carta2 == "A" and f_carta1 != "A":
        mano_jugador -= 10
    elif f_carta1 == "A" and f_carta2 == "A":
        mano_jugador -= 10

# Imprimir las cartas, dependiendo si son letras o numeros
if f_carta1 == " " and f_carta2 == " ":  # Ej: 3 y 5
    print("Cartas del JUGADOR: ", str(n_carta1) + palo_j," ",str(n_carta2) + palo_j2)
    print("Mano: ", mano_jugador)

elif f_carta1 == " " and f_carta2 != " ":  # Ej: 3 y J
    print("Cartas del JUGADOR: ", str(n_carta1) + palo_j," ",str(f_carta2) + palo_j2)
    print("Mano: ", mano_jugador)

elif f_carta1 != " " and f_carta2 == " ":  # Ej: J y 3
    print("Cartas del JUGADOR: ", str(f_carta1) + palo_j," ", str(n_carta2) + palo_j2)
    print("Mano: ", mano_jugador)

elif f_carta1 != " " and f_carta2 != " ":  # Ej: Q y J
    print("Cartas del JUGADOR: ", str(f_carta1) + palo_j," ", str(f_carta2) + palo_j2)
    print("Mano: ", mano_jugador)

# El jugador pide la tercera Carta si la mano es menos o igual a 16
if mano_jugador <= 16:

    # Define si la carta AS vale 1 o 11
    if n_carta3 == 11:
        if mano_jugador <= 10:
            n_carta3 = 11
            mano_jugador += n_carta3
        elif 10 < mano_jugador <= 16:
            n_carta3 = 1
            mano_jugador += n_carta3

    # Le da una figura a una carta si vale 10 puntos (J, Q o K)
    if n_carta3 == 10:
        f_carta3 = letra[random.randint(0, 3)]

    # Le da figura al AS
    if n_carta3 == 11:
        f_carta3 = "A"
    elif n_carta3 == 1:
        f_carta3 = "A"

    # Imprime o el numero o la figura de la 3ra carta
    if f_carta3 != " ":
        print("El JUGADOR obtiene una tercera carta: " + str(f_carta3) + palo_j3)

    elif f_carta3 == " ":
        mano_jugador += n_carta3
        print("El JUGADOR obtiene una tercera carta: " + str(n_carta3) + palo_j3)
else:
    print("No se entrega tercera carta")
    print(" ")
    # Mano final de jugador
print("La mano final del JUGADOR: ", mano_jugador)
print(" ")

print("---------------------")
print("| TURNO DEL CRUPIER |")
print("---------------------")

# Logica de cartas del jugador
if n_carta1_c == 10:  # Dar una figura a las cartas que valgan 10 puntos (J, Q y K)
    f_carta1_c = letra[random.randint(0, 3)]
if n_carta2_c == 10:
    f_carta2_c = letra[random.randint(0, 3)]

if n_carta1_c == 11:  # Dar figura al AS
    f_carta1_c = "A"
if n_carta2_c == 11:
    f_carta2_c = "A"

if mano_crupier > 21:  # Definir si el AS vale 1 punto, cuando la mano supera 21
    if f_carta1_c == "A" and f_carta2 != "A":
        mano_crupier -= 10
    elif f_carta2_c == "A" and f_carta1 != "A":
        mano_crupier -= 10
    elif f_carta1_c == "A" and f_carta2 == "A":
        mano_crupier -= 10

# Imprimir las cartas, dependiendo si son letras o numeros
if f_carta1_c == " " and f_carta2_c == " ":  # Ej: 3 y 5
    print("Cartas del CRUPIER: ", str(n_carta1_c) + palo_c,str(n_carta2_c) + palo_c2)
    print("Mano: ", mano_crupier)

elif f_carta1_c == " " and f_carta2_c != " ":  # Ej: 3 y J
    print("Cartas del CRUPIER: ", str(n_carta1_c) + palo_c,str(f_carta2_c) + palo_c2)
    print("Mano: ", mano_crupier)

elif f_carta1_c != " " and f_carta2_c == " ":  # Ej: J y 3
    print("Cartas del CRUPIER: ", str(f_carta1_c) + palo_c,str(n_carta2_c) + palo_c2)
    print("Mano: ", mano_crupier)

elif f_carta1_c != " " and f_carta2_c != " ":  # Ej: Q y J
    print("Cartas del CRUPIER: ", str(f_carta1_c) + palo_c,str(f_carta2_c) + palo_c2)
    print("Mano: ", mano_crupier)

# El jugador pide la tercera Carta si la mano es menos o igual a 16
if mano_crupier <= 16:

    # Define si la carta AS vale 1 o 11
    if n_carta3_c == 11:
        if mano_crupier <= 10:
            n_carta3_c = 11
            mano_crupier += n_carta3_c
        elif 10 < mano_crupier <= 16:
            n_carta3_c = 1
            mano_crupier += n_carta3_c

    # Le da figura al AS
    if n_carta3_c == 11:
        f_carta3_c = "A"
    elif n_carta3_c == 1:
        f_carta3_c = "A"

    # Le da una figura a una carta si vale 10 puntos (J, Q o K)
    if n_carta3_c == 10:
        f_carta3_c = letra[random.randint(0, 3)]

    # Imprime o el numero o la figura de la 3ra carta
    if f_carta3_c != " ":
        print("El CRUPIER obtiene una tercera carta: " + str(f_carta3_c) + palo_c3)
    elif f_carta3_c == " ":
        print("El CRUPIER obtiene una tercera carta: " + str(n_carta3_c) + palo_c3)

else:
    print("No se entrega tercera carta")
    print(" ")

# Mano final del crupier
print("La mano final del CRUPIER: ", mano_crupier)
print(" ")

print("--------------")
print("| RESULTADOS |")
print("--------------")

# Compara las similitudes en la primera carta entre Jugador y Crupier
if palo_j == palo_c:
    print("La carta 1 del JUGADOR y la carta 1 del CRUPIER son del mismo palo")
    if (n_carta1 == n_carta1_c) == 10:
        if f_carta1 == f_carta1_c:
            print("La carta N°1 del JUGADOR y la carta N°1 del CRUPIER SON IGUALES")
    elif 1 < (n_carta1 == n_carta1_c) < 10:
        print("La carta N°1 del JUGADOR y la carta N°1 del CRUPIER SON IGUALES")
    elif f_carta1 == "A" and f_carta1_c == "A":
        print("La carta N°1 del JUGADOR y la carta N°1 del CRUPIER SON IGUALES")

if n_carta1 == 10 or n_carta2 == 10 or n_carta3 == 10:
    if (n_carta1 or n_carta2 or n_carta3) != "10":
        print ("En la mano del JUGADOR toco al menos una figura")
elif n_carta1_c == 10 or n_carta2_c == 10 or n_carta3_c == 10:
    if (n_carta1_c or n_carta2_c or n_carta3_c) != "10":
        print ("En la mano del CRUPIER toco al menos una figura")

# Define el resultado Final
if mano_jugador < 21 and mano_crupier < 21:
    if mano_crupier > mano_jugador:
        print ("El ganador es el CRUPIER")
    elif mano_jugador > mano_crupier:
        print ("El ganador es el JUGADOR")
    elif mano_jugador == mano_crupier:
        print("El JUGADOR y el CRUPIER empataron")

elif mano_crupier > 21 and mano_jugador <= 21:
    print("El ganador es el JUGADOR")
elif mano_jugador > 21 and mano_crupier <= 21:
    print ("El ganador es el CRUPIER")
elif mano_jugador > 21 and mano_crupier > 21:
    print("El JUGADOR y el CRUPIER pasaron de 21, AMBOS pierden")

