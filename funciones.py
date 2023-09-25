import string
diccionario = string.ascii_lowercase #Define el alfabeto en minisculas

### Funcion de cifrado ROT
def rot_cifrado(mensaje, numero):
    cifrado = ''
    for i in mensaje:
        if i in diccionario:
            posicion = (diccionario.find(i) + numero) % len(diccionario)#encuentra la posicion del caracter en el alfabeto y aplica ROT
            cifrado += diccionario[posicion]
        else:
            cifrado += i  #caracteres que no están en el alfabeto
    return cifrado

### Función de descifrado ROT
def rot_descifrado(mensaje, numero):
    descifrado = ''
    for i in mensaje:
        if i in diccionario:
            posicion = (diccionario.find(i) - numero) % len(diccionario)#posicion del caracter en el alfabeto y aplica ROT inverso
            descifrado += diccionario[posicion]
        else:
            descifrado += i  #caracteres que no estan en el alfabeto
    return descifrado

### Funcion de cifrado y descifrado Vigenere.
def vigenere(mensaje, clave_original, modo):
    clave = ''
    # Asegura que la clave tenga la misma longitud que el mensaje
    if len(mensaje) > len(clave_original):
        clave = clave_original * (len(mensaje) // len(clave_original))
        clave += clave_original[:len(mensaje) % len(clave_original)]
    elif len(mensaje) < len(clave_original):
        clave = clave_original[:len(mensaje)]
    else:
        clave = clave_original

    resultado = ''

    for i in range(len(mensaje)):
        if mensaje[i] in diccionario and clave[i] in diccionario:
            # Encuentra las posiciones en el alfabeto y aplica el cifrado Vigenere o descifrado
            x = diccionario.find(mensaje[i])
            y = diccionario.find(clave[i])
            if modo == 'cifrado':
                suma = x + y
                posicion = suma % len(diccionario)
            elif modo == 'descifrado':
                resta = x - y
                posicion = resta % len(diccionario)
            resultado += diccionario[posicion]
        else:
            resultado += mensaje[i]  #caracteres que no estan en el alfabeto

    return resultado